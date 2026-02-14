# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def naive_solution(A):
    possible_solutions = set(range(1, 1000002))

    for num in A:
        if num in possible_solutions:
            possible_solutions.remove(num)
    
    return min(possible_solutions)

def solution(A):
    positive_numbers = set(num for num in A if num > 0)

    if len(positive_numbers) <= 0:
        return 1

    target = 1

    while target <= 1_000_000:
        if target not in positive_numbers:
            return target
    