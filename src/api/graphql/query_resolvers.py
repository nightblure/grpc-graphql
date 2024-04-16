from ariadne.types import GraphQLResolveInfo

from src.deps import create_users_repository


def get_users(obj, info: GraphQLResolveInfo):
    user_repository = create_users_repository()
    users = user_repository.get_all()
    return {'items': users}


def get_one_user(obj, info: GraphQLResolveInfo, **data):
    user_id = data['user_id']
    user_repository = create_users_repository()
    user = user_repository.get_by_id(user_id)
    return user
