import doctest

def cubes(a,b):
    '''
    return all the cubes of values in the range a to b
    >>> cubes(1,5)
    [1, 8, 27, 64]
    >>> cubes(1,101) # doctest:+ELLIPSIS +NORMALIZE_WHITESPACE
    [1, 8, ..., 1000000]
    '''
    answers = []
    for i in range(a,b):
        answers.append(i*i*i) # or i**3
    return answers

if __name__ == '__main__':
    # print(cubes(1,5))
    doctest.testmod(verbose=True)