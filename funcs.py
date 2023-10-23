# map , filter , zip, reduce

# map

# def multiply_by2(item):
#     return item*2
#
# print(list(map(multiply_by2, [1,2,3])))

#FILTER

# my_list=[1,2,3]
# def only_odd(item):
#     return item%2!=0
#
# print(list(filter(only_odd, [1,2,3])))

# zip

# my_list=[1,2,3]
# your_list=[10,20,30]
# their_list=[5,6,7]
# print(list(zip(my_list, your_list,their_list)))

# reduce
# from functools import reduce
# my_list=[1,2,3]
# def accumulator(acc,item):
#     print(acc,item)
#     return acc+item
# print(reduce(accumulator, my_list,10)) # here 0 is acc value
print(__name__)