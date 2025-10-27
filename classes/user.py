class User:
    

    def __init__(self, username: str, email: str, age: int):
        
        self.username = username
        self.email = email
        self.age = age
    
    def __str__():
        return f"Пользвоатель {self.username}  с адресом {self.email} возрастом {self.age} лет"

