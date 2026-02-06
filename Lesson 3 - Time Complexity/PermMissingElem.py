# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    N = len(A) + 1
    cumulative_sum = ((N) * (N + 1)) // 2
    current_sum = sum(A)

    missing_number = cumulative_sum - current_sum
    return missing_number
