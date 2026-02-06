# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A.sort()

    max_positive_product = A[-3] * A[-2] * A[-1]
    max_negatives_included_product = 1

    if A[0] <= A[1] < 0:
        max_negatives_included_product = A[0] * A[1] * A[-1]
    
    return max(max_positive_product, max_negatives_included_product)
