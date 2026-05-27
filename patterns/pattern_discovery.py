"""
Advanced Pattern Discovery System
Automatically identifies indicator combinations that form consistent, valid patterns.
"""

import pandas as pd
import numpy as np
from collections import defaultdict
from sklearn.preprocessing import StandardScaler
from itertools import combinations


class PatternDiscovery:
    """Discover consistent market reaction patterns from indicator and context data"""
    
    def __init__(self, df, min_frequency=10, min_directional_confidence=55):
        """
        Args:
            df: DataFrame with indicators and OHLCV data
            min_frequency: Minimum occurrences to consider pattern valid
            min_directional_confidence: Minimum dominant direction percentage required
        """
        self.df = df
        self.min_frequency = min_frequency
        self.min_directional_confidence = min_directional_confidence / 100
        self.patterns = []
        self.clusters = {}
        
    def _get_indicator_columns(self):
        """Get all indicator columns (exclude OHLCV)"""
        exclude = {'UTC', 'Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume'}
        return [col for col in self.df.columns if col not in exclude]
    
    def _calculate_price_move(self):
        """Calculate price movement in percentage"""
        return (self.df['Close'] - self.df['Open']) / self.df['Open'] * 100
    
    def _get_bullish_indicators_vectorized(self):
        """
        Vectorized approach to get bullish indicators for all rows at once.
        Much faster than row-by-row processing for large datasets.
        """
        indicators = self._get_indicator_columns()
        pattern_dict = defaultdict(list)
        
        # Create binary masks for each indicator column
        binary_indicators = {}
        
        for col in indicators:
            # Skip all-NaN columns
            if self.df[col].isna().all():
                continue
                
            # For boolean/binary indicators
            if col.startswith('DOJI') or col.startswith('COMPRESSION') or \
               col.startswith('VOL_REGIME') or col.startswith('BOS_') or \
               col.startswith('SQUEEZE_'):
                binary_indicators[col] = (self.df[col] == 1) | (self.df[col] == True)
            # For continuous indicators - check if > median
            else:
                median_val = self.df[col].median()
                if pd.notna(median_val):
                    binary_indicators[col] = self.df[col] > median_val
        
        # Build patterns efficiently
        for idx in range(len(self.df)):
            bullish = []
            for col, mask in binary_indicators.items():
                if mask.iloc[idx]:
                    bullish.append(col)
            
            if bullish:
                pattern_tuple = tuple(sorted(bullish))
                pattern_dict[pattern_tuple].append(idx)
        
        return pattern_dict
    
    def _score_pattern(self, indices, price_moves):
        """Calculate a consistency score for a candidate pattern"""
        if len(indices) < self.min_frequency:
            return 0
        
        bullish_count = (price_moves > 0).sum()
        bearish_count = (price_moves < 0).sum()
        flat_count = (price_moves == 0).sum()
        total = len(price_moves)
        
        bullish_pct = bullish_count / total
        bearish_pct = bearish_count / total
        neutral_pct = flat_count / total
        
        dominant_pct = max(bullish_pct, bearish_pct, neutral_pct)
        dominant_direction = (
            'bullish' if bullish_pct == dominant_pct else
            'bearish' if bearish_pct == dominant_pct else
            'neutral'
        )
        
        if dominant_pct < self.min_directional_confidence:
            return 0
        
        nondominant_count = total - max(bullish_count, bearish_count, flat_count)
        dominance_ratio = (
            max(bullish_count, bearish_count, flat_count) / nondominant_count
            if nondominant_count > 0 else float('inf')
        )
        
        move_mean = price_moves.mean()
        move_std = price_moves.std()
        move_var = price_moves.var()
        p10 = np.percentile(price_moves, 10)
        p25 = np.percentile(price_moves, 25)
        p50 = np.percentile(price_moves, 50)
        p75 = np.percentile(price_moves, 75)
        p90 = np.percentile(price_moves, 90)
        skewness = price_moves.skew()
        kurtosis = price_moves.kurtosis()
        
        # ATR-normalized move if ATR_14 is available
        atr_norm = None
        if 'ATR_14' in self.df.columns:
            atr = self.df.loc[indices, 'ATR_14'].replace(0, np.nan)
            atr_norm = (price_moves / atr).dropna()
        
        atr_normalized_mean = float(atr_norm.mean()) if atr_norm is not None and len(atr_norm) > 0 else None
        atr_normalized_std = float(atr_norm.std()) if atr_norm is not None and len(atr_norm) > 0 else None
        
        magnitude_consistency = 1 / (1 + abs(move_std)) if move_std is not None else 0
        
        score = len(indices) * dominant_pct * magnitude_consistency
        
        return {
            'score': score,
            'frequency': len(indices),
            'dominant_direction': dominant_direction,
            'directional_confidence': dominant_pct * 100,
            'dominance_ratio': dominance_ratio,
            'bullish_pct': bullish_pct * 100,
            'bearish_pct': bearish_pct * 100,
            'neutral_pct': neutral_pct * 100,
            'avg_move': move_mean,
            'median_move': p50,
            'min_move': price_moves.min(),
            'max_move': price_moves.max(),
            'move_std': move_std,
            'move_var': move_var,
            'p10': p10,
            'p25': p25,
            'p50': p50,
            'p75': p75,
            'p90': p90,
            'skewness': skewness,
            'kurtosis': kurtosis,
            'atr_normalized_mean': atr_normalized_mean,
            'atr_normalized_std': atr_normalized_std,
        }
    
    def discover(self, max_patterns=20):
        """
        Discover patterns by analyzing indicator combinations.
        Optimized for speed using vectorized operations.
        
        Returns:
            List of valid patterns ranked by quality score
        """
        
        price_moves = self._calculate_price_move()
        
        # Get all patterns using vectorized approach
        print("[Pattern Discovery] Analyzing indicator combinations...")
        pattern_dict = self._get_bullish_indicators_vectorized()
        
        print(f"[Pattern Discovery] Found {len(pattern_dict)} unique combinations")
        
        # Score each pattern
        print("[Pattern Discovery] Scoring patterns...")
        valid_patterns = []
        
        for combo, indices in pattern_dict.items():
            price_move_values = price_moves.iloc[indices]
            score_info = self._score_pattern(indices, price_move_values)
            
            if isinstance(score_info, dict) and score_info['score'] > 0:
                valid_patterns.append({
                    'indicators': list(combo),
                    'indicator_count': len(combo),
                    'indices': indices,
                    **score_info
                })
        
        # Sort by score
        valid_patterns.sort(key=lambda x: x['score'], reverse=True)
        
        # Keep top patterns
        self.patterns = valid_patterns[:max_patterns]
        
        print(f"[Pattern Discovery] Found {len(self.patterns)} valid patterns")
        return self.patterns
    
    def get_pattern_details(self, pattern_idx=0):
        """Get detailed information about a pattern"""
        if not self.patterns or pattern_idx >= len(self.patterns):
            return None
        
        pattern = self.patterns[pattern_idx]
        indices = pattern['indices']
        
        # Get sample rows
        sample_rows = self.df.iloc[indices[:10]].copy()
        sample_rows['PriceMove'] = (sample_rows['Close'] - sample_rows['Open']) / sample_rows['Open'] * 100
        
        pattern['sample_rows'] = sample_rows
        pattern['sample_count'] = len(sample_rows)
        
        return pattern
    
    def export_patterns_csv(self, filepath):
        """Export discovered patterns to CSV"""
        pattern_data = []
        
        for i, pattern in enumerate(self.patterns):
            pattern_data.append({
                'Rank': i + 1,
                'Indicators': ','.join(pattern['indicators']),
                'Count': pattern['frequency'],
                'Dominant_Direction': pattern['dominant_direction'],
                'Directional_Confidence_%': round(pattern['directional_confidence'], 2),
                'Avg_Move_%': round(pattern['avg_move'], 4),
                'Move_STD': round(pattern['move_std'], 4),
                'P10_%': round(pattern['p10'], 4),
                'P90_%': round(pattern['p90'], 4),
                'Quality_Score': round(pattern['score'], 2)
            })
        
        df_export = pd.DataFrame(pattern_data)
        df_export.to_csv(filepath, index=False)
        return df_export
    
    def generate_report_data(self, top_n=10):
        """Generate data suitable for HTML report"""
        report_data = {
            'total_patterns_found': len(self.patterns),
            'patterns': []
        }
        
        for pattern in self.patterns[:top_n]:
            pattern_details = {
                'indicators': ', '.join(pattern['indicators']),
                'frequency': pattern['frequency'],
                'dominant_direction': pattern['dominant_direction'],
                'directional_confidence': f"{pattern['directional_confidence']:.2f}%",
                'avg_move': f"{pattern['avg_move']:.4f}%",
                'median_move': f"{pattern['median_move']:.4f}%",
                'min_move': f"{pattern['min_move']:.4f}%",
                'max_move': f"{pattern['max_move']:.4f}%",
                'move_std': f"{pattern['move_std']:.4f}",
                'p10': f"{pattern['p10']:.4f}%",
                'p90': f"{pattern['p90']:.4f}%",
                'skewness': f"{pattern['skewness']:.4f}",
                'kurtosis': f"{pattern['kurtosis']:.4f}",
                'quality_score': f"{pattern['score']:.2f}"
            }
            report_data['patterns'].append(pattern_details)
        
        return report_data
