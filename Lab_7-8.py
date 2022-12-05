#author ate (11/28/22)

#def statements
def times (integer):
    '''square a number'''
    new_sum = integer * integer
    return new_sum

def square (name):
    '''cube a sqaured number'''
    number = times(name)**3
    return number

def adding (integer):
    '''adding the first two numbers together'''
    add = times(integer) + square(integer)
    return add

#print statement
print(adding(2))