# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def naive_solution(A):
    east_bound_cars = 0
    passing_cars = 0

    LIMIT = 1000000000

    for direction in A:
        if direction == 0:
            east_bound_cars += 1
        else:
            passing_cars += east_bound_cars
        
        if passing_cars > LIMIT:
            return -1
    
    return passing_cars
