# class Car:
#     def __init__(self,model,color,year):
#         self.model=model
#         self.color=color
#         self.year=year
#     def change_color(self,new_color):
#           self.color=new_color
#
# gentra=Car('ravon','black',2022)
# gentra.change_color('White')
# print(gentra.color)

# class Comment:
#     def __init__(self,user,text,likes=0):
#         self.user=user
#         self.text=text
#         self.likes=likes
#
# users=Comment('Dima','Хорошое видео',)
# print(users.likes,users.user,users.text)
# print(vars(users))

# class BankAccaunt:
#     def __init__(self,username,balans):
#         self.username=username
#         self.balans=balans
#     def cash(self,new_cash):
#         self.balans=new_cash
#     def cash_new(self,dop):
#         self.cash=dop


# deposit=BankAccaunt('Misha',0)
# print(vars(deposit))
# cash_new= input('Сколько добавить')
# deposit=BankAccaunt('Misha',cash_new)
# print(vars(deposit))
# cash_new=input('отнять')
# f=[int(i)-cash_new for i in deposit]
# print(vars(deposit))

class BankAccaunt:
    def __init__(self,name,balans=0):
        self.name=name
        self.balans=balans
    def deposit(self,amount):
        self.balans += amount
    def cash(self,amount):
        if self.balans >= amount:
            self.balans -= amount
            print('Деньг')
        else:
            print('')
    def my_balans(self):
        print(f'деньги на балансе:{self.balans}')
#     # def __repr__(self):     -----------
#     #     return f'Это какой то объект {vars(self)}'   -----------
user1=BankAccaunt('Misha')
# # print(user1)   ------------
while True:
    menu=input('Действие:\n'
               '1\n'
               '2\n'
               '3\n'
               'Действие:')
    if menu =='1':
        user1.my_balans()
    elif menu == '2':
        amount = float(input('summa'))
        user1.deposit(amount)
    elif menu == '3':
        amount=float(input('snyat'))
        user1.cash(amount)
    else:
        print('Error')

class User:
    def __init__(self,name,mail,nomber,age=18):
        self.name=name
        self.mail=mail
        self.age=age
        self.nomber=nomber
    def change_name(self,new_name):
        self.name=new_name
    def change_mail(self,new_mail):
        self.mail=new_mail
    def change_nomber(self,new_nomber):
        self.nomber=new_nomber
user1=User('Misha','tex4.com','12345')
while True:
    f=input('Что делать 1-изменить имя\n'
            '2-измнить почту\n'
            '3-изменить номер')
    if f == '1':
        new_name=input('новое имя')
        user1.change_name(new_name)
        print(vars(user1))