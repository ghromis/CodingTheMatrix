from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0, len(review_options)-1)]

## Tasks 2 and 3 are in dictutil.py

## Task 4    
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    #strlist2 = [x.lower() for x in strlist]
    list_of_words = []
    list2=[]
    for key in strlist:
        list_of_words.append(key)
        words = {k:v for (k,v) in enumerate(list_of_words)}
    t = list(words.values())
    for e in t:
        list2.extend(e.split())
    return { word : set(txt for txt, wrds in words.items() if word in wrds.split())
        for word in list2}

## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    results = set()
    for e in query:
        if e in inverseIndex.keys():
            value = inverseIndex[e]
            results.update(value)
    return results

## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    results1 = []
    results2 = set()
    for e in query:
        if e in inverseIndex.keys():
            value = inverseIndex[e]
            results1.extend(value)
    for doc_id in results1:
        if results1.count(doc_id)== len(query):
            results2.update({doc_id})
    return results2

