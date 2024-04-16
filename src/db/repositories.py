from datetime import datetime
from random import randint

from faker import Faker

from src.api.grpc.users_pb2 import UserRead as UserReadGrpc
from src.db.db import UsersCollection, SomePostsCollection, BaseCollection
from src.db.schemas import UserCreate, UserRead, PostCreate, PostRead


class BaseRepository:
    read_schema = None

    def __init__(self):
        self.collection = BaseCollection()

    def insert(self, item: dict) -> int:
        return self.collection.insert(item)

    def bulk_insert(self, items):
        for item in items:
            self.insert(item)

    def get_all(self):
        db_items = self.collection.get_all()
        return [self.read_schema(**item) for item in db_items]

    def get_by_id(self, id: int):
        user = self.collection.one_or_none(id)

        if user is not None:
            user = UserRead(**user)

        return user

    def fill_data(self, items_count: int):
        raise NotImplementedError()


class PostsRepository(BaseRepository):
    instance: 'PostsRepository' = None
    read_schema = PostRead

    def __init__(self):
        super().__init__()
        self.collection = SomePostsCollection()

    def fill_data(self, items_count: int = 1000):
        faker = Faker('en')

        posts = [
            PostCreate(user_id=randint(1, 20), text=faker.paragraph(nb_sentences=5)).to_dict()
            for _ in range(items_count)
        ]

        self.bulk_insert(posts)


class UserRepository(BaseRepository):
    instance: 'UserRepository' = None
    read_schema = UserRead

    def __init__(self, *, posts_repository: PostsRepository):
        super().__init__()
        self.posts_repository = posts_repository
        self.collection = UsersCollection()

    def fill_data(self, items_count: int = 20):
        faker = Faker('en')

        users = [
            UserCreate(
                username=faker.name(),
                email=faker.email(),
                phone_number=faker.phone_number(),
                birth_date=datetime.now()
            ).to_dict()
            for _ in range(items_count)
        ]

        self.bulk_insert(users)

    def fill_data_grpc(self, items_count: int = 20):
        faker = Faker('en')

        users = [
            UserReadGrpc(
                id=i,
                username=faker.name(),
                email=faker.email(),
                phone_number=faker.phone_number(),
                birth_date=int(datetime.now().timestamp())
            )
            for i in range(items_count)
        ]

        self.bulk_insert(users)

    def get_all(self):
        posts = self.posts_repository.get_all()
        user_id_to_posts = {}

        for post in posts:
            if post.user_id not in user_id_to_posts:
                user_id_to_posts[post.user_id] = []

            user_id_to_posts[post.user_id].append(post)

        users = self.collection.get_all()
        users_with_posts = users

        for u in users_with_posts:
            user_id = u['id']
            posts = user_id_to_posts[user_id]
            u['posts'] = posts

        return users_with_posts

    def get_all_grpc(self):
        users = self.collection.get_all_grpc()
        return users