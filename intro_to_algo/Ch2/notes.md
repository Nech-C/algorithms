## 2.3 Designing algorithms

### 2.3.1 The divide-and-conquer approach

Divide: We divide the problem into subproblems that have the same properties as the entire problem.

Conquer: We recursively solve those subproblems. When the subproblem is small enough, we can solve them directly.

Combine: We combine the solved subproblems to form the answer to the original problem.

#### Merge sort
The Merge sort algorithm is an example of the divide-and-conquer approach. It divides an array into smaller subarrays recursively and works bottom up by combining sorted arrays to sort the entire array.  
The Merge procedure is the core of the algorithm. Merge(A, p, q, r) takes an array $A$, the starting index of the left array $p$, the end of the left array $q$, and the end of the right array $r$. Elements in A[p..q] and A[q+1..r] are already in sorted order. It runs a for loop to fill A[p..r] with elements in     sorted order from the two arrays.  
We again use a loop invariant to prove the correctness of the procedure:
```
    At the start of the each iteration of the for loop, the subarray A[p..k-1] contains the smallest k-p elements from L[] and R[], in sorted order. L[i] and R[j] are the smallest elements of their array that have not been copies into A[].
```
Initialization: Prior to the loop, A[p..k-1] contains no element since p=k, which means that it contains 0 smallest elements from L and R. We know that at initialization, L and R are sorted, and therefore, L[i] and R[j] for i = j = 1 contains the smallest elements of L and R.  

Maintenanc: At the start of the iteration, we can assume that the loop variant holds. If $L[i] \leq R[j]$, the algorithm moves L[i] to A[k]. After incrementing i and k, the loop invariant is reestablished. The loop invariant holds. The proof is similar when $L[i] > R[j]$

Termination: When the loop terminates, k = r + 1. A[p..k-1] will containt k - p = r + 1 - p elements which includes all elements from p to r in sorted order. 

### 2.3.2 Analyzing divide-and-conquer algorithms
When an algorithm contains a recursive call to itself, we can often describe its
running time by a recurrence equation or recurrence, which describes the overall
running time on a problem of size n in terms of the running time on smaller inputs.You're absolutely right. 

$$
T(n) = \begin{cases}
    \Theta(1) & \text{if } n \leq c \\
    aT(n/b) + D(n) + C(n) & \text{otherwise}
\end{cases}
$$
where T(n) is the time needed to run the algo for input size of n. $a$ is the number of subproblems created during division, $1/b$ is the input to each subproblem(new size), D(n) is the time to divide the problem into subs, and C(n) is the time to combine the solutions to the subproblems.

#### Analysis of merge sort
Divide: The divide step just computes the middle of the subarray, which takes
constant time. Thus, $D(n)=\Theta(1)$.  
Conquer: We recursively solve two subproblems, each of size n=2, which contributes $2T(n/2)$ to the running time.  
Combine: We have already noted that the MERGE procedure on an n-element
subarray takes time $C(n)=\Theta(n)$.

$$
T(n) = \begin{cases}
    \Theta(1) & \text{if } n = 1, \\
    2T(n/2) + \Theta(n) & \text{if } n > 1.
\end{cases} \tag{2.1}
$$

Here is the recursion tree:

```
(a)         (b)              (c)
T(n)        cn               cn  
            / \             /   \  
                          cn/2  cn/2  
                          / \   / \  
                        T(n/4) T(n/4)  

(d)
     cn -----------------> cn
    /  \
  cn/2  cn/2 ------------> cn
  /  \   /  \
cn/4 cn/4 cn/4 cn/4 -----> cn
 |    |    |    |
 .    .    .    .
 .    .    .    .
 c    c    c    c  ...  c  c --> cn
\___________________________/
            n

Total: cn lg n + cn
```

We can see that each level costs cn, and it has lg(n) + 1 levels(the height is lg(n)). Thus, the total cost is cn(lg(n) + 1) = cnlg(n) + cn, which is $\Theta(nlg(n))$