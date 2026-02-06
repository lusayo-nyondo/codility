# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    return len(set(A))

def sort_solution(A):
    if not A:
        return 0
    
    # Sorting takes O(N log N) time
    A.sort()
    
    # We start at 1 because the first element is always "distinct" 
    # compared to nothing.
    distinct_count = 1
    
    for i in range(1, len(A)):
        # If the current element is different from the one before it,
        # it's a new unique value.
        if A[i] != A[i-1]:
            distinct_count += 1
            
    return distinct_count