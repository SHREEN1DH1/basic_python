# def my_decorator(func):
#     def wrap_func():
#         print('virat')
#         func()
#         print('shree')
#     return wrap_func
#
# @my_decorator  #using @ indicates a decorator
# def hello():
#     print("hey , how are you")

# hello()   #by using decorators, hello func is super boosted and used in the decorator func created above

# decorators are like wrappers the above decorator process can be achieved using
# my_decorator(hello) #this is the same as using the decorator above

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('virat')
        func(*args, **kwargs)
        print('shree')
    return wrap_func

@my_decorator
def hello(greeting,emoji=":)"):
    print(greeting,emoji)

hello("hiiiii")
