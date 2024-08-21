from dataclasses import dataclass
from typing import Optional


@dataclass
class PatientDomain:
    id: Optional[str]
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

    def to_dict(self):
        return {
            'patientId': self.id,
            'name': self.name,
            'address': self.address,
            'contact': self.contact,
            'alternate_number': self.alternate_number,
            'whatsapp_number': self.whatsapp_number,
            'age': self.age,
            'gender': self.gender,
            'birth_date': self.birth_date,
            'section': self.section,
            'reference_by': self.reference_by,
            'test_conducting_by': self.test_conducting_by,
            'test_hospital': self.test_hospital,
            'referred_hospital': self.referred_hospital,
            'clinical_category': self.clinical_category,
            'clinical_sub_category': self.clinical_sub_category,
            'test': self.test,
            'format': self.format,
            'exam_procedure': self.exam_procedure

        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get(id),
            name=data['name'],
            address=data['address'],
            contact=data['contact'],
            alternate_number=data['alternate_number'],
            whatsapp_number=data['whatsapp_number'],
            age=data['age'],
            gender=data['gender'],
            birth_date=data['birth_date'],
            section=data['section'],
            reference_by=data['reference_by'],
            test_conducting_by=data['test_conducting_by'],
            test_hospital=data['test_hospital'],
            referred_hospital=data['referred_hospital'],
            clinical_category=data['clinical_category'],
            clinical_sub_category=data['clinical_sub_category'],
            test=data['test'],
            format=data['format'],
            exam_procedure=data['exam_procedure']
        )
