#dunder methods-can be modified ie., the function of it can be changed as done below for__str__

# class Toy():
#     def __init__(self,color,age):
#         self.color=color
#         self.age=age
#     def __str__(self):
#         return f'{self.color}'
#
# action_figure=Toy('red',0)
# print(action_figure.__str__())


# by inheriting list in the base class we can use the object name superlist1 evn as a list variable


# class SuperList(list):
#     def __len__(self):
#         return 1000
#
# superlist1 = SuperList()
# print(len(superlist1))
# superlist1.append(5)
# print(superlist1[0])


