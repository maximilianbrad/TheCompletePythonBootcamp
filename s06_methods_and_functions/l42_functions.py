def name_function():
    '''
    DOCSTRING: Information about the function
    INPUT: no input
    OUTPUT: Hello .. 
    '''
    print('Hello')

name_function()

def say_hello(name = 'NAME'):
    print('hello ' + name)

say_hello('Max')
say_hello()

def say_bye (name = 'NAME'):
    return 'goodbye ' + name
bye = say_bye('Max')
print(bye)

def add(n1, n2):
    return n1 + n2

result = add(10, 20)
print(result)

'''
Find out if the word "dog" is in a string
'''
def dog_check(string):
    return 'dog' in string.lower()

print(dog_check('my dog ran away'))
print(dog_check('my cat ran away'))

def pig_latin(word):
    first_letter = word[0]
    #vowel check
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    
    return pig_word

print(pig_latin('more'))
print(pig_latin('everywhere'))
