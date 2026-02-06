# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    if len(A) == 1:
        return A[0]

    current_sliding_max = A[0]
    global_max = A[0]

    for num in A[1:]:
        # since negative numbers can bring the max down
        possible_max = current_sliding_max + num
        if num > possible_max:
            current_sliding_max = num
        else:
            current_sliding_max = possible_max

        global_max = max(current_sliding_max, global_max)

    return global_max
