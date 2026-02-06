def solution(A):
    # Logic: bidirectional pass using kadane's algorithm to find best meeting point at Y."
    N = len(A)

    left_max_slice_at_index = [0] * N
    right_max_slice_at_index = [0] * N

    # calculate left max slice sum for each potential Y
    for i in range(1, N - 1):
        left_max_slice_at_index[i] = max(0, left_max_slice_at_index[i - 1] + A[i])
    
    # calculate right max slice sum for each potential Y
    for i in range(N - 2, 0, -1):
        right_max_slice_at_index[i] = max(0, right_max_slice_at_index[i + 1] + A[i])

    # calculate the maximum sum by combining left at right at each Y and comparing.
    max_double_slice = 0

    for i in range(1, N - 1):
        current_sum = left_max_slice_at_index[i - 1] + right_max_slice_at_index[i + 1]
        max_double_slice = max(max_double_slice, current_sum)
    
    return max_double_slice

