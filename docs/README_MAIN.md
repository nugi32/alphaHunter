# AlphaHunter - Multi-Timeframe Analysis & Report Generator

Sistem terintegrasi untuk menjalankan analisis teknikal pada berbagai timeframe dan menghasilkan laporan HTML otomatis.

## 📁 Struktur File Baru

```
alphaHunter/
├── main.py                    # ← ORCHESTRATOR UTAMA (baru)
├── analysis.py               # Analisis teknikal
├── patterns.txt              # Daftar pola untuk batch analysis (baru)
├── output_*.csv             # CSV hasil analisis (generated)
│
├── report/
│   ├── report_generator.py   # ← UPDATED: Lebih fleksibel
│   ├── run_report.py         # ← UPDATED: Auto-detect CSV
│   ├── reports/              # Folder laporan HTML & gambar
│   ├── templates/
│   │   └── report.html
│   └── dummy_analysis.py
│
└── data/
    └── XAUUSD/
        ├── XAUUSD1.csv       # M1
        ├── XAUUSD5.csv       # M5
        ├── XAUUSD15.csv      # M15
        ├── XAUUSD60.csv      # H1
        ├── XAUUSD240.csv     # H4
        ├── XAUUSD1440.csv    # D1
        ├── XAUUSD10080.csv   # W1
        └── XAUUSD43200.csv   # MN1
```

## 🚀 Cara Menggunakan

### 1. **Run Semua Timeframe Sekaligus**

```bash
python main.py
```

Ini akan:
- Menganalisis semua 8 timeframe (M1, M5, M15, H1, H4, D1, W1, MN1)
- Menyimpan CSV hasil untuk setiap timeframe (`output_M1.csv`, `output_D1.csv`, dll)
- Generate HTML report otomatis untuk masing-masing

### 2. **Run Timeframe Spesifik**

```bash
# Single timeframe
python main.py --tf D1

# Multiple timeframes
python main.py --tf D1 H4 H1

# Tanpa generate report (hanya CSV)
python main.py --tf D1 --no-report
```

### 3. **Analisis dengan Pattern Tertentu**

```bash
# Single pattern
python main.py --pattern "RSI_14>70,MACD>MACD_SIGNAL"

# Dengan timeframe spesifik
python main.py --tf D1 H4 --pattern "EMA_20>EMA_50"
```

### 4. **Batch Analysis dari File Pattern**

```bash
# Gunakan patterns.txt yang sudah ada
python main.py --patterns patterns.txt

# Atau buat file custom Anda sendiri
python main.py --patterns my_patterns.txt
```

File pattern format:
```
# Comment lines (dengan #) akan diabaikan
EMA_20>EMA_50
MACD>MACD_SIGNAL,RSI_14>50
Close>PIVOT
# Blank lines juga diabaikan
```

## 📊 Keluaran

### CSV Files
- `output_M1.csv`, `output_D1.csv`, dll
- Berisi semua indicator yang dihitung
- Dapat digunakan untuk analisis lebih lanjut

### HTML Reports
- Lokasi: `report/reports/`
- Format: `{TIMEFRAME}_{PATTERN}.html`
  - Contoh: `D1_all.html`, `H4_RSI_gt_70.html`
- Berisi:
  - Statistik (total, bullish/bearish, avg move)
  - Histogram distribusi price movement
  - Scatter plot RSI vs Price Move
  - Sample data 10 baris pertama
  - Insights otomatis

### Images
- `report/reports/{TF}_{PATTERN}_histogram.png`
- `report/reports/{TF}_{PATTERN}_scatter.png`

## 📝 Available Patterns

Lihat `patterns.txt` untuk daftar lengkap pattern yang tersedia. Beberapa contoh:

### Single Indicators
```
EMA_20>EMA_50          # EMA 20 di atas EMA 50
RSI_14>70              # RSI overbought
MACD>MACD_SIGNAL       # MACD bullish cross
ADX_14>=20             # Trend kuat
MOMENTUM>0             # Positive momentum
```

### Combined Patterns
```
EMA_20>EMA_50,MACD>MACD_SIGNAL
Close>BB_UPPER,ADX_14>=20
SQUEEZE_ON=true,COMPRESSION=1
```

### Perubahan yang Dilakukan

#### 1. **report_generator.py**
- ✅ Lebih fleksibel: bekerja dengan kolom standard CSV
- ✅ Support pathnames yang lebih panjang
- ✅ Automatic directory creation
- ✅ Better error handling

#### 2. **run_report.py**
- ✅ Auto-detect CSV files
- ✅ Tidak perlu hardcode nama file lagi
- ✅ Batch process multiple CSVs

#### 3. **main.py (BARU)**
- ✅ Orchestrator utama untuk semua operasi
- ✅ Flexible CLI arguments
- ✅ Batch pattern analysis
- ✅ Progress tracking

## 💡 Tips Penggunaan

### Untuk Testing Cepat
```bash
# Test 1 timeframe tanpa report
python main.py --tf D1 --no-report

# Test 1 pattern pada 1 timeframe
python main.py --tf D1 --pattern "RSI_14>70"
```

### Untuk Batch Analysis
```bash
# Analisis dengan banyak pattern
python main.py --patterns patterns.txt

# Hanya timeframe tertentu
python main.py --tf D1 --patterns patterns.txt
```

### Generate Report dari CSV Existing
```bash
cd report
python run_report.py
```

## ⚙️ Modifikasi Pattern

Edit `patterns.txt` untuk menambah/mengubah pattern:

```
# Tambah pattern baru di akhir file
MyNewPattern=1
INDICATOR_A>VALUE,INDICATOR_B<VALUE
```

Pattern akan dijalankan saat `python main.py --patterns patterns.txt`

## 📌 Status

✅ **Selesai:**
- report_generator.py: Updated & flexible
- run_report.py: Updated & auto-detect CSV
- main.py: Created dengan full functionality
- patterns.txt: Template patterns tersedia

**Tested:**
- ✅ D1 timeframe analysis + report generation (14s)
- ✅ CSV output creation
- ✅ HTML report generation dengan proper paths

**Catatan Performance:**
- M1 (~700K candles): ~2-3 minutes
- H1 (~9K candles): ~20s
- D1 (~700 candles): ~15s
- Semua timeframe: ~15-20 minutes total

---

**Next Steps:**
- Jalankan `python main.py --tf D1` untuk test
- Lihat reports di `report/reports/D1_all.html`
- Edit `patterns.txt` sesuai kebutuhan
- Jalankan `python main.py --patterns patterns.txt` untuk batch analysis
