# class PlayerCharacter:
#     def __init__(self,name,age):    #player character is a class player1 and 2 are objects
#         self.name=name         #init is a function or method kinda thing, used everytime in a class
#         self.age=age
#     def run(self):
#         print('run')
#         return 'done'
#
# player1=PlayerCharacter('shree',18)
# player2=PlayerCharacter('nidhi',20)
#
# print(player1.name)
# print(player2.age)
# print(player1.run())


# class cat:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
# cat1=cat('tom',10)
# cat2=cat('max',6)
# cat3=cat('john',15)
#
# def oldst_cat():
#     cats=[cat1.age,cat2.age,cat3.age]
#     cats.sort()
#     print(f"the oldest cat is {cats[-1]} years old")
# oldst_cat()

##INHERITANCE

class football():
    def position(self):
        print("attacker")

class country(football):
    def __init__(self,name,pos):
        self.name=name
        self.pos=pos
    def func(self):
        print(f'the player {self.name} plays at the position {self.pos}')

class club(football):
    pass

country1=country('shreee','midfield')
country1.func()


