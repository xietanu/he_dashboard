"""Takes the data from the raw tables and processes it for use in the student timeseries data"""
from pandas import read_csv

from data.research.columns import REFColumns
from util.add_z_score import add_z_score


def extract_research_quality_metrics():
    """Takes the data from the raw tables and prepares it for the student timeseries data"""
    converters = {
        REFColumns.GRADE_4STAR_PERCENTAGE.value: lambda x: float(x)
        if x.isnumeric()
        else 0,
        REFColumns.GRADE_3STAR_PERCENTAGE.value: lambda x: float(x)
        if x.isnumeric()
        else 0,
        REFColumns.GRADE_2STAR_PERCENTAGE.value: lambda x: float(x)
        if x.isnumeric()
        else 0,
        REFColumns.GRADE_1STAR_PERCENTAGE.value: lambda x: float(x)
        if x.isnumeric()
        else 0,
        REFColumns.GRADE_UNCLASSIFIED_PERCENTAGE.value: lambda x: float(x)
        if x.isnumeric()
        else 0,
    }
    ref_2014_table = read_csv(
        "data/research/raw/REF2014.csv", skiprows=7, converters=converters
    )

    add_research_quality_metrics(ref_2014_table)

    ref_2014_table = filter_to_overall_score(ref_2014_table)

    ref_2014_table_weighted_volume = calc_total_weighted_volume_per_uni(ref_2014_table)

    ref_2014_table_quality_score = calc_avg_quality_score_per_uni(ref_2014_table)

    ref_2014_table_output = ref_2014_table_weighted_volume.join(
        ref_2014_table_quality_score
    )

    add_z_score(
        ref_2014_table_output,
        REFColumns.QUALITY_SCORE.value,
        REFColumns.QUALITY_SCORE_Z.value,
    )
    add_z_score(
        ref_2014_table_output,
        REFColumns.QUALITY_WEIGHTED_VOLUME.value,
        REFColumns.QUALITY_WEIGHTED_VOLUME_Z.value,
    )

    ref_2014_table_output[
        [REFColumns.QUALITY_SCORE_Z.value, REFColumns.QUALITY_WEIGHTED_VOLUME_Z.value]
    ] = round(
        ref_2014_table_output[
            [
                REFColumns.QUALITY_SCORE_Z.value,
                REFColumns.QUALITY_WEIGHTED_VOLUME_Z.value,
            ]
        ],
        2,
    )

    ref_2014_table_output = (
        ref_2014_table_output.reset_index()
        .melt(
            id_vars=[
                REFColumns.HE_PROVIDER_CODE.value,
                REFColumns.HE_PROVIDER_NAME.value,
            ],
            value_vars=[
                REFColumns.QUALITY_SCORE_Z.value,
                REFColumns.QUALITY_WEIGHTED_VOLUME_Z.value,
            ],
            var_name="Metric",
            value_name="Value",
        )
        .sort_values(by=REFColumns.HE_PROVIDER_CODE.value, ignore_index=True)
    )

    ref_2014_table_output.to_csv(
        "data/research/research_quality_metrics.csv", index=False
    )


def calc_avg_quality_score_per_uni(dataframe):
    """Calculate a dataframe with an average quality score for each uni"""
    ref_2014_table_quality_score = dataframe[
        [
            REFColumns.HE_PROVIDER_CODE.value,
            REFColumns.HE_PROVIDER_NAME.value,
            REFColumns.FTE_STAFF.value,
            REFColumns.QUALITY_SCORE.value,
        ]
    ]
    ref_2014_table_quality_score = (
        ref_2014_table_quality_score.groupby(
            by=[
                REFColumns.HE_PROVIDER_CODE.value,
                REFColumns.HE_PROVIDER_NAME.value,
            ]
        )
        .sum()
        .copy()
    )

    ref_2014_table_quality_score[REFColumns.QUALITY_SCORE.value] = (
        ref_2014_table_quality_score[REFColumns.QUALITY_SCORE.value]
        / ref_2014_table_quality_score[REFColumns.FTE_STAFF.value]
    )
    return ref_2014_table_quality_score


def calc_total_weighted_volume_per_uni(dataframe):
    """Calculate the total weighted volume of research for each uni"""
    ref_2014_table_weighted_volume = dataframe[
        [
            REFColumns.HE_PROVIDER_CODE.value,
            REFColumns.HE_PROVIDER_NAME.value,
            REFColumns.QUALITY_WEIGHTED_VOLUME.value,
        ]
    ]
    ref_2014_table_weighted_volume = (
        ref_2014_table_weighted_volume.groupby(
            by=[
                REFColumns.HE_PROVIDER_CODE.value,
                REFColumns.HE_PROVIDER_NAME.value,
            ]
        )
        .sum()
        .copy()
    )

    ref_2014_table_weighted_volume[REFColumns.QUALITY_WEIGHTED_VOLUME.value] = (
        ref_2014_table_weighted_volume[REFColumns.QUALITY_WEIGHTED_VOLUME.value]
    ).copy()

    return ref_2014_table_weighted_volume


def filter_to_overall_score(dataframe):
    """Filter out sub categories of ref scores"""
    return dataframe[(dataframe[REFColumns.PROFILE.value] == "Overall")]


def add_research_quality_metrics(dataframe):
    """Add quality scores and quality weighted volume of research columns"""
    dataframe[REFColumns.QUALITY_SCORE.value] = (
        dataframe[REFColumns.FTE_STAFF.value]
        * (
            dataframe[REFColumns.GRADE_4STAR_PERCENTAGE.value]
            + dataframe[REFColumns.GRADE_3STAR_PERCENTAGE.value]
        )
        / (
            dataframe[REFColumns.GRADE_4STAR_PERCENTAGE.value]
            + dataframe[REFColumns.GRADE_3STAR_PERCENTAGE.value]
            + dataframe[REFColumns.GRADE_2STAR_PERCENTAGE.value]
        )
    )

    dataframe[REFColumns.QUALITY_WEIGHTED_VOLUME.value] = (
        dataframe[REFColumns.FTE_STAFF.value]
        * (
            dataframe[REFColumns.GRADE_4STAR_PERCENTAGE.value] * 4
            + dataframe[REFColumns.GRADE_3STAR_PERCENTAGE.value]
        )
        / 500
    )
