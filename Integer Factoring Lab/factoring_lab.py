from vec import Vec
from GF2 import one
from math import sqrt

from factoring_support import dumb_factor
from factoring_support import intsqrt
from factoring_support import gcd
from factoring_support import primes
from factoring_support import prod

import echelon


## Task 1
def int2GF2(i):
    '''
    Returns one if i is odd, 0 otherwise.

    Input:
        - i: an int
    Output:
        - one if i is congruent to 1 mod 2
        - 0   if i is congruent to 0 mod 2
    Examples:
        >>> int2GF2(3)
        one
        >>> int2GF2(100)
        0
    '''
    if i%2 == 0:
        return 0
    else:
        return one


## Task 2
def make_Vec(primeset, factors):
    '''
    Input:
        - primeset: a set of primes
        - factors: a list of factors [(p_1,a_1), ..., (p_n, a_n)]
                   with p_i in primeset
    Output:
        - a vector v over GF(2) with domain primeset
          such that v[p_i] = int2GF2(a_i) for all i
    Example:
        >>> make_Vec({2,3,11}, [(2,3), (3,2)]) == Vec({2,3,11},{2:one})
        True
    '''
    rdict = {}
    r = Vec(primeset, rdict)
    for e in factors:
        rdict[e[0]]= int2GF2(e[1])
    return r

## Task 3
def find_candidates(N, primeset):
    '''
    Input:
        - N: an int to factor
        - primeset: a set of primes

    Output:
        - a list [roots, rowlist]
        - roots: a list a_0, a_1, ..., a_n where a_i*a_i - N can be factored
                 over primeset
        - rowlist: a list such that rowlist[i] is a
                   primeset-vector over GF(2) corresponding to a_i
          such that len(roots) = len(rowlist) and len(roots) > len(primeset)
    '''
    roots=[]
    rowlist = []
    i = 2
    k=0
    while k < len(primeset)+1:
        x = intsqrt(N)+i
        T = dumb_factor(x*x - N, primeset)
        if T != []:
            roots.append(x)
            factors = T
            row = make_Vec(primeset, factors)
            rowlist.append(row)
            k +=1
        i +=1
        
    return roots, rowlist
            

## Task 4
def find_a_and_b(v, roots, N):
    '''
    Input: 
     - a {0,1,..., n-1}-vector v over GF(2) where n = len(roots)
     - a list roots of integers
     - an integer N to factor
    Output:
      a pair (a,b) of integers
      such that a*a-b*b is a multiple of N
      (if v is correctly chosen)
    '''
    alist = []
    d=[]
    
    for k, v in v.f.items():
        if v == one:
            d.append(k)
    for n, root in enumerate(roots):
        if n in d:
            alist.append(root)      
    a = prod(alist)
    c = prod(x*x -N for x in alist)
    b = intsqrt(c)
    if b*b == c:
        return a, b



## Task 5

smallest_nontrivial_divisor_of_2461799993978700679 = 1230926561
