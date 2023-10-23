# lambda is used when u onl wnna use a function once
# syntax----- lambda parameter:action on parameter


# my_list=[1,2,3]
#
# def only_odd(item):
#     return item%2!=0
#
# def accumulator(acc,item):
#     print(acc,item)
#     return acc+item
#
# print(list(map(lambda item:item*2, my_list)))


#excercise

#square
# my_list=[5,4,3]
# print(list(map(lambda item:item**2,my_list)))

#list sorting
a=[(0,2),(4,3),(9,9),(10,-1)]
a.sort(key=lambda x:x[1])
print(a)