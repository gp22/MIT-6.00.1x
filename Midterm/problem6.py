def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    For example, if L = [[1, 2], [3, 4], [5, 6, 7]] then deep_reverse(L)
    mutates L to be [[7, 6, 5], [4, 3], [2, 1]]    
    It does not return anything.
    """
    for i in L:
        listRotate(i)
    listRotate(L)
    
def listRotate(L):
    """ assumes L is a list
    Mutates L such that it reverses its elements. 
    For example, if L = [5, 6, 7] then listRotate(L)
    mutates L to be [7, 6, 5]   
    It does not return anything.
    """    
    for i in range(len(L)//2):
        L[i], L[-(i+1)] = L[-(i+1)], L[i]
        
#myList = [5, 6, 7, 8, 9, 10]
#print(myList)
#listRotate(myList)
#print(myList)

#listOfLists = [[1, 2], [3, 4], [5, 6, 7]]
#print(listOfLists)
#deep_reverse(listOfLists)
#print(listOfLists)

L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
deep_reverse(L) 
print(L)