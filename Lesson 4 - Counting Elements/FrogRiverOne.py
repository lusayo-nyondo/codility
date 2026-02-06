def naive_solution(X, A):
    position_counts = [0] * (X + 1)

    for second in range(len(A)):
        position = A[second]
        position_counts[position] += 1

        if 0 not in position_counts[1:]:
            return second
    
    return -1

def set_based_solution(X, A):
    positions_accounted_for = set()

    for time, position in A:
        if position > 0 and position <= X:
            positions_accounted_for.add(position)
        
        if len(positions_accounted_for) == X:
            return time
    
    return -1

def counter_boolean_array_solution(X, A):
    # 'seen' tracks if a leaf has already fallen at a position
    # We use X + 1 so we can use the position as a direct index
    seen = [False] * (X + 1)
    
    # How many unique positions we still need to fill
    count = X 

    for time, position in enumerate(A):
        # We only care about positions between 1 and X
        # AND we check if we haven't seen a leaf there yet
        if position <= X and not seen[position]:
            seen[position] = True
            count -= 1
            
            # As soon as count hits 0, we have all positions covered
            if count == 0:
                return time
                
    return -1