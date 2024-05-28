# word='  hello   '
# print(word.strip())

# x= {'name':'pasha', 'job':'tgbot creator'}
# print(x['job'])

# data={'name':['jordan','pavel'],'age':(12,21),'job':'programmers'}
# print(data ['name'][0], data['job'][-1])

data={'name':['jordan','pavel'],'age':(12,21),'job':'programmers'}
print(data ['name'],data ['age'], data['job'][-1])

# x=input('vvod')
# y={'name':x,'course':'pyton'}
# print(y['name'])

# istructor={'name':'jordan', 'age':21,'job':'programmer'}
# if 21 in istructor.values():
#     print('да есть')
# else:
#     print('ошибка')

# users={}
# users['name'], users['age']='jordan',21 #добавить в словарь
# # users={}
# # users.update(job='junior',email='jordan.com')
# print(users)

# caffes={'evos':{'gorod':'tashkent','filialov':'mnogo','otkritie':2007}}
# caffes['evos']['лухня']='fast food'
# print(caffes)

# my_dict={'name':'jordan'}
# my_dict.clear()
# print(my_dict)

# my=dict(name='jordan', job='develoe')
# my2=my.get('name')    #''''my.copy()''''
# print(my2)

# nums={1,2,3,3,4,4,5}
# print(nums)
#
# nums2=set({'hello','hello','myname',2,2,0})
# print(nums2)
# list1=['jordan','pavel','jordan','jordan','sasha']
# counter=0
# for i in list1:
#     if i == 'jordan':
#         counter+=1
#     else:
#         print('')
# print(counter)

# my=['2','33','33',2,'tgbot']
# my2=set(my)
# print(my2)

# instr=dict(name='jordan', age=21, job='python developer')
# for v in instr.keys():
#     print(v)
# instr = dict(name='jordan', age=21, job='python developer')
# for v in instr.values():
#     print(v)

# instr=dict(name='jordan', age=21, job='python developer')
# for k,v in instr.items():
#     print(k,v)

# instr=dict(name='jordan', age=21, job='python developer')
# for k,v in instr.items():
#     print(f'{k}: {v}')

# game_properties=['current_score', 'high_score','number_of_lives','power_ups','ammo','skills']
# s=int(input('fd'))
# new_player={}.fromkeys(game_properties,s)
# print(new_player)

# all_products={'весь склад':{'картошка':20,'помидор':30,'лук':25}}
# korzina={}
# while True:
#     choice = input('Хотите добавить или посмотреть весь список?')
#     if choice.lower()== 'добавить':
#         products=input('продукт:')
#         count=int(input('кол-во'))
#         all_products['весь склад'][products]=count
#     elif choice.lower()=='продукт':
#         print(all_products)
#         c = input('что нибудь добваить в корзину?')
#         f=input('количество')
#         korzina[c]=f
#         print(korzina)
#         # if c=='картошка':
#         #     korzina.update(картошка=f)
#         #     print(korzina)
#         # elif c == 'помидор':
#         #     korzina.update(помидор=f)
#         #     print(korzina)
#         # elif c == 'лук':
#         #     korzina.update(лук=f)
#         #     print(korzina)
#         g=input('Закончить покупку?')
#         if g=='yes':
#             break
#         elif g == 'заменить':
#             korzina.clear()
#             l=input('Какой товар выберите?')
#             k=input('кол-во')
#             korzina[l]=k
#             print(korzina   )
#             # if l == 'помидор':
#             #     korzina.update(l=k)
#             #     print(korzina)
#             # if l == 'лук':
#             #     korzina.update(лук=k)
#             #     print(korzina)
#         z=input('закончить покупку?')
#         if z=='yes':
#             break
#         elif z=='стереть':
#             korzina.clear()
#             print(korzina)
#             break




