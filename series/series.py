
def fibonacci(n):
    '''  this function calculates the fibonacci for a number.
    :param => n:int 
    :return => int 
    '''

    if n == 0 :
        return 0
    if n == 1 :
        return 1
    if n > 1 :
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    '''  this function calculates the lucas for a number.
    :param => n:int 
    :return => int 
    '''

    if n == 0 :
        return 2 
    if n == 1 :
        return 1
    if n > 1 :
        return lucas(n-1) + lucas(n-2)



    
    