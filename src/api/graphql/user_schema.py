from ariadne import (
    make_executable_schema,
    load_schema_from_path,
    ObjectType,
    InputType
)

from api.graphql.custom_scalars import custom_scalars
from src.api.graphql.mutation_resolvers import create_user
from src.api.graphql.query_resolvers import get_one_user, get_users
from src.db.schemas import UserCreate


def create_user_schema(path: str = 'api/graphql/users_schema.graphql'):
    schema_definition = load_schema_from_path(path)

    mutations = ObjectType('UserMutation')  # must be same with type name in graphql schema definition
    mutations.set_field('create_user', create_user)

    queries = ObjectType('UserQuery')  # must be same with type name in graphql schema definition
    queries.set_field('users_all', get_users)
    queries.set_field('one_user', get_one_user)

    """
    Здесь удобно определять функции для парсинга данных, 
      в обработчики запросов теперь можно подставлять тайп-хинты схем (датаклассы или pydantic-модели)
      https://ariadnegraphql.org/docs/inputs
    """
    graphql_schemas = [
        # InputType('UserCreateInput', lambda data: UserCreate.convert_str_date(data))
        InputType('UserCreateInput', lambda data: UserCreate(**data))
    ]

    bindables = [queries, mutations]

    bindables.extend(graphql_schemas)
    bindables.extend(custom_scalars)

    schema = make_executable_schema(schema_definition, bindables)  # , convert_names_case=True)
    return schema
