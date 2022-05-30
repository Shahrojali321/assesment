lst=[]
n=int(input("enter the length of list: "))
for i in range(0,n):
    element=input("Enter the element of a list: ")
    lst.append(element)
print(lst)
lst1=['a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for j in lst1:
    for i in lst:
        lst2=[]
        char=i[0]
        if(char==j):
            lst2.append(i)
    print(lst2)
