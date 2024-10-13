from enum import Enum

class TaskType(Enum):
    RESPIRATORY_MEDICINE = "Respiratory medicine"
    GASTROENTEROLOGY = "Gastroenterology"
    MICROBIOLOGY = "Microbiology"
    ADD_ON_BLOODS_TEST = "Add-on bloods test"
    REFER_INPATIENT_MEDICAL_SPECIALITY = "Refer to inpatient medical speciality"
    REFER_OUTPATIENT_CLINIC = "Refer to outpatient clinic"
    DECIDE_ON_PRESCRIPTION = "Decide on prescription"
    UNKNOWN = "Unknown"

    def __str__(self):
        return str(self.value)