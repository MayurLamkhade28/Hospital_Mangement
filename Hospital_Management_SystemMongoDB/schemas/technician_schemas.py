from pydantic import BaseModel
from typing import Optional


class TechnicianBase(BaseModel):
    id: Optional[str]  # Changed to str to match MongoDB's ObjectId
    user_name: str
    name: str
    hospital_name: str
    address: str
    contact_number: str
    alternate_number: str
    whatsApp_number: str
    emailID: str
    education: str
    dob: str
    gender: str
    description: str


class CreateTechnician(TechnicianBase):
    pass


class UpdateTechnician(BaseModel):
    id: Optional[str]
    user_name: Optional[str] = None
    name: Optional[str] = None
    hospital_name: Optional[str] = None
    address: Optional[str] = None
    contact_number: Optional[str] = None
    alternate_number: Optional[str] = None
    whatsApp_number: Optional[str] = None
    emailID: Optional[str] = None
    education: Optional[str] = None
    dob: Optional[str] = None
    gender: Optional[str] = None
    description: Optional[str] = None


class ResponseTechnician(TechnicianBase):
    id: str
