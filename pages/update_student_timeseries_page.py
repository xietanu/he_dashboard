"""update_student_timeseries_page function"""
from components.graph import graph
from data.students.columns import StudentColumns
from figures.timeseries import timeseries
from util.he_data import HEData, HEDataColumn


def update_student_timeseries_page(data: HEData, selected_university: str) -> list:
    """
    Function to update the student timeseries page with selected univerities.

    Args:
        data (HEData): Data containing student types.
        selected_university (str): University to display data for.
            If None, displays aggregate data for the UK.

    Returns:
        list: List of HTML elements to display.
    """
    dataframe = data.get_dataframe(providers=selected_university)

    dataframe = dataframe.groupby(
        by=[HEDataColumn.ACADEMIC_YEAR.value, StudentColumns.LEVEL_OF_STUDY.value],
        as_index=False,
    )[StudentColumns.NUMBER.value].sum()

    visualisation = timeseries(
        dataframe,
        HEDataColumn.ACADEMIC_YEAR.value,
        StudentColumns.NUMBER.value,
        StudentColumns.LEVEL_OF_STUDY.value,
    )

    return [graph(element_id="student-enrolment-timeseries", figure=visualisation)]
