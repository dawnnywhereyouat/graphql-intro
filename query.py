from graphene import ObjectType
from data import users

class Query(ObjectType):
    def get_user(root, info, id):
        return list(filter(lambda user: user['id'] == id ))[0]

    def get_users(root, info):
        return users