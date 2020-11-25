import re

m = re.search('(?<=abc123)def', 'abc123def')
print(m.group(0))

def abss(n):
    '''
    Function to get absolute value of number

    Example:
    >>> abss(1)
    1
    >>> abss(-1)
    1
    >>> abss(0)
    0
    >>> abss('a')
    Traceback (most recent call last):
        ...
    ValueError: 'a'
    '''
    return n if n >= 0 else (-n)
#print(abss(0))

def fact(n):
    '''
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    10*fact(9)
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError: value > zero
    '''
    if(n < 1):
        raise ValueError()
    if(n == 1):
        return 1
    return n * fact(n - 1)

if __name__=="__main__":
    import doctest
    doctest.testmod()

