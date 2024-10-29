# Section 3

## 2.3-1
A = [3, 41, 52, 26, 38, 57, 9 ,49]  
[3, 41, 52, 26] [38, 57, 9 ,49]  
[3, 41] [52, 26] [38, 57] [9 ,49]  
[3] [41] [52] [26] [38] [57] [9] [49]   
[3, 41] [26, 52] [38, 57] [9, 49]  
[3, 26, 41, 52] [9, 38, 49, 57]  
[3, 9, 26, 38, 41, 49, 52, 57]

## 2.3-2
MERGE(A, p, q, r)  
...  
$let L[1..n_1] and R[1..n_2]$ be new arrays  
...  
i=1  
j=1  
k = p  
while i <= n_1 and j <= n_2  
> if L[i] <= R[j]
>> A[k] =  L[i]  
>> k++  
>> i++

> else
>> A[k] = R[j]  
>> k++  
>> j++

if i = n_1  
> while j <= n_2  
> > A[k] = R[j]  
> >k++  
> j++    

else  
> while i <= n_1
> >A[k] = L[i]  
> k++  
> i++  

## 2.3-3
Need to prove T(n) = n lg n. It means that the running time of n elements will be c * n lg n.  
base case:  
n = 2. T(2) = 2. T(2) = 2 lg 2 = 2 * 1 = 2  
inductive step:  
// continue from https://chatgpt.com/c/67104652-2b3c-800d-a9f3-e78cdf882619