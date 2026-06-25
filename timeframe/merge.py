from timeframe.align import align_to_base


def merge(base, higher, tf_name):
    cols = [c for c in higher.columns if c != "UTC"]

    rename = {c: f"{tf_name}_{c}" for c in cols}

    higher = higher.rename(columns=rename)

    merged = align_to_base(base, higher)

    return merged
