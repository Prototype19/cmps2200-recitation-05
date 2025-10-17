# CMPS 2200 Reciation 5
## Answers

**Name:** Daron Lebaredian

Place all written answers from `recitation-05.md` here for easier grading.







- **1b.**


Sorted:

|     n |   qsort-fixed-pivot |   qsort-random-pivot |   tim_sort |
|-------|---------------------|----------------------|------------|
|   100 |               1.826 |                0.335 |      0.002 |
|   200 |               7.689 |                0.673 |      0.003 |
|   500 |              39.479 |                1.946 |      0.006 |
|  1000 |             128.148 |                4.209 |      0.011 |
|  2000 |             499.065 |                8.880 |      0.018 |
|  5000 |            2767.687 |               23.452 |      0.058 |
| 10000 |           11035.585 |               63.287 |      0.160 |

Unsorted/Shuffled:

|      n |   qsort-fixed-pivot |   qsort-random-pivot |   tim_sort |
|--------|---------------------|----------------------|------------|
|    100 |               0.333 |                0.414 |      0.010 |
|    200 |               0.618 |                0.748 |      0.018 |
|    500 |               1.822 |                2.141 |      0.049 |
|   1000 |               4.092 |                4.750 |      0.105 |
|   2000 |              11.077 |               11.695 |      0.258 |
|   5000 |              27.582 |               27.039 |      0.644 |
|  10000 |              56.965 |               55.842 |      1.463 |
|  20000 |             112.609 |              130.353 |      3.023 |
|  50000 |             342.576 |              387.933 |     10.146 |
| 100000 |             794.226 |              762.276 |     22.886 |

The Reason why I removed some value list sizes when compairing the functions with sorted lists is because for the qsort-fixed-pivot the sorted list is its worse time case so it take a super long time for it to sort larger lists.

With the sorted lists the fixed pivot qsort is both O(n) work and span; this is because of it all of the left recursive call's inputs are empty lists because all of the pivot points are by defintion the smallest elements no element can be smaller than it. This makes the fixed pivot qsort identical to a iterator funcion. The random pivot qsort on the otherhand has a much more logarithmic span; it is much more work efficient than the fixed point. This is likely due to the fact is can split the work between the recursive calls, leading to a lower span and more possible parrelization.

With the unsorted lists, both the fixed point pivot and random pivot qsorts have similar times, logarithmic. In this case the fixed point qsort is basically the same thing as the random pivot qsort because the chances of the first element being the largest, smallers, or some other elemnent is equally possible, just like with the random pivot. The interesting thing is that the random pivot qsort working on the unsorted list was much less time efficient than with the sorted list. 

Both 

- **1c.**

Look at the graphs above for the times of tim_sort. You can see tim_sort is much faster tha both fixed and random pivot qsort algorithmns, likely O(log(n)) work some asympotic notation with a lower bound.


