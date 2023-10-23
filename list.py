def lists():
    n=int(input("Enter the number of students"))
    print("Enter the srn of those students")
    list1=[]
    list2=[]
    k=0
    for i in range(n):
        value=input()
        list1.append(value)
    m=int(input("Enter the number of extra students"))
    print("Enter the srn of extra students")
    for i in range(m):
        value=input()
        list2.append(value)
    list1.extend(list2)
    key=int(input("Enter the srn to be searched"))
    for i in range(len(list1)):
        if(key == list1[i]):
            print("srn found")
        else:
            print("Srn not found")
            break
lists()



