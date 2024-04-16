from concurrent.futures import ThreadPoolExecutor

import grpc

from src.api.grpc.users_pb2_grpc import UsersServicer, add_UsersServicer_to_server
from src.api.grpc.users_pb2 import UsersResponse
from deps import create_users_repository
from src.db.repositories import UserRepository


class UsersService(UsersServicer):
    def __init__(self, repository: UserRepository = create_users_repository()):
        self.repository = repository

    def GetAll(self, request, context):
        # if request.category not in books_by_category:
        #     context.abort(grpc.StatusCode.NOT_FOUND, "Category not found")

        users = [u for u in self.repository.get_all_grpc()]
        return UsersResponse(items=users)


def register_services(server: grpc.Server):
    users_service = UsersService()
    add_UsersServicer_to_server(users_service, server)


def start_server(*, port: int):
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    register_services(server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()


def run():
    user_repository = create_users_repository()
    user_repository.fill_data_grpc(100)
    start_server(port=50051)
