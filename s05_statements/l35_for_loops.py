my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in my_list:
    print(num)
    print('hello')

for num in my_list:
    #check for even
    if (num % 2 == 0):
        print(num)
    else:
        print(f'Odd number: {num}')

list_sum = 0

for num in my_list:
    list_sum += num
    print(list_sum)

for letter in 'Hello World':
    print(letter)

tup = (1, 2, 3)

for item in tup:
    print(item)

#example of tuple unpacking
my_list = [(1,2),(3,4),(5,6),(7,8)]
for a,b in my_list:
    print(a)
    print(b)

my_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a,b,c in my_list:
    print(b)

d = {'k1':1, 'k2':2, 'k3':3}
for key,value in d.items():
    print(value)
