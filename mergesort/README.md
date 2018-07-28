# Mergesort

Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.


#### Pseudocode

```
mergesort(array)
    if length of array > 1:
         sort(1st half), mergeSort(2nd half)


 sort:
    c = outputArray a = 1st sorted Array(n/2) b = 2nd sorted Array(n/2)

    i = 1; j = 1
    for k = 1 to n
         if a(i) < b(j):
              c(k) = a(i)
              i++
         else if a(i) > b(j)
              c(k) = b(j)
              j++
    end
     c += remainder of a
     c += remainder of b

    return c
```