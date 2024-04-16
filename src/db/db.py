class BaseCollection:
    def __init__(self):
        self.collection: dict[int, dict] = {}

    @property
    def next_id(self):
        if len(self.collection) == 0:
            return 1
        return max(self.collection.keys()) + 1

    def insert(self, item: dict) -> int:
        id = self.next_id
        self.collection[id] = item
        return id

    def get_all(self) -> list[dict]:
        return list(self.collection.values())

    def one_or_none(self, id: int) -> dict | None:
        return self.collection.get(id)


class UsersCollection(BaseCollection):
    def get_all(self) -> list[dict]:
        users = []

        for id, u in self.collection.items():
            u['id'] = id
            users.append(u)

        return users

    def get_all_grpc(self) -> list[dict]:
        return list(self.collection.values())

    def one_or_none(self, id: int) -> dict | None:
        user = self.collection.get(id)

        if user is not None:
            user['id'] = id

        return user


class SomePostsCollection(BaseCollection):
    pass
