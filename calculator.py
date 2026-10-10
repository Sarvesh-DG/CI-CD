def validate_input(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        raise ValueError("Both inputs must be integers")
    if a<=0 or b<=0:
        raise ValueError("Both inputs must be positive integers")
def add(a,b):
    validate_input(a,b)
    return a+b
def sub(a,b):
    validate_input(a,b)
    return a-b
def mul(a,b):
    validate_input(a,b)
    return a*b