import time
import random

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
            max_left_index = i
            max_left_sum = current_sum

    max_right_index = mid
    max_right_sum = float('-inf')
    current_sum = 0
    for i in range(mid+1, high+1):
        current_sum += A[i]

        if current_sum > max_right_sum:
            max_right_sum = current_sum
            max_right_index = i


    return max_left_index, max_right_index, max_left_sum + max_right_sum

def find_max_subarray(A, low, high):
    if low > high:
        return -1, -1, float('-inf')  # Handle invalid subarray
    elif low == high:
        return low, high, A[low]

    mid = (low + high) // 2

    # Corrected recursive call to include mid
    left_low, left_high, left_sum = find_max_subarray(A, low, mid)
    mid_low, mid_high, mid_sum = find_max_crossing_subarray(A, low, mid, high)
    right_low, right_high, right_sum = find_max_subarray(A, mid + 1, high)

    # Use >= to handle equal sums
    if left_sum >= mid_sum and left_sum >= right_sum:
        return left_low, left_high, left_sum
    elif mid_sum >= left_sum and mid_sum >= right_sum:
        return mid_low, mid_high, mid_sum
    else:
        return right_low, right_high, right_sum


def test_time():
    # 4.1-3
    for n in range(5, 15):
        random_list = [random.randint(-100, 100) for i in range(2**n)]
        start = time.time()
        maxium_sub_array_brute_force(random_list)
        end = time.time()
        print(f"Time taken for n = {n}: {end - start} (Brute Force)")

        random_list = [random.randint(-100, 100) for i in range(2**n)]
        start = time.time()
        find_max_subarray(random_list, 0, len(random_list) - 1)
        end = time.time()
        print(f"Time taken for n = {n}: {end - start} (Divide and Conquer)")

def linear_time_max_sub(A):
    if len(A) < 1:
        return -1, -1, 0

    curr_max_start = -1
    curr_max_end = -1
    curr_max = 0

    candidate_start = -1
    candidate_end = -1
    candidate_max = 0

    for i, num in enumerate(A):
        candidate_max += num
        if candidate_max < 0:
            candidate_start = -1
            candidate_end = -1
            candidate_max = 0
        else:
            if candidate_start == -1:
                candidate_start = i
            candidate_end = i

        if candidate_max > curr_max:
            curr_max = candidate_max
            curr_max_start = candidate_start
            curr_max_end = candidate_end

    return curr_max_start, curr_max_end, curr_max



if __name__ == '__main__':
    test_time()
