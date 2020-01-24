# list
print([1,3,True,6.5])
[1, 3, True, 6.5]
myList = [1,3,True,6.5]
print(myList)
[1, 3, True, 6.5]
myList = [0] * 6
print(myList)
[0, 0, 0, 0, 0, 0]
myList = [1,2,3,4]
A = [myList]*3
print(A)
myList[2]=45
print(A)
myList = [1024, 3, True, 6.5]
myList.append(False)
print(myList)
myList.insert(2,4.5)
print(myList)
print(myList.pop())
print(myList)
print(myList.pop(1))
print(myList)
myList.pop(2)
print(myList)
myList.sort()
print(myList)
myList.reverse()
print(myList)
print(myList.count(6.5))
print(myList.index(4.5))
myList.remove(6.5)
print(myList)
del myList[0]
print(myList)

print((54).__add__(21))


print(range(10))
range(0, 10)
print(list(range(10)))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(range(5,10))
range(5, 10)
print(list(range(5,10)))
[5, 6, 7, 8, 9]
print(list(range(5,10,2)))
[5, 7, 9]
print(list(range(10,1,-1)))
[10, 9, 8, 7, 6, 5, 4, 3, 2]

# string
print("David")
'David'
myName = "David"
print(myName[3])
'i'
print(myName*2)
'DavidDavid'
print(len(myName))
5
