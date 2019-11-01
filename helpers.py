# Import sentence separator from natural language processing tool kit(nltk)
from nltk.tokenize import sent_tokenize

# Return a list of common item(s) in set A and set B
def commonInAandB(splittedA, splittedB):
    result = []
    for item in splittedA:
        if item in splittedB:
            result.append(item)
    return result

# Return lines common in both a and b
def lines(a, b):
    return commonInAandB(set(a.split('\n')), set(b.split('\n')))


# Return sentences common in both a and b
def sentences(a, b):
    return commonInAandB(set(sent_tokenize(a)), set(sent_tokenize(b)))


# Return substrings of length n common in both a and b
def substrings(a, b, n):
    startIndex = 0
    splittedA = set()
    splittedB = set()

    while True:
        if startIndex + n <= len(a):
            splittedA.add(a[startIndex:(startIndex + n)])
        if startIndex + n <= len(b):
            splittedB.add(b[startIndex:(startIndex + n)])
        if startIndex + n > len(a) and startIndex + n > len(b):
            break
        startIndex = startIndex + 1

    return commonInAandB(splittedA, splittedB)
