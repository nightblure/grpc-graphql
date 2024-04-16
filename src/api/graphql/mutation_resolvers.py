from db.schemas import UserCreate
from deps import create_users_repository


# arg names must be same with UserMutation (see users_schema.graphql)
def create_user(_, info, user_data: UserCreate):
    user_repository = create_users_repository()
    id = user_repository.insert(user_data.to_dict())
    return user_repository.get_by_id(id)
