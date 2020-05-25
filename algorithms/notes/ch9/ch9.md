# chpater 9

## 9.1 minimun and maximum

### minimum or maximum

O(h) = n-1
- every element needs to be compared, at least once

### minumum and maximum
O(h) = 2 * (n -1)

More efficient:
2 elements everytime  => n/2
compare with each other and smaller compare to minimum, larger compare to maximum => * 3

O(h) = 3 * (n/2)

### Q1 (to solve)

2 => 1, 1
3 => first two (1) + compare to min + compare to max => 3, 3+2-2 = 3
4 => first two (1) + 2 * (compare to min, compare to max) => 5, 4 + 2 -2 = 4
5 => 1 + 2 * 3 => 7, 5 + 3 -2 = 6
6 => 1 + 2 * 4 => 9, 6 + 3 -2 = 7


solution: divid and min, find the minumum, remember all the losers, trace back


get min:
T(n) = 2 * T(n/2) + 1
     = 2 * (2 * T(n/4) + 1) + 1
     = 2 ** lg(n/2) * T(2) + 2**lg(n/4) + 2**g(n/8) + .... + 1
     = n/2 + n/4 + n/8 + .... 1
     = n


T(n) = 2 * T(n/2) + 2
     = 2 * (2 * T(n/4) + 2 ) + 2
     = 2 ** lg(n/2) * T(2) + 2**lg(n/2) + 2** lg(n/4) + .... + 2
     = n/2 + n/2 + n/4 + n/8 + ... + 2
     =



##  9.2 linear expected time for arbitrary rank of number

quick sort but only do the sorting on one side
 - n + n/2 + n/4 + ... + 1 < 2n if evenly splitted,
 - n + n-1 + n-2 + ... + 1 < n(n+1)/2 in worst case
 - since random split, not possilbe, so this is lower bound

 expectaton O(T) = theta(n)

### Q 9.2-3


while p > r:
    q = partition(Arr, p, r)
    k = q - p + 1

    if i == k:
        return A[q]
    if i < k:
        r = q - 1
        random_select(Arr, p, r, i)
    else:
        p = q + 1
        i = i - k
        random_select(Arr, p, r, i)


### Q 9.2-4
9, 8, 7, ...


## 9.3

linear time for find the ith minimum/maximum element

SELECT
1. n/5 groups
2. insert sort in each, find the n/5 medians
3. find the median of n/5 medians, by recursively calling SELECT
4. partition with median x, arr => 0:x, x+1:n
5. if i==k, return, if i < k: SELECT(0:x); else: SELECT(x+1:n)


### Q 9.3-1
7 yes: T(n) = cn + (8c + an -cn/7) < cn so if cn/7 > 8c + an
3 not: T(n) = cn + (4c + an) > cn so ω(n)


### Q 9.3-2
if n >140: 3n/10 -6 = (3n - 60)/10 > (3n - 0.5n) / 10 = n/4

### Q 9.3-3
find the median first: cn + nlog(n)

### Q 9.3-4
know min ith, do we know min i-1, and max n-i

max n-i => min i+1:
  1,2,3,4,5 => min 2 = max 4
  1,2,3,4,5,6 => min 2 = max 5

if only by compare, know i th is ith, must compared with i-1 and i+1

### Q 9.3-5
implemented in middle_number

### Q 9.3-6
implement the k-quantile

### Q 9.3-7
- first find median n/2
- find n/2 -  k/2
- find n/2 + k/2
- take elements in between

### Q 9.3-8
take each element from the side is smaller, untill one side is empty, get median, 2n - 1

### Q 9.3-9
find the median, i.e. equal number of oil wells on each side is the minimum

# final

### Q1
- sort: n log(n)
- heap: n + log(n) * i
- ith maximum: O(n)

### Q2
- a:
    (n/2 -2) ... n/2-1... n/2 if even
    (n-2/2 ) ... (n-1)/2 ... (n+1)/2 if odd

- b: sort then sum(i+1) = sum(i) + x(i+1), until sum > 0.5

- c: medium, summation, and then partition again

- d: same a oil wells

- e: x, y independet, find the median for x and y

### Q3
??

### Q4
??
