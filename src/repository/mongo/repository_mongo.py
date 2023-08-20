from src.infra.Mongo.infra import MongoInfrastructure


class MongoRepository:

    infra = MongoInfrastructure.get_db_and_collection()
    @classmethod
    def insert_one(cls, insert):
        return cls.infra.insert_one(insert)

    @classmethod
    def delete_data(cls, delete):
        return cls.infra.delete_one(delete)

    @classmethod
    def get_one(cls, get_data):
        return cls.infra.find_one(get_data)

    @classmethod
    def get_all(cls, skip, limit):
        skip_limit = cls.infra.find({}, {"_id": False}).skip(skip).limit(limit)
        result_in_list = list(skip_limit)
        return result_in_list

    @classmethod
    def update_data(cls, old, update):
        update = {"$set": update}
        database_update = cls.infra.update_one(old, update)
        return database_update


