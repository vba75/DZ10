import logging
from classes.user import User
from classes.usermanager import UserManager

logging.basicConfig(filename='app.log', level=logging.ERROR ) #, encoding='utf-8')

#    def __init__(self, username:  str, email: str, age: int):

mng = UserManager()

one = User('vladimir', 'vreboot@yandex.ru', 50)
two = User('vladimir', 'vreboot@yandex.ru', 50)
three = User('Svetlana', 'vreboot@yandex.ru', 50)
four = User('Anastasiya', 'vvreboot@yandex.ru', 30)

mng.add_user(one)
mng.add_user(four)



#################33
# Следующий метод вызывает исключение , имя пользователя не уникально
#
mng.add_user(two)  


mng.remove_user(four.username)

#################33
# Следующий метод вызывает исключение , Петра не добавляли
#
mng.remove_user('Petr')




existing_user = mng.find_user('Vladimir')


#################33
# Следующий метод вызывает исключение , Петра не добавляли
#
not_existing_user = mng.find_user('Petr')
