# Write a program that counts up the number of vowels contained in the 
# string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, 
# if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

def countVowels(theStr):
    vowels = 'aeiou'
    count = 0
    for c in theStr:
        if c in vowels:
            count += 1
    return count

s = 'azcbobobegghakl'

print('Number of vowels:', countVowels(s))
