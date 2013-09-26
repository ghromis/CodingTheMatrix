# version code 988
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec
from independence import is_independent
from vec import Vec
import itertools



## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    while True:
        u = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
        if a0*u == s and b0*u == t:
            return u

       
def helper():
    L0 = []
    while True:
        a1 = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
        b1 = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
        a2 = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
        b2 = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
        if is_independent ([a0, b0, a1, b1, a2, b2]) == True:
            break
        L0 = [a0, b0, a1, b1, a2, b2]
    while True:
        a3 = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
        b3 = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
        L1 = [a0, b0, a1, b1, a3, b3]
        L2 = [a0, b0, a2, b2, a3, b3]
        L3 = [a1, b1, a2, b2, a3, b3]
        if is_independent (L1) == True and is_independent (L2) == True and is_independent (L3) == True:
                break           
    while True:
        a4 = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
        b4 = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
        L4 = [a0, b0, a1, b1, a4, b4]
        L5 = [a0, b0, a2, b2, a4, b4]
        L6 = [a1, b1, a2, b2, a4, b4]
        L7 = [a0, b0, a3, b3, a4, b4]
        L8 = [a1, b1, a3, b3, a4, b4]
        L9 = [a2, b2, a3, b3, a4, b4]
        if is_independent (L4) == True and is_independent (L5) == True and is_independent (L6) == True and is_independent (L7) == True and is_independent (L8) == True and is_independent (L9) == True:
            break
    return a0, b0, a1, b1, a2, b2, a3, b3, a4, b4

   

## Problem 2
# Give each vector as a Vec instance
secret_a0 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: 0, 3: one, 4: 0, 5: one})
secret_b0 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: 0, 3: 0, 4: 0, 5: one})

secret_a1 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: one, 3: 0, 4: one, 5: 0})
secret_b1 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: 0, 2: one, 3: one, 4: 0, 5: one})

secret_a2 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: 0, 2: one, 3: one, 4: 0, 5: 0})
secret_b2 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: one, 3: 0, 4: 0, 5: 0})

secret_a3 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: 0, 3: 0, 4: one, 5: one})
secret_b3 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: one, 3: one, 4: one, 5: 0})

secret_a4 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: 0, 2: 0, 3: 0, 4: one, 5: 0})
secret_b4 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: 0, 3: 0, 4: 0, 5: 0})

