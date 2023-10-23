# list and set comprehensions are the same except for the function they hold


# my_list=[char for char in 'shree']
# my_list2=[num for num in range(0,100)]
# my_list3=[num**2 for num in range (0,100)]
# my_list4=[num**2 for num in range(0,100) if num%2==0]
# print(my_list4)

# dictionary comprehensions are a bit different compared to set and list comprehensions
simple_dict={'a':1,'b':2}
my_dict={ key:value**2 for key,value in simple_dict.items()}
print(my_dict)