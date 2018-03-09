'''
Q1
LESSER OF TWO EVENS: Write a function that returns the lesser of two given
numbers if both numbers are even, but returns the greater if one or both
numbers are odd
'''
# my solution
'''
def lesser_of_two_evens(a,b):
    if (a % 2 == 0 and b % 2 == 0):
        if (a < b):
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b
'''
# slightly cleaner solution
def lesser_of_two_evens(a,b):
    if (a % 2 == 0 and b % 2 == 0):
        return min(a,b)
    else:
       return max(a,b)

print(lesser_of_two_evens(4,2))
print(lesser_of_two_evens(5,2))

'''
Q2
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if
both words begin with same letter
'''
def animal_crackers(text):
    text_list = text.lower().split()
    return text_list[0][0] == text_list[1][0]

print(animal_crackers('Levelheaded Llama'), animal_crackers('Crazy Kangaroo'))

'''
Q3
MAKES TWENTY: Given two integers, return True if the sum of the integers is 20
or if one of the integers is 20. If not, return False
'''
def makes_twenty(n1, n2):
    return n1 + n2 == 20 or n1 == 20 or n2 == 20

print(makes_twenty(20,10), makes_twenty(12,8), makes_twenty(2,3)) 

'''
Q4 
OLD MACDONALD: Write a function that capitalizes the first and fourth
letters of a name
'''
# my solution
'''
def old_macdonald(name):
    new_name = ''
    for i, letter in enumerate(name):
        if (i == 0 or i == 3):
            new_name = new_name + letter.upper()
        else:
            new_name = new_name + letter
    return new_name
'''
# solution given
def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]

    return first_half.capitalize() + second_half.capitalize()

print(old_macdonald('macdonald'))

'''
Q5
MASTER YODA: Given a sentence, return a sentence with the words reversed
'''
def master_yoda(text):
    text_list = text.split()
    text_list.reverse()
    return ' '.join(text_list)

print(master_yoda('I am home'), master_yoda('We are ready'))

'''
Q6
ALMOST THERE: Given an integer n, return True if n is within 10
of either 100 or 200
'''
def almost_there(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10

print(almost_there(104), almost_there(150), almost_there(209))

'''
Q7
FIND 33: Given a list of ints, return True if the array contains a 3 next
to a 3 somewhere.
'''
# my solution
'''
def has_33(nums):
    for i, num in enumerate(nums):
        if i + 1 < len(nums):
            if num == 3 and nums[i+1] == 3:
                return True
    return False
'''

# slightly less convoluted solution
def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i:i+2] == [3,3]:
            return True
    return False

print(has_33([1, 3, 3]), has_33([1, 3, 1, 3]), has_33([3, 1, 3]))

'''
Q8
PAPER DOLL: Given a string, return a string where for every character in the
original there are three characters
'''
def paper_doll(text):
    new_text = ''
    for letter in text:
        new_text += letter*3
    return new_text

print(paper_doll('Hello'), paper_doll('Mississippi'))

'''
Q9
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or
equal to 21, return their sum. If their sum exceeds 21 and there's an eleven,
reduce the total sum by 10. Finally, if the sum (even after adjustment)
exceeds 21, return 'BUST'
'''
def blackjack(a, b, c):
    bjack_list = [a, b, c]
    total = sum(bjack_list)
    if total <= 21:
        return total
    else:
        for item in bjack_list:
            if item == 11:
                total -= 10
            if total <= 21:
                return total
        return 'BUST'        

print(blackjack(5,6,7), blackjack(9,9,9), blackjack(10,11,11))

'''
Q10
SUMMER OF '69: Return the sum of the numbers in the array, except ignore
sections of numbers starting with a 6 and extending to the next 9 (every 6
will be followed by at least one 9). Return 0 for no numbers.
'''
# my solution
def summer_69(arr):
    i = 0
    sum = 0
    while i < len(arr):
        if arr[i] == 6:
            while arr[i] != 9:
                i += 1
            i +=1
        else:
            sum += arr[i]
            i += 1
    return sum

# solution given
'''
def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total
'''

print(summer_69([]), summer_69([4, 5, 6, 7, 8, 9]),
      summer_69([2, 1, 6, 9, 11]))

'''
Q11
SPY GAME: Write a function that takes in a list of integers and returns True
if it contains 007 in order
'''
# my solution
'''
def spy_game(nums):
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            while i < len(nums):
                if nums[i] == 0:
                    while i < len(nums):
                        if nums[i] == 7:
                            return True
                        else:
                            i +=1
                else:
                    i += 1
        else:
            i += 1
    return False
'''

# definately cleaner solution
def spy_game(nums):
    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    
    return len(code) == 1

print(spy_game([1,2,4,0,0,7,5]), spy_game([1,0,2,4,0,5,7]), 
      spy_game([1,7,2,0,4,5,0]))

'''
Q12
COUNT PRIMES: Write a function that returns the number of prime numbers
that exist up to and including a given number
'''
def prime_check(num):
    i = 2
    while i <= num**(0.5):
        if num % i == 0:
            return False
        else:
            i += 1
    return True

def count_primes(num):
    counter = 0
    for i in range(2, num+1):
        if prime_check(i):
            counter += 1
    return counter

print(count_primes(1000))