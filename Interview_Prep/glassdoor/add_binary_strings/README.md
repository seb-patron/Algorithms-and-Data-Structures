# Problem: Add Binary Strings  

**Note: Write a solution that does not use any built in string to int conversions or parsing tools.**

Given two binary strings, write a function that adds them. You are not allowed to use any built in string to int conversions or parsing tools. E.g. Given "100" and "111" you should return "1011". What is the time and space complexity of your algorithm?

### Solution Runtime

We transverse each element in the longest string
Runtime O(n) = n

Both strings are set to the length of the longest string, so n + n. End string is length n. So n + n + n
Space Complexity O(n) = 3n = n


### Solution

For simplicity's sake, make both strings equal length by adding 0's to the shortest string until it is equal length to the longest string.

Initiate a result string and a carry variable. Carry will hold a value that determines if we carry the one over.

Next, loop through each char in string1 in reverse order. If i at string1 is 1, increment the carry. If i at string2 is 1, increment the carry.

If the carry is divisible by 2, that means that the current result position is a 0. If it is not divisible by 2, it means only one of the chars at the current string positions is a 1, or both are 1 and we carried a 1 over from the previous result, and therefor we add a 1 to the result.

Finally, if our carry is less than 2, it means that we have nothing to carry over to the next iteration, so we reset carry to 0.
Else if our carry is 2 or greater, this means we have a carry, and we set carry to 1 for the next loop operation.

Finally, after our loop is done, we check if we have anything that needs to be carried over. If so, we add 1 to the front of our result. This basically accounts for edge cases where both strings end in 1.