from fastapi import APIRouter, Depends, HTTPException
from typing import List
from schemas.patient_schema import PatientSchema, PatientCreate, PatientUpdate, PatientResponse
from services.patient_serves import get_patient_service, PatientService

router = APIRouter()


@router.post("/patient", response_model=PatientResponse)
def create_patient(patient: PatientCreate, service: PatientService = Depends(get_patient_service)):
    try:
        return service.create_patient(patient)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/patients", response_model=List[PatientResponse])
def list_patients(service: PatientService = Depends(get_patient_service)):
    try:
        return service.list_patients()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/patient/{patient_id}", response_model=PatientResponse)
def update_patient(patient_id: str, patient_update: PatientUpdate, service: PatientService = Depends(get_patient_service)):
    try:
        return service.update_patient(patient_id, patient_update)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/patient/{patient_id}", response_model=None)
def delete_patient(patient_id: str, service: PatientService = Depends(get_patient_service)):
    try:
        service.delete_patient(patient_id)
        return {"message": "Patient deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
