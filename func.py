# parameters
# def say_hello(name,age):
#     print('hello',name)
# # arguments
# say_hello('shree',18)

# def sum(num1,num2):
#     return num1+num2
# print(sum(10,5))

# *ARGS,**KWARGS
# def duper_func(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# print(duper_func(1,2,3,4,5,num1=1,num2=2,name='shree'))

# RULE:--- parameters,args,default parameter,kwargs

# excercise- print highest even number in a given list
def highest_even(li):
    even=[]
    for i in li:
        if i%2==0:
            even.append(i)
    print(max(even))

highest_even([28,4,6,8,10,12])