myList = [1,2,3]

myList = ['String', 100, 23.1]

print(len(myList))

myList = ['one', 'two', 'three']

#Indexing and Slicing work the same for lists as strings
print(myList[0])

print(myList[1:])

#Concatenation
anotherList = ['four', 'five']

print(myList + anotherList)

print(myList, anotherList)

newList = myList + anotherList

print(newList)

#Lists are MUTABLE
newList[0] = 'ONE ALL CAPS'

print(newList)

#list methods
newList.append('six')

print(newList)

print(newList.pop()) #function returns popped item

print(newList)

poppedItem = newList.pop()

print(poppedItem)

print(newList.pop(0))

print(newList)

newList = ['a', 'd', 'r', 'o', 'b']
numList = [1,2,3,4]

newList.sort() #sorts list items IN PLACE ie. returns None
print(newList)

numList.sort()
print(numList)

numList.reverse()
print(numList)