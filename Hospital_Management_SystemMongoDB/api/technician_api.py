from fastapi import APIRouter, Depends
from schemas.technician_schemas import ResponseTechnician, CreateTechnician
from services.technician_service import TechnicianService, get_technician_service

router = APIRouter()


@router.post("/technician", response_model=ResponseTechnician)
def create_technician(technician: CreateTechnician, service: TechnicianService = Depends(get_technician_service)):

    return service.create_technician(technician)


@router.get("/technician", response_model=list[ResponseTechnician])
def list_technician(service: TechnicianService = Depends(get_technician_service)):
    return service.list_technician()
