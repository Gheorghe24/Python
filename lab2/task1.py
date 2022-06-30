def sum(list):
    for i in list1:
        print(i)

n=int(input("Enter a number"))
c = 0
list1 = []
while n:
    list1.append(n%10)
    c+=1
    n=n//10
list1.reverse()

sum(list1)
