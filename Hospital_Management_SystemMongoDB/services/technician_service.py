from typing import List
from schemas.technician_schemas import CreateTechnician, UpdateTechnician, ResponseTechnician
from repository.technician_repo import TechnicianRepository
from domain.technician_domain import TechnicianDomain


def get_technician_service():
    return TechnicianService(TechnicianRepository())


class TechnicianService:
    def __init__(self, repository: TechnicianRepository):
        self.repository = repository

    def create_technician(self, technician: CreateTechnician) -> ResponseTechnician:
        technician_domain = TechnicianDomain(id=None, **technician.dict())
        created_technician = self.repository.create(technician_domain)
        return ResponseTechnician(**created_technician.to_dict())

    def list_technician(self) -> List[ResponseTechnician]:
        technicians = self.repository.list()
        return [ResponseTechnician(**technician.to_dict()) for technician in technicians]
