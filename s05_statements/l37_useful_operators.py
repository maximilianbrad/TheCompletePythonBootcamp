# range operator
for num in range(0,11,2):
    print(num)

print(list(range(0,10,1)))

#enumerate operator
# common operation
'''
index_count = 0
word = 'abcde'

for letter in word:
    print(word[index_count])
    index_count += 1
'''

# can do this instead
word = 'abcde'
for index,letter in enumerate(word):
    print(index,'\n'+letter,'\n')

# zip operator
my_list1 = [1,2,3]
my_list2 = ['a', 'b', 'c']
my_list3 = [100, 200, 300]

for item in zip(my_list1, my_list2, my_list3):
    print(item)

# in operator
print('x' in [1,2,3])
print('x' in ['x','y','z'])
print('a' in 'a world')
print('mykey' in {'mykey':345})

d = {'mykey':345}
print(345 in d.values(), 345 in d.keys())

# min, max and random
mylist = [10, 23, 34, 45, 100]

print(min(mylist))
print(max(mylist))

from random import shuffle
mylist = [1,2,3,4,5,6,7,8]
shuffle(mylist)
print(mylist)

from random import randint
print(randint(0,100))

# input function
result = input('Enter a number here: ')
print(result)