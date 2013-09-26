# version code 988
# Please fill out this stencil and submit using the provided submission script.

from matutil import *
from GF2 import one
from echelon import transformation
from vec import Vec
from vecutil import zero_vec
from triangular import triangular_solve



## Problem 1
# Write each matrix as a list of row lists

echelon_form_1 = [[1,2,0,2,0],
                  [0,1,0,3,4],
                  [0,0,2,3,4],
                  [0,0,0,2,0],
                  [0,0,0,0,4]]

echelon_form_2 = [[0,4,3,4,4],
                  [0,0,4,2,0],
                  [0,0,0,0,1],
                  [0,0,0,0,0]]

echelon_form_3 = [[1,0,0,1],
                  [0,0,0,1],
                  [0,0,0,0]]

echelon_form_4 = [[1,0,0,0],
                  [0,1,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]



## Problem 2
def is_echelon(A):
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    Examples:
        >>> is_echelon([[1,1,1],[0,1,1],[0,0,1]])
        True
        >>> is_echelon([[0,1,1],[0,1,0],[0,0,1]])
        False
    '''
    K=[]
    if A[0][0]==0:
        K.append(1)
    else:
        K.append(-1)
        
    for l in A[1:]:
        if 0 not in l:
            return False
        else:
            for n, e in enumerate(l):
                if e !=0:
                    K.append(n)
                    break
    if len(K) > len(set(K)):
        return False
    if -1 in K and 0 in K:
        return False                         
    return K == sorted(K)
        

## Problem 3
# Give each answer as a list

echelon_form_vec_a = [0,5,3,0]
echelon_form_vec_b = [-3,0,-2,3]
echelon_form_vec_c = [0,-5,2,0,2]



## Problem 4
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None".

solving_with_echelon_form_a = None
solving_with_echelon_form_b = [5,8,2,0,0]



## Problem 5
def echelon_solve(rowlist, label_list, b):
    '''
    Input:
        - rowlist: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in rowlist
        - b: a vector (represented as a list)
    Output:
        - Vec x such that rowlist * x is b
    >>> D = {'A','B','C','D','E'}
    >>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}),
                  Vec(D,{'C':one})] 
    >>> b_list = [one,0,one]
    >>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list)
    Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    '''
    D = rowlist[0].D
    x = zero_vec(D)
    for j in reversed(range(len(rowlist))):
        row = rowlist[j]
        for c in label_list:
            if c in row.f.keys() and row.f[c]== one:
                x[c] = (b[j] - x*row)/row[c]
                break
    return x




## Problem 6
rowlist = [Vec({'A', 'B', 'C', 'D'},{'A':one, 'B':one, 'C':0, 'D':one}),
           Vec({'A', 'B', 'C', 'D'},{'A':0, 'B':one, 'C':0, 'D':0}),
           Vec({'A', 'B', 'C', 'D'},{'A':0, 'B':0, 'C':one, 'D':0}),
           Vec({'A', 'B', 'C', 'D'},{'A':0, 'B':0, 'C':0, 'D':one})]
# Provide as a list of Vec instances
label_list = ['A', 'B', 'C', 'D'] # Provide as a list
b = [one, one, 0, 0]          # Provide as a list



## Problem 7
null_space_rows_a = {3,4} # Put the row numbers of M from the PDF



## Problem 8
null_space_rows_b = {4}



## Problem 9
# Write each vector as a list
closest_vector_1 = [8/5, 16/5]
closest_vector_2 = [0,1,0]
closest_vector_3 = [3,2,1,-4]



## Problem 10
# Write each vector as a list

project_onto_1 = [2,0]
projection_orthogonal_1 = [0,1]

project_onto_2 = [-1/6,-1/3,1/6]
projection_orthogonal_2 = [1.166666666,1.333333333,3.8333333333]

project_onto_3 = [1,1,4]
projection_orthogonal_3 = [0,0,0]



## Problem 11
norm1 = 3
norm2 = 4
norm3 = 1

