from pymongo import MongoClient
from bson import ObjectId
from MongoDB_Connection import get_technician
from models.technician_model import TechnicianModel
from domain.technician_domain import TechnicianDomain


class TechnicianRepository:
    def __init__(self):
        self.collection = get_technician()

    def create(self, technician: TechnicianDomain) -> TechnicianDomain:
        technician_model = TechnicianModel.from_domain(technician)
        result = self.collection.insert_one(technician_model.dict(by_alias=True, exclude={"id"}))
        technician_model.id = result.inserted_id
        return technician_model.to_domain()

    def list(self) -> list[TechnicianDomain]:
        technicians = self.collection.find()
        return [TechnicianModel(**technician).to_domain() for technician in technicians]

    def get(self, technician_id: str) -> TechnicianDomain:
        technician = self.collection.find_one({"_id": ObjectId(technician_id)})
        if technician:
            return TechnicianModel(**technician).to_domain()
        return None

    def update(self, technician_id: str, technician: TechnicianDomain) -> TechnicianDomain:
        technician_model = TechnicianModel.from_domain(technician)
        update_data = technician_model.dict(by_alias=True, exclude={"id"})
        self.collection.update_one({"_id": ObjectId(technician_id)}, {"$set": update_data})
        return self.get(technician_id)

    def delete(self, technician_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(technician_id)})
        return result.deleted_count > 0
