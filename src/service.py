
""" Helper function to convert input argument into float """


def to_float(s):
    try:
        return float(s)
    except ValueError:
        return False
