'''
Q1
Use for, split(), and if to create a Statement that will print out words that 
start with 's':
'''
st = 'Print only the words that start with s in this sentence'
for words in st.split():
    if (words[0] == 's'):
        print(words)

'''
Q2
Use range() to print all the even numbers from 0 to 10.
'''
# my solution
for x in range(0, 11):
    if (x % 2 == 0):
        print(x)

# solution from solutions lecture
for x in range(0, 11, 2):
    print(x)

'''
Q3
Use List comprehension to create a list of all numbers between 
1 and 50 that are divisible by 3.
'''
my_list = [x for x in range(0, 50) if x % 3 == 0]
print(my_list)

'''
Q4
Go through the string below and if the length of a word is even print "even!"
'''
st = 'Print every word in this sentence that has an even number of letters'
for words in st.split():
    if (len(words) % 2 == 0):
        print('"{w}" has an even number of letters!'.format(w=words))

'''
Q5
Write a program that prints the integers from 1 to 100. But for multiples of
three print "Fizz" instead of the number, and for the multiples of five print
"Buzz". For numbers which are multiples of both three and five print
"FizzBuzz".
'''
for num in range(1, 101):
    if (num % 3 == 0 and num % 5 == 0):
        print('FizzBuzz')
    elif (num % 3 == 0):
        print('Fizz')
    elif (num % 5 == 0):
        print('Buzz')
    else:
        print(num)
'''
Q6
Use List Comprehension to create a list of the first letters of every word in
the string below:
'''
st = 'Create a list of the first letters of every word in this string'
my_list2 = [x[0] for x in st.split()]
print(my_list2)
