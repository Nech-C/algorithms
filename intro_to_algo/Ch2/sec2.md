## Section 2.2
### 2.2-1 $\Theta(n^3)$

### 2.2-2 The loop invariant is that the subarry arr[0..i] is sorted. For an array with one element, it's already sorted. Best case: $\Omega(n^2)$. Worst case: $\Theta(n^2)$

### 2.2-3 On average, half of the sequence need to be checked. In the worst case, all elements need to be checked.Best-case: $\Theta(1)$. Worst-case: $\Theta(n)$. In the best-case, the target element is the first element, so only a constant time is required. In the worst-case, the target element is the last element or the tartet element is not in the array, so it has to search all *n* elements.

### 2.2-4 We can add a check at the beginning of the algorithm to see if the input is already in the desired state.
