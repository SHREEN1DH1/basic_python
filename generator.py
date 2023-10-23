def generator_func(num):
    for i in range(num):
        yield i * 2  # yield stops the process when next keyword is used


g = generator_func(1000)
next(g)
next(g)
print(next(g))