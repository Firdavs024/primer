# a = {'12':2121, 'privet': 'sss'}
# print(a.get('12'))

# def create_list():
#     my_list=[]
#     print(my_list)
#
# create_list()
#
# def my1():
#     x=['jordan','mayk']
#     if 'jordan' in x:
#         print(x)
# my1()
#
# def calc():
#      a= 1+2
#      return 'операция произошла успешно'
# test=calc()
# print(test)
#
# def spam2(a,b,c=7):
#     print(a+b+c)
# spam2(3,5,9) #c это необезательный параметр

# def calc(a,b):
#     s=a+b
#     return s
# print(calc(3,5))

# def spam1(*num):
#     return num
# print(spam1(1,2,3,'HJello'))
# def spam1(*num):
#     return num
# h=int(input('s'))
# e=int(input('s'))
# print(spam1(e,h))
#
def spam2(**set):
    return set
print(spam2(name='my1',age=23))

# def spam1(**kwargs):
#     for k,v in kwargs.items():
#         return k,v                    #return работает один раз
# print(spam1(name="my1", sas=21))

# a=int(input('число'))
# def ch(a):
#     ch=[i for i in a if i %2==0]
#     print('ch')
#     ne=[i for i in a if i %2!=0]
#     print('ne')
# print(ch(a))
#

# numbers = [int(i) for i in input('Введи числа: ').split()]
# numbers1 = [i for i in numbers if int(i) > 0]
# numbers2 = [i for i in numbers if int(i) < 0]
#
# print('Уникальные числа', set(numbers))
# print('Отсортированные числа', numbers.sort())
# print('Сумма положительных', sum(numbers1))
# print('Сумма отрицательных', sum(numbers2))
#
# ["Привет", "наши", "машина", "кресло", "наш", "папа", "дочка"]
# text = input('Введи слова: ').split()
# word_5 = [i for i in text if len(i) > 5]
# print(word_5)
#
# import requests
# response=requests.get('ссылка')
# print(response.text)