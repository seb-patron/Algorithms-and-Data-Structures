# Problem 1 [Easy]: Sub Sum in Array

Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

### Solution

Create a hashmap. Then iterate through the array. For each number in the array, subtract it from the target. If the difference is in the hashmap, return true.

If the difference is not in the hashmap, put the original number as a key in the hashmap, with the corresponding result being anything you want (true in this case).

Note if the problem were to say what are the indexes of the numbers that add up to the target, you could store the index as the value in the hashmap instead.

Example:

nums=[3, 2, 4], target=6

first iteration, 6-3 = 3, 3 is not in the hashmap, so hashmap = {3: true}
second iteration, 6 - 2 = 4, 4 is not in the hashmap, so hashmap = {3: true, 2: true}
third iteration, 6 - 4 = 2, 2 is in the hashmap, so return true