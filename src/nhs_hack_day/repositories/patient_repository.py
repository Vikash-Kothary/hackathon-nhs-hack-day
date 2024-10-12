

patients = {}

def list_patients():
    return list(patients.values())

def create_new_patient(patient):
    global patients
    patients[patient.patient_id] = patient
    return patient
