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
    # TO-DO check this too     
    max_left_index = mid
    max_left_sum = float('-inf')
    current_sum = 0
    for i in range(mid, low - 1, -1):
        current_sum += A[i]

        if current_sum > max_left_sum:
            max_left = i
            max_left_sum = current_sum
    
    max_right_index = mid
    max_right_sum = float('-inf')
    current_sum = 0
    for i in range(mid+1, high+1):
        current_sum += A[i]

        if current_sum > max_right_sum:
            max_right_sum = current_sum
            max_right_index = i
    
    if max_left_sum == float('-inf'):
        max_left_sum = 0
    
    if max_right_sum == float('-inf'):
        max_right_sum = 0

    return max_left_index, max_right_index, max_left_sum + max_right_sum

def find_max_subarray(A, low, high):
    # TO-DO check this
    if low == high:
        return low, high, A[low]
    
    mid = (low + high) / 2

    left_low, left_high, left_sum = find_max_subarray(A, low, mid)

    mid_low, mid_high, mid_sum = find_max_crossing_subarray(A, low, mid, high)

    right_low, right_high, right_sum = find_max_subarray(A, mid, high)

    if left_sum > mid_sum and left_sum > right_sum:
        return left_low, left_high, left_sum
    elif mid_sum > left_sum and mid_sum > right_sum:
        return mid_low, mid_high, mid_sum
    else:
        return right_low, right_high, right_sum

