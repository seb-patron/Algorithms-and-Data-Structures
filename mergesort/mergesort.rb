
# recursive call
# if length of array > 1:
#     mergeSort(1st half), mergeSort(2nd half)
# else
#     return array
# then
#     merge split arrays
#     return new merged array
def mergesort(array)
     if array.length < 2
          return array
     end
     left_array = mergesort(array[0, array.length/2])
     right_array = mergesort(array[array.length/2, array.length])

     new_array = merge(left_array, right_array)
     return new_array
end

# create new array
# vars i, j = 0
# while i < left array length AND j < right array length
#     check if left array @ i < right array @ j
#         append left array @ i to new array
#         i++
#     else
#         append right array @ j to new array
#         j++
# append remaining array elements to new array
# return new array
def merge(left_array, right_array)
     new_array = Array.new()
     i = 0
     j = 0
     while i < left_array.length && j < right_array.length

          if left_array[i] < right_array[j]
               new_array.push(left_array[i])
               i = i +1
          else
               new_array.push(right_array[j])
               j = j + 1
          end

     end

     # add remaining elements to new array
     new_array += left_array[i..-1]
     new_array += right_array[j..-1]
     return new_array
end


array = [1, 3, 2, 5, 8, 7, 6, 4]
print mergesort(array)