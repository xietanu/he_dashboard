"""Takes the data from the raw tables and processes it for use in the student timeseries data"""
from pandas import read_csv

from columns import REFColumns  # pylint: disable=import-error


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
    ref_2014_table = read_csv("raw/REF2014.csv", skiprows=7, converters=converters)

    ref_2014_table[REFColumns.QUALITY_SCORE.value] = (
        ref_2014_table[REFColumns.FTE_STAFF.value]
        * (
            ref_2014_table[REFColumns.GRADE_4STAR_PERCENTAGE.value]
            + ref_2014_table[REFColumns.GRADE_3STAR_PERCENTAGE.value]
        )
        / (
            ref_2014_table[REFColumns.GRADE_4STAR_PERCENTAGE.value]
            + ref_2014_table[REFColumns.GRADE_3STAR_PERCENTAGE.value]
            + ref_2014_table[REFColumns.GRADE_2STAR_PERCENTAGE.value]
        )
    )
    ref_2014_table[REFColumns.QUALITY_WEIGHTED_VOLUME.value] = (
        ref_2014_table[REFColumns.FTE_STAFF.value]
        * (
            ref_2014_table[REFColumns.GRADE_4STAR_PERCENTAGE.value] * 4
            + ref_2014_table[REFColumns.GRADE_3STAR_PERCENTAGE.value]
        )
        / 500
    )

    ref_2014_table = ref_2014_table[
        (ref_2014_table[REFColumns.PROFILE.value] == "Overall")
    ]

    ref_2014_table_weighted_volume = ref_2014_table[
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

    ref_2014_table_quality_score = ref_2014_table[
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

    ref_2014_table_output = ref_2014_table_weighted_volume.join(
        ref_2014_table_quality_score
    )

    quality_score_mean = ref_2014_table_output[REFColumns.QUALITY_SCORE.value].mean()
    quality_score_std = ref_2014_table_output[REFColumns.QUALITY_SCORE.value].std()
    quality_weighted_volume_mean = ref_2014_table_output[
        REFColumns.QUALITY_WEIGHTED_VOLUME.value
    ].mean()
    quality_weighted_volume_std = ref_2014_table_output[
        REFColumns.QUALITY_WEIGHTED_VOLUME.value
    ].std()

    ref_2014_table_output[REFColumns.QUALITY_SCORE_Z.value] = (
        ref_2014_table_output[REFColumns.QUALITY_SCORE.value] - quality_score_mean
    ) / quality_score_std
    ref_2014_table_output[REFColumns.QUALITY_WEIGHTED_VOLUME_Z.value] = (
        ref_2014_table_output[REFColumns.QUALITY_WEIGHTED_VOLUME.value]
        - quality_weighted_volume_mean
    ) / quality_weighted_volume_std

    ref_2014_table_output[
        [REFColumns.QUALITY_WEIGHTED_VOLUME.value, REFColumns.FTE_STAFF.value]
    ] = round(
        ref_2014_table_output[
            [REFColumns.QUALITY_WEIGHTED_VOLUME.value, REFColumns.FTE_STAFF.value]
        ],
        1,
    )

    ref_2014_table_output.loc[:,REFColumns.QUALITY_SCORE.value :] = round(
        ref_2014_table_output.loc[:,REFColumns.QUALITY_SCORE.value :],
        2,
    )

    ref_2014_table_output.to_csv("research_quality_metrics.csv")


if __name__ == "__main__":
    extract_research_quality_metrics()
