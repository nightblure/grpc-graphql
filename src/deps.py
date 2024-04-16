from src.db.repositories import UserRepository, PostsRepository


def create_posts_repository() -> PostsRepository:
    if PostsRepository.instance is None:
        PostsRepository.instance = PostsRepository()
    return PostsRepository.instance


def create_users_repository(posts_repository=create_posts_repository()) -> UserRepository:
    if UserRepository.instance is None:
        UserRepository.instance = UserRepository(posts_repository=posts_repository)
    return UserRepository.instance
