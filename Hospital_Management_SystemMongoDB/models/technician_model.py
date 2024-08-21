from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from bson import ObjectId
from domain.technician_domain import TechnicianDomain


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema):
        field_schema.update(type="string")


class TechnicianModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    user_name: str
    name: str
    hospital_name: str
    address: str
    contact_number: str
    alternate_number: str
    whatsApp_number: str
    emailID: EmailStr
    education: str
    dob: str
    gender: str
    description: str

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

    @classmethod
    def from_domain(cls, technician_domain: 'TechnicianDomain'):
        return cls(
            id=technician_domain.id,
            user_name=technician_domain.user_name,
            name=technician_domain.name,
            hospital_name=technician_domain.hospital_name,
            address=technician_domain.address,
            contact_number=technician_domain.contact_number,
            alternate_number=technician_domain.alternate_number,
            whatsApp_number=technician_domain.whatsApp_number,
            emailID=technician_domain.emailID,
            education=technician_domain.education,
            dob=technician_domain.dob,
            gender=technician_domain.gender,
            description=technician_domain.description
        )

    def to_domain(self) -> TechnicianDomain:
        return TechnicianDomain(
            id=str(self.id) if self.id else None,
            user_name=self.user_name,
            name=self.name,
            hospital_name=self.hospital_name,
            address=self.address,
            contact_number=self.contact_number,
            alternate_number=self.alternate_number,
            whatsApp_number=self.whatsApp_number,
            emailID=self.emailID,
            education=self.education,
            dob=self.dob,
            gender=self.gender,
            description=self.description
        )
