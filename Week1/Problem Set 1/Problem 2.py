# A program that prints the number of times the string 'bob' occurs in s. 
# For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2

def count(substr,theStr):
    c = 0
    for i in range(len(theStr)):
        if substr in (theStr[i:(i + len(substr))]):
            c += 1
    return c

substring = 'bob'
s = 'azcbobobegghakl'

print('Number of times bob occurs is:', count(substring, s))
