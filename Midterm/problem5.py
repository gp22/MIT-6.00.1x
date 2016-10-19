def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    returns the sum of the pairwise products of listA and listB
    '''
    listSum = 0
    
    for i in range(len(listA)):
        listSum += listA[i] * listB[i]
    
    return listSum
    
listA = [1, 2, 3]
listB = [4, 5, 6]

print(dotProduct(listA, listB))