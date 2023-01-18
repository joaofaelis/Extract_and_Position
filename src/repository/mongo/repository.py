from src.infra.Mongo.infra import MongoInfra


class conection:

    infra = MongoInfra
    db_name = "Excel"
    collection = "Excel"

    @classmethod
    def get_collection(cls):
        client = cls.infra.get_client()
        database = client[cls.db_name]
        collect = database[cls.collection]
        return collect

    @classmethod
    def insert_one(cls, create):
        collection = cls.get_collection()
        return collection.insert_one(create)

    @classmethod
    def get_all_coletor(cls, skip, limit):
        collection = cls.get_collection()
        coletor_skip = collection.find({}, {"_id": False}).skip(skip).limit(limit)
        resultado = list(coletor_skip)
        return resultado

    @classmethod
    def get_coletor(cls, coletor_dados):
        collection = cls.get_collection()
        return collection.find_one(coletor_dados)

    @classmethod
    def update(cls, old, atualizar):
        collection = cls.get_collection()
        new = {"$set": atualizar}
        coletor_data = collection.update_one(old, new)
        return coletor_data

    @classmethod
    def delete_coletor(cls, deletar):
        collection = cls.get_collection()
        print(deletar)
        delete_onee = collection.delete_one(deletar)
        return delete_onee
