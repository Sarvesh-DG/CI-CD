def input_validation(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        raise ValueError("The inputs must be integers")
    if a<=0 or b<=0:
        raise ValueError("The inputs must be Positive integers")
def add(a,b):
    input_validation(a,b)
    return a+b
def sub(a,b):
    input_validation(a,b)
    return a-b
def mul(a,b):
    input_validation(a,b)
    return a*b