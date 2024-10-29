def maxium_sub_array_brute_force(A):
    max_sum = float('-inf')
    max_start, max_end = (None, None)
    for i in range(len(A)):
        curr_sum = 0
        for j in range(i, len(A)):
            curr_sum += A[j]

            if curr_sum > max_sum:
                max_sum = curr_sum
                max_start = i
                max_end = j

    return (max_start, max_end, max_sum)


def find_max_crossing_subarray(A, low, mid, high):
    left_max_sum = float('-inf')
    left_max
    for i in range(mid, low - 1, -1):
        