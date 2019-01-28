# Input:  set[] = {3, 34, 4, 12, 5, 2}, sum = 9
# Output:  True  //There is a subset (4, 5) with sum 9.

# A recursive solution for subset sum 
# problem 
  
# Returns true if there is a subset  
# of set[] with sun equal to given sum 
class Subsetsum:
    def __init__(self, array):
        self.set = array

    def subsetsum(self, sum):
        return self.isSubsetSum(self.set, sum)

    def isSubsetSum(self, set, sum):
        if sum < 1: return None
        if len(set) == 0: return None


        if set[0] == sum:
            return [set[0]]
        else:
            subset = self.isSubsetSum(set[1:],(sum - set[0]))
            if subset:
                return [set[0]] + subset
            else:
                return self.isSubsetSum(set[1:], sum)



# array = [3, 34, 4, 12, 5, 2] 
# sum = 9
# if (isSubsetSum(array, sum) != None) : 
#     print("Found a subset with given sum", (isSubsetSum(array, sum)))
# else : 
#     print("No subset with given sum") 