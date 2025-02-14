from sqlmodel import Session, select
from app.models import User, CreateUser




class UserFactory:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[User | None]:
        return self.session.exec(select(User)).all()

    def get_by_id(self, id: int) -> User | None:
        return self.session.exec(select(User).where(User.id == id)).one_or_none()

    def create(self, user_data: CreateUser) -> User:
        user_data = user_data.model_dump(exclude_unset=True)
        user = User(**user_data)
        print(user)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
    
    def update_by_id(self, id: int, user_data: CreateUser) -> User:
        existing_user = self.session.exec(select(User).where(User.id == id)).one_or_none()
        if existing_user is None:
            return None
        user_data = user_data.model_dump(exclude_unset=True)
        for key, value in user_data.items():
            setattr(existing_user, key, value)
        self.session.add(existing_user)
        self.session.commit()
        self.session.refresh(existing_user)
        return existing_user