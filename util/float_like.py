def float_like(x, /):
    try:
        float(x)
        return True
    except ValueError:
        return False
