## gRPC and GraphQL examples

---

### How to run gRPC example
1. Generate server and client protos by command 
```bash
make gen-proto
```

2. Run `run_grpc_server.py` and `run_grpc_client.py`

*If import error appear, fix import in file `users_pb2.py`: replace `import users_pb2 as users__pb2` with `from . import users_pb2 as users__pb2`

---

### How to run GraphQL example
1. Run `run_graphql_server.py` and `run_graphql_client.py`

---

### Links
* [RealPython: python-microservices-grpc](https://realpython.com/python-microservices-grpc/)
* [Ariadne](https://ariadnegraphql.org/docs/intro.html)