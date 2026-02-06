# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    distance = Y - X
    modulo = distance % D
    minimum_jumps = distance // D
     
    return minimum_jumps if modulo == 0 else minimum_jumps + 1

def with_integer_ceiling(X, Y, D):
    # This formula (a + b - 1) // b is a standard way to get ceil(a/b) 
    # without using floats or if-statements.
    return (Y - X + D - 1) // D