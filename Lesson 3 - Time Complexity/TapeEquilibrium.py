# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    lowest_p_value = float('inf')
    
    left_value = 0
    right_value = sum(A)

    for num in A:
        left_value += num
        right_value -= num

        diff = abs(right_value - left_value)

        if diff < lowest_p_value:
            lowest_p_value = diff
    
    return lowest_p_value
