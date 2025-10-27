from classes.user import User
from classes.exeptions import UserAlreadyExistsError, UserNotFoundError


class UserManager:
    
    users = {}
   
    
    def __init__(self):
        pass

    def add_user(self, user: User):
        if self.users.get(user.username, 0) != 0:
            raise UserAlreadyExistsError(user.username) 
        
        self.users[user.username] = user

    
    def remove_user(self, username: str):
        if self.users.get(username, 0) == 0:
            raise UserNotFoundError(username) 
        else:
            del self.users[username]



    def find_user(self, username: str)->User:
        if self.users.get(username, 0) == 0:
            raise UserNotFoundError(username) 
        else:
            return self.users.get(username)

