"""float_like function"""

def float_like(x, /) -> bool:
    """
    Tests if an object could be converted to a float.

    Args:
        x (Any): object to test

    Returns:
        bool: Whether the object can be converted to a float.
    """
    try:
        float(x)
        return True
    except ValueError:
        return False
