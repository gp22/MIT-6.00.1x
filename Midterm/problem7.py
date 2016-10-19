#Write a function called dict_interdiff that takes in two dictionaries
#(d1 and d2). The function will return a tuple of two dictionaries:
#a dictionary of the intersect of d1 and d2 and a dictionary of the
#difference of d1 and d2, calculated as follows:
#
#intersect: The keys to the intersect dictionary are keys that are common
#in both d1 and d2. To get the values of the intersect dictionary, look at
#the common keys in d1 and d2 and apply the function f to these keys' values --
#the value of the common key in d1 is the first parameter to the function and
#the value of the common key in d2 is the second parameter to the function.
#
#difference: a key-value pair in the difference dictionary is (a) every
#key-value pair in d1 whose key appears only in d1 and not in d2 or (b) every
#key-value pair in d2 whose key appears only in d2 and not in d1.
#
#Example:
#
#If f(a, b) returns a + b
#d1 = {1:30, 2:20, 3:30, 5:80}
#d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
#then dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})

def f(a, b):
    return a > b
    
def dict_interdiff(d1, d2):    
    result = ({}, {})
    for key in d1:                              # iterate through each key in d1
        if key in d2.keys():                    # see if the same key exists in d2
            result[0][key] = f(d1.get(key), d2.get(key))  # if it does, add it to the first dictionary in the tuple
        else:                                   # otherwise:
            result[1][key] = d1.get(key)        # add it to the second dictionary in the tuple
    
    for key in d2:                              # iterate through each key in d2
        if key not in d1.keys():                # if it's not in d1, add it to tuple dictionary 2
            result[1][key] = d2.get(key)
    
    return result

d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}

print(dict_interdiff(d1, d2))