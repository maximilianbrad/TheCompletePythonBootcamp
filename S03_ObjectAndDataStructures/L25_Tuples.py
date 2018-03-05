t = (1,2,3)
myList = [1,2,3]

print(type(t))
print(myList)

print(t)

t = ('one', 2)

#can index a tuple like a list
print(t[0],t[-1])

#tuple methods
t = ('a', 'a', 'b')

print(t.count('a'))
print(t.index('a'), t.index('b'))

print(t, myList)

myList[0] = 'NEW'
print(myList)

#t[0] = 'NEW' throws an error
print(t)