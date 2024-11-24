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
        
def heap_sort(arr):
    class Min_heap():
        def __init__(self, arr):
            self.arr = []
            for i in arr:
                self.insert(i)
            print(self.arr)
        def pop(self) -> int:
            min_num = self.arr[0]
            self.arr[0] = self.arr[-1]
            self.arr.pop()
            self._bubble_down()
            return min_num

        def peek(self) -> int:
            return self.arr[0]

        def insert(self, num: int):
            self.arr.append(num)
            self._bubble_up()
        
        def _bubble_up(self):
            idx = len(self.arr) - 1
            while idx > 0:
                parent = (idx - 1) // 2
                if self.arr[idx] < self.arr[parent]:
                    self.arr[idx], self.arr[parent] = self.arr[parent], self.arr[idx]
                    idx = parent
                else:
                    break

        def _bubble_down(self):
            n = len(self.arr)
            index = 0
            arr = self.arr
            while True:
                left = 2 * index + 1
                right = 2 * index + 2
                smallest = index

                if left < n and arr[left] < arr[smallest]:
                    smallest = left

                if right < n and arr[right] < arr[smallest]:
                    smallest = right

                if smallest == index:
                    break

                arr[index], arr[smallest] = arr[smallest], arr[index]

                index = smallest

    min_heap = Min_heap(arr)

    for i in range(len(arr)):
        arr[i] = min_heap.pop()

