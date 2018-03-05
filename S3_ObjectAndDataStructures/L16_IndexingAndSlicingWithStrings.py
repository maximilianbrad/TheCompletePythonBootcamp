mystring = 'Hello World'

print(mystring)

print(mystring[0])

print(mystring[8])

print(mystring[-2])

mystring = 'abcdefghijk'

print(mystring[2:]) #print from index 2 to end of string

print(mystring[:3]) #print up to but not including index 3

print(mystring[3:6]) #print from index 3 up to but not including index 6

print(mystring[1:3])

print(mystring[::2]) #print from begining to end in step size of 2

print(mystring[::-1]) #print in reverse order

#print from index 2 ('c') up to index 7 ('h') with stepsize of 2
print(mystring[2:7:2]) #combining everything