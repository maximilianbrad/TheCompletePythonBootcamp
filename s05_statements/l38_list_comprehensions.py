# this is common
'''
my_string = 'hello'
my_list = []
for letter in mystring:
    my_list.append(letter)
'''

# this does the same
my_string = 'hello'
my_list = [letter for letter in my_string]
print(my_list)

# can perform operations
my_list = [x**2 for x in range(0,11)]
print(my_list)

# can add a conditional
my_list = [x for x in range(0,11) if x%2==0]
print(my_list)

# also this
celcius = [0,10, 20, 34.5]
fahrenheit = [((9/5*temp + 32)) for temp in celcius]

print(fahrenheit)

# if/else in list comprehentions
# remember that readability is still king
results = [x if x%2==0 else 'ODD' for x in range(0,11)]

#nested loops in list comprehentions
my_list = [x*y for x in [2,4,6] for y in [1,10,100]]
print(my_list)