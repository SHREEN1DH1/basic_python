import re
# pattern=re.compile(r"^\S+@\S+\.\S+$")
# string='shree@gmail.com'
# a=pattern.search(string)
# # b=pattern.findall(string)
# c=pattern.fullmatch(string)
# d=pattern.match(string)
# print(a)


#password validation

pattern=re.compile(r"[A-Za-z0-9@#$%]{8,}")
string=input("enter a password which contains alphabets , numbers and only @#$% symbols and atleast 8 char long ")
a=pattern.fullmatch(string)
print(a)