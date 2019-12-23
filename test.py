# # l1 = [1,2,3,['Eason','GAI']]
# # l2 = l1
# # l2[0] = 'Eason'
# # l2[3][0]='GAI'
# #
# # print(l1)
# # print(id(11)==id(l2))
#
# l1 = [1, 2, 3, ['aa', 'bb']]
# l2 = l1
# l2[0]='aaa'
# l2[3][0]='bbb'
# print(l1)  #['aaa', 2, 3, ['bbb', 'bb']]
# print(id(l1)==id(l2))  #True


import copy


# l2 = l1
# print(id(l1),id(l2))
# l2 = copy.copy(l1)  # 拷贝一份 .......  浅拷贝
# print(id(l1),id(l2))
# l1[0] = 222  #修改了l1的值
# print(l1,l2)

# import copy
# l1[2].append(666)
# print(l1,l2)
# l2 = copy.deepcopy(l1)
# l1[2].append(666)
# print(l1,l2)
# print(id(l1))
# print(id(l2))


import copy
l1 = [1,2,[1,2]]
l2=l1
l1[2].append(666)
print(l1,l2)
l2 = copy.deepcopy(l1)
l1[2].append(666)
print(l1,l2)
print(id(l1))
print(id(l2))
