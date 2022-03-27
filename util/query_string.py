"""Functions to convert between query string and kwargs"""


def kwargs_to_query_string(**kwargs) -> str:
    """
    Converts keyword arguments to query string for URL

    Returns:
        str: Generated query string
    """
    query_string = "?" + "&".join([f"{key}={value}" for key, value in kwargs.items()])
    return query_string.replace(" ", "+")


def query_string_to_kwargs(query_string: str) -> dict:
    """
    Converts URL query string to keyword arguments.

    Args:
        query_string (str): URL query string

    Returns:
        dict: Generated keyword arguments
    """
    key_value_pairs = query_string[1:].split("&")
    output = {}
    for key_value_pair in key_value_pairs:
        if "=" in key_value_pair:
            key, value = key_value_pair.split("=")
            output[key] = value.replace("+", " ")
    return output
