"""Enum for coluumns in the REF data"""
from enum import Enum


class REFColumns(Enum):
    """The columns in the REF (Research Excellence Framework) data"""

    HE_PROVIDER_CODE = "Institution code (UKPRN)"
    HE_PROVIDER_NAME = "Institution name"
    SORT_ORDER = "Institution sort order"
    MAIN_PANEL = "Main panel"
    UNIT_OF_ASSESSMENT_CODE = "Unit of assessment number"
    UNIT_OF_ASSESSMENT_NAME = "Unit of assessment name"
    MULTIPLE_SUBMISSION_CODE = "Multiple submission letter"
    MULTIPLE_SUBMISSION_NAME = "Multiple submission name"
    JOINT_SUBMISSION = "Joint submission"
    PROFILE = "Profile"
    FTE_STAFF = "FTE Category A staff submitted"
    GRADE_4STAR_PERCENTAGE = "4*"
    GRADE_3STAR_PERCENTAGE = "3*"
    GRADE_2STAR_PERCENTAGE = "2*"
    GRADE_1STAR_PERCENTAGE = "1*"
    GRADE_UNCLASSIFIED_PERCENTAGE = "unclassified"
    QUALITY_WEIGHTED_VOLUME = "Total quality weighted volume"
    QUALITY_WEIGHTED_VOLUME_Z = "Total quality weighted volume - Z score"
    QUALITY_SCORE = "Quality score"
    QUALITY_SCORE_Z = "Quality score - Z score"
