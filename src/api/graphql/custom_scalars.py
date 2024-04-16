from datetime import datetime

from ariadne import ScalarType

datetime_scalar = ScalarType('DateTime')


# https://ariadnegraphql.org/docs/scalars
@datetime_scalar.serializer
def serialize_datetime(value: str):
    return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')


custom_scalars = [
    datetime_scalar,
    # ... more scalars
]
