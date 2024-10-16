def insertion_sort(arr):
    for i in range(1, len(arr)):
        value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > value:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = value


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        if min_idx != i:
            temp = arr[i]
            arr[i] = arr[min_idx]
            arr[min_idx] = temp
            
def merge_sort(arr):
    def merge_sort_helper(arr, p, r):
        def merge(arr, p, q, r):
            pass
        pass
    merge_sort_helper(arr, 0, len(arr))
        
        