# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    
    # minimal average can have at most 2 or 3 elements mathematically speaking.
    min_idx = 0
    min_avg = (A[min_idx] + A[min_idx + 1]) / 2

    for i in range(len(A) - 1):
        # Check slice of length 2
        avg_2 = (A[i] + A[i+1]) / 2.0
        if avg_2 < min_avg:
            min_avg = avg_2
            min_idx = i
            
        # Check slice of length 3 (if it exists)
        if i < len(A) - 2:
            avg_3 = (A[i] + A[i+1] + A[i+2]) / 3.0
            if avg_3 < min_avg:
                min_avg = avg_3
                min_idx = i
                
    return min_idx