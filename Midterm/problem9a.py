#==============================================================================
# a function to flatten a list. The list contains other lists, strings,
# or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened
# into [1,'a','cat',2,3,'dog',4,5] (order matters).
#==============================================================================

def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    if aList == []:
        return aList
    if type(aList[0]) == list:
        return flatten(aList[0]) + flatten(aList[1:])
    return aList[:1] + flatten(aList[1:])
    
aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
newList = flatten(aList)
print(newList)