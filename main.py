arr1 = [1,2,3,4,5,6,7,7,5,4,3,2]
arr2 = [1,2,3,4,5,6,7]

def isAllElementsIndividual(arr):
    setFromArr = set(arr)
    return True if len(arr) == len(setFromArr) else False
print(isAllElementsIndividual(arr1))
print(isAllElementsIndividual(arr2))