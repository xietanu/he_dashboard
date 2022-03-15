"""Test add_z_score function"""
from util.query_string import query_string_to_kwargs, kwargs_to_query_string


## query_string_to_kwargs


def test_query_string_to_kwargs_empty():
    """Test an empty query string returns and empty dict"""
    kwargs = query_string_to_kwargs("?")

    kwargs_expected = {}

    assert kwargs == kwargs_expected


def test_query_string_to_kwargs_single():
    """Test basic key:value pair is read correctly"""
    kwargs = query_string_to_kwargs("?key=value")

    kwargs_expected = {"key": "value"}

    assert kwargs == kwargs_expected


def test_query_string_to_kwargs_multiple_arguments():
    """Test multiple key:value pairs are read correctly"""
    kwargs = query_string_to_kwargs("?key=value&second_key=second_value")

    kwargs_expected = {"key": "value", "second_key": "second_value"}

    assert kwargs == kwargs_expected


def test_query_string_to_kwargs_arg_with_spaces():
    """Check that spaces are handled correctly"""
    kwargs = query_string_to_kwargs("?key=value+with+spaces")

    kwargs_expected = {"key": "value with spaces"}

    assert kwargs == kwargs_expected


### kwargs_to_query_string


def test_kwargs_to_query_string():
    """Check that no arguments given returns an empty query string"""
    query_string = kwargs_to_query_string(**{})

    query_string_expected = "?"

    assert query_string == query_string_expected


def test_kwargs_to_query_string_single():
    """Check that a single key:value pair are written correctly"""
    query_string = kwargs_to_query_string(**{"key": "value"})

    query_string_expected = "?key=value"

    assert query_string == query_string_expected


def test_kwargs_to_query_string_multiple_arguments():
    """Check that multiple key value pairs are written correctly"""
    query_string = kwargs_to_query_string(
        **{"key": "value", "second_key": "second_value"}
    )

    query_string_expected = "?key=value&second_key=second_value"

    assert query_string == query_string_expected


def test_kwargs_to_query_string_arg_with_spaces():
    """Check that a value with spaces is written correctly"""
    query_string = kwargs_to_query_string(**{"key": "value with spaces"})

    query_string_expected = "?key=value+with+spaces"

    assert query_string == query_string_expected
