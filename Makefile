install-deps:
	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt

GRPC_DIR=src/api/grpc
PROTOBUF_DIR=${GRPC_DIR}/protobuf

gen-proto:
	python3 -m grpc_tools.protoc -I ${PROTOBUF_DIR} \
 		--python_out=${GRPC_DIR} \
 		--grpc_python_out=${GRPC_DIR} \
 		${PROTOBUF_DIR}/users.proto