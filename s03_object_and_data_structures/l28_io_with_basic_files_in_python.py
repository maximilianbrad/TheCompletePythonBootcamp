my_file = open('./test.txt')

print(my_file.read())

# Cursor is at the end of the file
print(my_file.read())

my_file.seek(0)
print(my_file.read())

my_file.seek(0)
contents = my_file.read()

print(contents)

my_file.seek(0)
print(my_file.readlines())

my_file.close()

with open('./test.txt') as my_file:
    contents = my_file.read()

print(contents)

with open('./test_two.txt', mode = 'r') as f:
    print(f.read())

with open('./test_two.txt', mode = 'a') as f:
    f.write('\nFOUR ON FOURTH')

with open('./test_three.txt', mode = 'w') as f:
    f.write('I CREATED THIS FILE!')

with open('./test_three.txt', mode = 'r') as f:
    print(f.read())