def solution(A):
    N = len(A)
    if N < 2:
        return 0

    # Create sorted lists of the start and end points of each interval
    left_boundaries = sorted(J - A[J] for J in range(N))
    right_boundaries = sorted(J + A[J] for J in range(N))

    intersections = 0
    active_discs = 0
    right_ptr = 0

    # We iterate through the left boundaries (starts)
    for left_pt in left_boundaries:
        # Before we process a new disc starting, we check how many 
        # have already ended to our left.
        while left_pt > right_boundaries[right_ptr]:
            active_discs -= 1
            right_ptr += 1
        
        # Every currently active disc intersects with this new one
        intersections += active_discs
        
        # Now this disc is added to the active count
        active_discs += 1
        
        # Requirement: return -1 if we exceed the limit
        if intersections > 10_000_000:
            return -1
            
    return intersections