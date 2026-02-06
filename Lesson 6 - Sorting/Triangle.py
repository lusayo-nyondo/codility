# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if len(A) < 3:
        return 0

    A.sort()

    for i in range(len(A) - 2):
        P, Q, R = A[i], A[i + 1], A[i + 2]

        if P + Q > R:
            return 1
    
    return 0
