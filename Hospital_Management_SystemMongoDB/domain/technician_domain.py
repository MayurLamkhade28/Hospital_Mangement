from dataclasses import dataclass
from typing import Optional


@dataclass
class TechnicianDomain:
    id: Optional[str]
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

    def to_dict(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'name': self.name,
            'hospital_name': self.hospital_name,
            'address': self.address,
            'contact_number': self.contact_number,
            'alternate_number': self.alternate_number,
            'whatsApp_number': self.whatsApp_number,
            'emailID': self.emailID,
            'education': self.education,
            'dob': self.dob,
            'gender': self.gender,
            'description': self.description
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get(id),
            user_name=data['user_name'],
            name=data['name'],
            hospital_name=data['hospital_name'],
            address=data['address'],
            contact_number=data['contact_number'],
            alternate_number=data['alternate_number'],
            whatsApp_number=data['whatsApp_number'],
            emailID=data['emailID'],
            education=data['education'],
            dob=data['dob'],
            gender=data['gender'],
            description=data['description']
        )
