from graphene import ObjectType, Int, String

class User(ObjectType):
    id = Int()
    name = String()
    email = String()
    password = String()