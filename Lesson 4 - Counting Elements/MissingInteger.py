# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def naive_solution(A):
    possible_solutions = set(range(1, 1000002))

    for num in A:
        if num in possible_solutions:
            possible_solutions.remove(num)
    
    return min(possible_solutions)
