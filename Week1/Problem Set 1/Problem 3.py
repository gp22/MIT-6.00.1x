# A program that prints the longest substring of s in which the letters occur 
# in alphabetical order. For example, if s = 'azcbobobegghakl', then your 
# program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, 
# if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc

def longest_substr(theStr):
    substr = theStr[0]    
    tempstr = ''
    for i in range(1,len(theStr)):
        # if the next character is in alphabetical order
        # add it to the string        
        if theStr[i] >= theStr[i-1]:
            substr += theStr[i]
        else:
            if len(substr) > len(tempstr):
                tempstr = substr            
            substr = theStr[i]
            
    # return the longest of the two strings
    if len(substr) > len(tempstr):
        return substr
    else:
        return tempstr

s = 'azcbobobegghakl'

print('Longest substring in alphabetical order is:', longest_substr(s))
