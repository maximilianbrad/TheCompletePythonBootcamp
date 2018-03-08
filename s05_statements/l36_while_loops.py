x = 0

while x < 5:
    print(f'The current value of x is {x}')
    x += 1
else:
    print("X IS NOT LESS THAN FIVE")

# break, continue and pass

x = [1,2,3]
for item in x:
    # pass is used as a placeholder to prevent syntax error
    pass

my_string = 'Sammy'
for letter in my_string:
    if letter == 'a':
        # continue moves the code back to the top of the 
        # nearest enclosing loop
        continue
    print(letter)

for letter in my_string:
    if letter == 'a':
        # break stops the nearest enclosing loop
        break
    print(letter)

x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1