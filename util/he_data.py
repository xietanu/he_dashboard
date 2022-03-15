from pandas import DataFrame


class HEData:
    def __init__(
        self, dataframe: DataFrame, academic_year_column: str, provider_column: str
    ) -> None:
        self.dataframe = dataframe
        self.academic_year_column = academic_year_column
        self.provider_column = provider_column

    def get_filtered_dataframe(
        self, selected_university: str = None, academic_year: str = None
    ) -> DataFrame:
        output_df = self.dataframe.copy()
        if selected_university:
            output_df = output_df[
                output_df[self.provider_column] == selected_university
            ]

        if academic_year:
            output_df = output_df[output_df[self.academic_year_column] == academic_year]

        return output_df

    def get_dataframe(self):
        return self.dataframe.copy()
