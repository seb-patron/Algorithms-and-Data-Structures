array = [1, 3, 2, 5, 8, 7, 6, 4]

def mergesort(array)
     if array.length > 1
          left_array = mergesort(array[0, array.length/2])
          right_array = mergesort(array[array.length/2, array.length])
     else
          return array
     end

     new_array = merge(left_array, right_array)
     return new_array
end

def merge(left_array, right_array)
     new_array = Array.new()
     i = 0
     j = 0
     k = 0
     while i < left_array.length && j < right_array.length
          if left_array[i] < right_array[j]
               new_array.push(left_array[i])
               i = i +1
          else
               new_array.push(right_array[j])
               j = j + 1
          end

          k = k + 1
     end


     
     new_array += left_array[i..-1]
     
     
     new_array += right_array[j..-1]

     return new_array
end

print mergesort(array)