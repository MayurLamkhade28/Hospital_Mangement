from fastapi import FastAPI
from api.hospital_api import router as hospital_router
from api.patient_api import router as patient_router
from api.technician_api import router as technician_router
app = FastAPI()

app.include_router(hospital_router, tags=["HOSPITAL"])
app.include_router(patient_router, tags=["PATIENT"])
app.include_router(technician_router, tags=["TECHNICIAN"])

