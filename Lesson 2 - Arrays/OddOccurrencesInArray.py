# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    unpaired_numbers_set = set()

    for num in A:
        if num in unpaired_numbers_set:
            unpaired_numbers_set.remove(num)
        else:
            unpaired_numbers_set.add(num)
    
    return unpaired_numbers_set.pop()


def with_xor(A):
    result = 0

    for num in A:
        result ^= num
    
    return result
