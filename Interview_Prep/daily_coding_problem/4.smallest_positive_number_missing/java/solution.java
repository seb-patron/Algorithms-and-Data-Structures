// import static java.lang.System;
import java.util.Arrays;

class Solution {
     public static void main(String[] args) {
          System.out.println("Hello World!");
          Solution solution = new Solution();
          int arr[] = {1,2,0};
          int x = solution.firstMissingPositive(arr);

          System.out.println("answer =" + x + ", should be 3");

          int arr2[] = {7,8,9,11,12};
          x = solution.firstMissingPositive(arr2);

          System.out.println("answer=" + x +", should be 1");
    }

    public int firstMissingPositive(int[] nums) {
        int n = nums.length;
        if (n == 0) {
            return 1;
        }
        int k = partition(nums, n); //all negs should be at k..length
        int temp = 0;
        int first_missing_index = k; // our first missing number is where our array becomes negative
        
        // if a number exists, set its index to negative 
        for (int i = 0; i < k; i++) {
            temp = Math.abs(nums[i]);
            if(temp<=k && temp != 0) {
                if (nums[temp-1] < 0) nums[temp-1] = nums[temp-1];
                else nums[temp-1] = -nums[temp-1];
           }
            
        }
        
        // all existing numbers should be negative
        // any missing numbers should be positive
        // now just perform a linear scan to find the first positive number
        for (int i = 0; i < k; i++) {
            if (nums[i] > 0){
                first_missing_index = i;
                break;
            }
        }
        return first_missing_index + 1;
    }
    
    public int partition(int[] nums, int length) {
          int j = 0;
          for (int i = 0; i < length; i++) {
               if (nums[i] > 0) {
                    swap(nums, i, j);
                    j++;
               }
          }
          // at end of loop j will be index of first negative number
          return j-1;
    }
    
    public void swap(int[] nums, int i, int j) {
        if (i != j){
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
}