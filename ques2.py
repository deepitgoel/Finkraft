#Implement a Python function that takes a list of integers and a target number as input, 
# and returns a tuple of two integers that add up to the target number.
def solve( A, B):
    '''
    A: list of integeres
    B: target number
    '''
    
    for i in A:
        if (B - i) in A :
            return (i, B-i)
    return -1
