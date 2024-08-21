from typing import List
from schemas.patient_schema import PatientCreate, PatientUpdate, PatientResponse
from repository.patient_repo import Patient_Repository
from domain.patient_domain import PatientDomain


def get_patient_service():
    return PatientService(Patient_Repository())


class PatientService:
    def __init__(self, repository: Patient_Repository):
        self.repository = repository

    def create_patient(self, patient: PatientCreate) -> PatientResponse:
        patient_domain = PatientDomain(id=None, **patient.dict())
        created_patient = self.repository.create(patient_domain)
        return PatientResponse(**created_patient.to_dict())

    def list_patients(self) -> list[PatientResponse]:
        patients = self.repository.list()
        return [PatientResponse(**patient.to_dict()) for patient in patients]

    def list_patients_by_hospital(self, hospital_id: str) -> list[PatientResponse]:
        patients = self.repository.find_by_hospital_id(hospital_id)
        return [PatientResponse(**patient.to_dict()) for patient in patients]
