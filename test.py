# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def update_row(flat_array, N, target_row):
    start_index = target_row * N
    for i in range(N):
        index = start_index + i
        flat_array[index] = flat_array[index] + 1

def update_col(flat_array, N, target_col):
    for i in range(N):
        index = target_col + (i * N)
        flat_array[index] = flat_array[index] + 1

def solution(N, A, S):
    # Implement your solution here
    highest_value = 0
    result = [0] * N * N

    for index, operation in enumerate(S):
        if operation == 'R':
            target_row = A[index]
            update_row(result, N, target_row)      
        elif operation == 'C':
            target_col = A[index]
            update_col(result, N, target_col)
    
    for value in result:
        if value > highest_value:
            highest_value = value
    
    return highest_value
