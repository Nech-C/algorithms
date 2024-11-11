# section 3
## 4.3-1
show that $T(n) = T(n-1) + n $ is $O(n^2)$  
$T(n) <= cn^2$  
$T(n) = T(n-1) + n$   
$T(n) \le c(n-1)^2 + n$   
$T(n) \le cn^2 -2cn + c + n$  
$T(n) \le cn^2 -(2c+1)n + c$  
we just need to show that c - (2c+1)n <= 0.

let c - (2c+1)n <= 0  
$c <= (2c+1)n$  
$\frac{c}{2c+1} \le n$

as long as $\frac{c}{2c+1} \le n$, the induction holds.