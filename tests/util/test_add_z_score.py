"""Test add_z_score function"""
from pandas import DataFrame
from pandas.testing import assert_frame_equal

from util.add_z_score import add_z_score


def test_add_z_score_unit():
    """Test case of already z-scored column"""
    test_df = DataFrame(
        {
            "column": [-1, 1],
        }
    )
    add_z_score(test_df, "column", "z_column")

    expected_df = DataFrame(
        {
            "column": [-1, 1],
            "z_column": [-1.0, 1.0],
        }
    )

    assert_frame_equal(test_df, expected_df)


def test_add_z_score_basic():
    """Basic case with two values"""
    test_df = DataFrame(
        {
            "column": [1, 3],
        }
    )
    add_z_score(test_df, "column", "z_column")

    expected_df = DataFrame(
        {
            "column": [1, 3],
            "z_column": [-1.0, 1.0],
        }
    )

    assert_frame_equal(test_df, expected_df)


def test_add_z_score_more_values():
    """Test case of more columns"""
    test_df = DataFrame(
        {
            "column": [-1, 0, 1, 3, -3],
        }
    )
    add_z_score(test_df, "column", "z_column")

    expected_df = DataFrame(
        {
            "column": [-1, 0, 1, 3, -3],
            "z_column": [-0.5, 0, 0.5, 1.5, -1.5],
        }
    )

    assert_frame_equal(test_df, expected_df)
