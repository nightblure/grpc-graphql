from api.graphql.client import run

"""
Query examples for Postman:

localhost:8076/users

query Users_all {
    users_all {
        items {
            username
            email
            phone_number
            birth_date
        }
    }
}

query one_user {
    one_user(user_id: 15) {
        id
        username
        email
        phone_number
        birth_date
    }
}

mutation create_user {
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

if __name__ == "__main__":
    run()
