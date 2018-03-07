t = (1,2,3)
my_list = [1,2,3]

print(type(t))
print(my_list)

print(t)

t = ('one', 2)

#can index a tuple like a list
print(t[0],t[-1])

#tuple methods
t = ('a', 'a', 'b')

print(t.count('a'))
print(t.index('a'), t.index('b'))

print(t, my_list)

my_list[0] = 'NEW'
print(my_list)

#t[0] = 'NEW' throws an error
print(t)