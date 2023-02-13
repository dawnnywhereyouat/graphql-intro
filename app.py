import graphene
from mutation import CreateUser, UpdateUser
from query import Query
from type import User

class MyMutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    