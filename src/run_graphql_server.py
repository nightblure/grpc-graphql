import uvicorn
from ariadne.asgi import GraphQL
from fastapi import FastAPI

from api.graphql.endpoints import path_to_graphql_schema
from src.deps import create_users_repository, create_posts_repository

if __name__ == '__main__':
    app = FastAPI()

    for path, schema in path_to_graphql_schema.items():
        app.mount(path, GraphQL(schema, debug=True))

    repos = [create_users_repository(), create_posts_repository()]

    for repo in repos:
        repo.fill_data()

    uvicorn.run(app, host='0.0.0.0', port=8076)
