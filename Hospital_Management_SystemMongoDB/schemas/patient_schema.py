from pydantic import BaseModel
from typing import Optional


class PatientSchema(BaseModel):
    name: str
    address: str
    contact: str
    alternate_number: Optional[str]
    whatsapp_number: Optional[str]
    age: str
    gender: str
    birth_date: str
    section: str
    reference_by: str
    test_conducting_by: str
    test_hospital: str
    referred_hospital: str
    clinical_category: str
    clinical_sub_category: str
    test: str
    format: str
    exam_procedure: str


class PatientCreate(PatientSchema):
    pass


class PatientUpdate(BaseModel):
    name: str
    address: Optional[str] = None
    contact: Optional[str] = None
    alternate_number: Optional[str] = None
    whatsapp_number: Optional[str] = None
    age: Optional[str] = None
    gender: Optional[str] = None
    birth_date: Optional[str] = None
    section: Optional[str] = None
    reference_by: Optional[str] = None
    test_conducting_by: Optional[str] = None
    test_hospital: Optional[str] = None
    referred_hospital: Optional[str] = None
    clinical_category: Optional[str] = None
    clinical_sub_category: Optional[str] = None
    test: Optional[str] = None
    format: Optional[str] = None
    exam_procedure: Optional[str] = None


class PatientResponse(PatientSchema):
    pass

