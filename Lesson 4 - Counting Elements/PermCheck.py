# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    array_len = len(A)
    number_set = set(A)

    if array_len != len(number_set):
        return 0

    expected_cumulative_sum = (array_len * (array_len + 1)) // 2
    current_cumulative_sum = sum(number_set)

    return 1 if expected_cumulative_sum == current_cumulative_sum else 0
