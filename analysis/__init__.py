# add these lines to your existing __init__.py
from .search_space     import build_search_space, describe_combo, combo_stats
from .condition_engine import scan_all_combos
from .reaction_engine import measure_reactions
from .consistency    import run_consistency_filter
from .validator      import validate_overfit
from .ranker         import rank_candidates
from .reporter       import generate_report