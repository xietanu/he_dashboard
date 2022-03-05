"""Takes the data from the raw tables and processes it for use in the student timeseries data"""
from pandas import read_csv

from columns import StudentColumns


def extract_student_timeseries_data():
    """Takes the data from the raw tables and prepares it for the student timeseries data"""
    hesa_table_2 = read_csv("raw/table-2.csv", skiprows=20)
    output = (
        hesa_table_2[
            (hesa_table_2[StudentColumns.HE_PROVIDER_CODE.value] > 0)
            & (hesa_table_2[StudentColumns.COUNTRY.value] == "All")
            & (hesa_table_2[StudentColumns.REGION.value] == "All")
            & (hesa_table_2[StudentColumns.LEVEL_OF_STUDY.value] != "Total")
        ]
        .drop([StudentColumns.COUNTRY.value, StudentColumns.REGION.value], axis=1)
        .copy()
    )
    output.to_csv("student_timeseries_data.csv")


if __name__ == "__main__":
    extract_student_timeseries_data()
