# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # Implement your solution here
    if not A or K == 0:
        return A
    
    shift = K % len(A)

    leading = A[-shift:]
    trailing = A[:-shift]

    return leading + trailing

def left_shift(A, K):
    if not A or K == 0:
        return A
    
    shift = K % len(A)

    leading = A[shift:]
    trailing = A[:shift]

    new_array = leading + trailing
    return new_array