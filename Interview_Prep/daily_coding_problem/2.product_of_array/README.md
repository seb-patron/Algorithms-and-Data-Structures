# Product of Array Except Self

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

### Easy Solution

Create a new list of the product of the entire list. This is done use a lambda function inside of a reduce function to find the product. This answer is then placed inside a list comprehension and made the same size as the original list.

Then, iterate over each element in the new list and divide it by the number in the original list in the same position.


# No Division Solution

First, we create a new list, called output, and a variable called product = 1

Then we iterate over the original list. At each iteration, we append the product of the previous portion of the list in the output list. This means that our final element in the list should be the product of the list except itself, and each element before it is the product of list minus the half of the list in front of it.

Once this is done, we reset product to 1.

Next, iterate backwards through the list, skipping the last element (since it is correct), we multiply the current list element with the product of the list in front of it. We keep track of this half of the lists product again using the product variable.