import requests


def run():
    query = """
        mutation Create_user {
    create_user(
        user_data: {
            username: "test"
            email: "test@gmail.com"
            phone_number: "3453462"
            birth_date: "2022-04-30 00:00:00"
        }
    ) {
        id
        username
        email
        phone_number
        birth_date
        posts {
            user_id
            text
        }
    }
}
    """

    body = {
        'operationName': 'Create_user',
        'query': query
    }
    response = requests.post('http://localhost:8076/users', json=body)
    print(response.json())
