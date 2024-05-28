# name=('pasha')
# n=[a for a in name]
# print(n)
# nums =[i for i in range(100)]
# print(nums)

# my_list=[1, 'a', 2, 4.5]
# my=[i+2 for i in my_list]
# print(my)                     #ОШИБКА
# my=[]
# for i in my_list:
#     my.append(i+2)
# # отличие в том что в новом варианте действие происходит разом а не по очереди с каждым элементом
#     print(my)

# w=[range(1,11)]
nums=[i for i in range(1,11)]
ch=[num for num in nums if num %2==0] # "%" остаток от деления
ne=[num for num in nums if num %2!=0]
print(ch,ne)

# names=['Pavel','Sasha','Jordan','Pasha']
# answer=[i[0]for i in names]
# print(answer)
#
# nums=[i for i in range(1,21)]
# nums2=[num for num in nums if num %2==0]
# print(nums, nums2)

# names=[]
# while True:
#     s=input('введите имя')
#     if s.lower() in [i.lower() for i in names]:
#         print('Такой юзер имеется')
#     elif s.lower() not in [i.lower() for i in names]:
#         names.append(s)
#         print(f'{'юзер успешно добавлен'}', names)
# else:
#     print('ошибка')

