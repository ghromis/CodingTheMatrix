# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num):
    result = []
    return [result for result in L if result%num != 0]



## Problem 2
def myLists(L):
    result =[]
    for e in L:
        l = list(range(1,e+1))
        result.append(l)
    return result


## Problem 3
def myFunctionComposition(f, g):
    result = dict()
    inv_map = {v:k for k, v in f.items()}
    for value in f.values():
        g[value]
        inv_map[value]
        result.update({inv_map[value]:g[value]})
    return result
    
    

## Problem 4
# Please only enter your numerical solution.

complex_addition_a = 5+3j
complex_addition_b = 1j
complex_addition_c = -1 + 0.001j
complex_addition_d = 0.001+9j



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
    current = 0
    for x in L:
        current = current + x
    return current


## Problem 7
def myProduct(L):
    current = 1
    for x in L:
        current = current*x
    return current


## Problem 8
def myMin(L):
    current = max(L)
    for x in L:
        if x < current:
            current = x
    return current


## Problem 9
def myConcat(L):
    current = ""
    for x in L:
        current = current + x
    return current
    

## Problem 10
def myUnion(L):
    current = set()
    for x in L:
        current = current.union(x)
    return current



