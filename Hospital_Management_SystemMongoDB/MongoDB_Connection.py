from pymongo import MongoClient


class Db_Connect:
    def __init__(self, uri: str, db: str):
        self.client = MongoClient(uri)
        self.db = self.client[db]

    def get_collection(self, collection: str):
        return self.db[collection]


db_con = Db_Connect(uri="mongodb://localhost:27017/", db="H_ProjectDB")


def get_hospital():
    return db_con.get_collection("Hospital")


def get_patient():
    return db_con.get_collection('Patients')


def get_technician():
    return db_con.get_collection('Technician')
