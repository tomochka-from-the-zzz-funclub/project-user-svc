from datetime import date

class UserFilterQuery:
    def __init__(self,
                 email: str | None = None,
                 password: str | None = None,
                 name: str | None = None,
                 surname: str | None = None,
                 birth: date | None = None,
                 subscription: bool | None = None
    ):
        self.email = email
        self.password = password
        self.name = name
        self.surname = surname
        self.birth = birth
        self.subscription = subscription


    def to_dict(self) -> dict:
        data = {
            "email": self.email,
            "password": self.password,
            "name": self.name,
            "surname": self.surname,
            "birth": self.birth,
            "subscription": self.subscription
        }
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data