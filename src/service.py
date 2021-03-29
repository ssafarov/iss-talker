def to_float(s):
    try:
        return float(s)
    except ValueError:
        return False
