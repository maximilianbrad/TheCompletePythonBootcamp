my_list = [1,2,3]

my_list = ['String', 100, 23.1]

print(len(my_list))

my_list = ['one', 'two', 'three']

#Indexing and Slicing work the same for lists as strings
print(my_list[0])

print(my_list[1:])

#Concatenation
anotherList = ['four', 'five']

print(my_list + anotherList)

print(my_list, anotherList)

new_list = my_list + anotherList

print(new_list)

#Lists are MUTABLE
new_list[0] = 'ONE ALL CAPS'

print(new_list)

#list methods
new_list.append('six')

print(new_list)

print(new_list.pop()) #function returns popped item

print(new_list)

popped_item = new_list.pop()

print(popped_item)

print(new_list.pop(0))

print(new_list)

new_list = ['a', 'd', 'r', 'o', 'b']
num_list = [1,2,3,4]

new_list.sort() #sorts list items IN PLACE ie. returns None
print(new_list)

num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)