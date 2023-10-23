random=['a','b','c','b','d','m','n','n']

duplicates=[item for item in random if random.count(item)>1]
set=set(duplicates)
print("the duplicate values are",set)