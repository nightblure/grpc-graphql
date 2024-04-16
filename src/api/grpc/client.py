import grpc
from google.protobuf.json_format import MessageToDict

from src.api.grpc.users_pb2 import UsersRequest
from src.api.grpc.users_pb2_grpc import UsersStub
from src.db.schemas import UsersResponse


class GrpcClient:
    def __init__(self, *, url: str):
        channel = grpc.insecure_channel(url)
        self.client = UsersStub(channel)

    def get_users(self, request: UsersRequest) -> UsersResponse:
        response_dict = MessageToDict(self.client.GetAll(request))
        users = UsersResponse(**response_dict)
        return users


"""
Here ok that we have the python error "Cannot find reference UsersRequest". 
Its python grpc issues, but it works
"""


def run():
    client = GrpcClient(url='localhost:50051')
    request = UsersRequest()
    users = client.get_users(request)
    print(users.items[0])
