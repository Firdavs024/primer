# def x(values):
#     values[0]=1
# v=[1,2,3,4]
# x(v)
# print(v)

# users=[]
# users.append([name,age])
# class Noname:
#     def __init__(self,word):
#         return f'Слово:{word}'
# c=Noname
# print(c)

# class car:
#     def __init__(self,model,color):
#         self.model=model
#         self.color=color
#
# class traktor(car):
#     pass

# class parants:
#     def __init__(self,name,gender):
#         self.name=name
#         self.gender=gender
#     def hello(self):
#         print('hello')
# class son(parants):
#     def __init__(self,age):
#         self.age=age
#
# mom=parants(name='ann', gender='female')
# son1=son(age='20')
# mom.hello()
# son1.hello()

# class Car:
#     def __init__(self,model,color,year):
#         self.model=model
#         self.color=color
#         self.year=year
# class supercar(Car):
#     def __init__(self,model,color,year,sponsor):
#         super().__init__(model,color,year)
#         self.sponsor=sponsor

# class parants1:
#     def __init__(self,name,gender):
#         self.name=name
#         self.gender=gender
#     def bye(self):
#         print('bye')
# class parants:
#     def __init__(self,name,gender):
#         self.name=name
#         self.gender=gender
#     def hello(self):
#         print('hello')
# class son(parants1,parants):
#     pass
# son(name='o',gender='man')
# print(son)

class myclass:
    @classmethod
    def class_info(cls):
        print(f'название этого каласса {cls.__name__}')

myclass.class_info()

# all_workers=[]
# class Worker:
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         all_workers.append([name,age,gender])
# class Meneger(Worker):
#     def __init__(self,look,name,age,gender):
#         super().__init__(name,age,gender)
#         self.look=look
#     def show(self,look):
#         if look==self.look:
#             print(all_workers)
# worker=Worker(name='oleg',age='20',gender='men')
# manager=Meneger(name='alisa',age='20',gender='women',look='21')
# manager.show(('21'))
