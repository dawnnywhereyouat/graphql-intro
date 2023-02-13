import graphene
from type import User
from data import users

class CreateUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        email = graphene.String()
        password = graphene.String()

    user = graphene.Field(lambda: User)

    def mutate(root, info, id, name, email, password):
        user = User(id, name, email, password)
        users.append({
            "id": id,
            "name": name,
            "email": email,
            "password": password
        })
        
        return CreateUser(user = user)

class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        email = graphene.String()
        password = graphene.String()

    user = graphene.Field(lambda: User)

    def mutate(root, info, id, name, email, password):
        user = User(id, name, email, password)
        old_user = list(filter(lambda user: user['id'] == id ))[0]

        users.remove(old_user)
        users.append({
            "id": id,
            "name": name,
            "email": email,
            "password": password
        })
        return UpdateUser(user = user)

class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    user = graphene.Field(lambda: User)

    def mutate(root, info, id):
        old_user = list(filter(lambda user: user['id'] == id ))[0]
        # user = User(id, name, email, password)

        users.remove(old_user)
        return UpdateUser(user = old_user)