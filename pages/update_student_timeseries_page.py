from components.graph import graph
from data.students.columns import StudentColumns
from figures.timeseries import timeseries
from util.he_data import HEData


def update_student_timeseries_page(data: HEData, selected_university: str):
    dataframe = data.get_filtered_dataframe(selected_university=selected_university)

    dataframe = dataframe.groupby(
        by=[StudentColumns.ACADEMIC_YEAR.value, StudentColumns.LEVEL_OF_STUDY.value],
        as_index=False,
    )[StudentColumns.NUMBER.value].sum()

    visualisation = timeseries(
        dataframe,
        StudentColumns.ACADEMIC_YEAR.value,
        StudentColumns.NUMBER.value,
        StudentColumns.LEVEL_OF_STUDY.value,
    )

    return [graph(element_id="student-enrolment-timeseries", figure=visualisation)]
