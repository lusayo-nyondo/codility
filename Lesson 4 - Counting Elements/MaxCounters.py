# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def naive_solution(N, A):
    counters = [0] * N

    for X in A:
        if 1 <= X and X <= N:
            counters[X - 1] += 1
        
        if X == N + 1:
            current_max = max(counters)
            counters = [current_max] * N
    
    return counters


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    counters = [0] * N

    current_baseline = 0
    current_max = 0
    
    for X in A:
        if 1 <= X <= N:
            current_value = counters[X - 1]

            if current_value < current_baseline:
                current_value = current_baseline
            
            current_value = current_value + 1
    
            if current_max < current_value:
                current_max = current_value
    
            counters[X - 1] = current_value
                
        if X == N + 1:
            current_baseline = current_max

    for index, value in enumerate(counters):
        if value < current_baseline:
            counters[index] = current_baseline
    
    return counters
