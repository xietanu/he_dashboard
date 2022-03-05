"""Enum for coluumns in the student data"""
from enum import Enum


class StudentColumns(Enum):
    """The columns in the student data"""

    HE_PROVIDER_CODE = "UKPRN"
    HE_PROVIDER_NAME = "HE provider"
    COUNTRY = "Country of HE provider"
    REGION = "Region of HE provider"
    ACADEMIC_YEAR = "Academic Year"
    LEVEL_OF_STUDY = "Level of study"
    NUMBER = "Number"
