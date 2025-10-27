
class UserAlreadyExistsError(Exception):
    def __init__(self, username: str):
        self.message  = "Пользователь с таким именем пользователя уже зарегистрирован, выберите другое"
        self.username= username
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} {self.username}"


######


class UserNotFoundError(Exception):
    def __init__(self, username ):
        self.message = "Пользователь с таким именем пользователя не найден"
        self.username = username
        super().__init__(self.message)

    def __str__(self):
#        return f"{self.message}: {self.username}"
        return f"Пользователь с таким именем пользователя не найден"
    

