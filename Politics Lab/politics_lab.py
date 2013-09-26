voting_data = list(open("voting_record_dump109.txt"))

## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    l=[]
    mylist= []
    d = {}
    for e in voting_data:
        splitted = e.split(" ")
        l.append(splitted)
    for e in l:
        spl = e[3:]
        spl = list(map(int, spl))
        d[e[0]]=spl
    return d

## Task 2

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """
    return sum([a*b for (a,b) in zip(voting_dict[sen_a], voting_dict[sen_b])])


## Task 3

def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    result = -1000000
    most_s = set()
    for k in voting_dict.keys():
        if k != sen:
            new_result = policy_compare(sen, k, voting_dict)
            if new_result > result:
                result = new_result
                most_s = (k, result)
    return most_s[0]
    

## Task 4

def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """
    result = 1000000
    least_s = set()
    for k in voting_dict.keys():
        if k != sen:
            new_result = policy_compare(sen, k, voting_dict)
            if new_result < result:
                result = new_result
                least_s = (k, result)
    return least_s[0]
        
## Task 5

most_like_chafee    = most_similar('Chafee', create_voting_dict())
least_like_santorum = least_similar('Santorum', create_voting_dict()) 

# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    result = 0
    for n in sen_set:
        new_result = policy_compare(sen, n, voting_dict)
        result += new_result
    return result / len(sen_set)

def dems(voting_dict):
    l=[]
    dems = []
    for e in voting_data:
        splitted = e.split(" ")
        l.append(splitted)
    for e in l:
        if e[1]=='D':
            dems.append(e)
    return dems

def create_voting_dict_dems():
    l=[]
    mylist= []
    d = {}
    for e in dems(voting_data):
        spl = e[3:]
        spl = list(map(int, spl))
        d[e[0]]=spl
    return d

def sen_set_dems(voting_dict):
    dem_set = set()
    for key in voting_dict:
        dem_set.add(key)
    return dem_set

def most_average(sen_set, voting_dict):
    most_avg = -1000000
    for e in sen_set:
        new_avg = find_average_similarity(e, sen_set, voting_dict)
        if most_avg < new_avg:
            most_avg = new_avg
    return (most_avg, e)
        
        
most_average_Democrat = 'Kerry' # give the last name (or code that computes the last name)

# Task 7

def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """
    l=[]
    for e in sen_set:
        voting_recs = voting_dict[e]
        l.extend([voting_recs])
    return [sum([el[i] for el in l])/len(sen_set) for i in range(len(l[0]))]
        

average_Democrat_record = [-0.16279069767441862, -0.23255813953488372, 1.0, 0.8372093023255814,
                           0.9767441860465116, -0.13953488372093023, -0.9534883720930233,
                           0.813953488372093, 0.9767441860465116, 0.9767441860465116,
                           0.9069767441860465, 0.7674418604651163, 0.6744186046511628,
                           0.9767441860465116, -0.5116279069767442, 0.9302325581395349,
                           0.9534883720930233, 0.9767441860465116, -0.3953488372093023,
                           0.9767441860465116, 1.0, 1.0, 1.0, 0.9534883720930233,
                           -0.4883720930232558, 1.0, -0.32558139534883723, -0.06976744186046512,
                           0.9767441860465116, 0.8604651162790697, 0.9767441860465116,
                           0.9767441860465116, 1.0, 1.0, 0.9767441860465116, -0.3488372093023256,
                           0.9767441860465116, -0.4883720930232558, 0.23255813953488372,
                           0.8837209302325582, 0.4418604651162791, 0.9069767441860465,
                           -0.9069767441860465, 1.0, 0.9069767441860465, -0.3023255813953488]
# (give the vector)


# Task 8

def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    result = 1000000
    most_s = set()
    for key in voting_dict:
        for n in voting_dict:
            new_result = policy_compare(key, n, voting_dict)
            if new_result < result:
                result = new_result
                most_s = (key, n)
    return most_s

