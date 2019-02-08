# Problem: First Non Repeated Char In String

**Note: Write a solution that only iterates over the string once and uses O(1) additional memory, since this is what you would be asked to do during a real interview.**

Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

### Example

For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
firstNotRepeatingCharacter(s) = '_'.

There are no characters in this string that do not repeat.

### Input/Output



A string that contains only lowercase English letters.

Guaranteed constraints:
1 ≤ s.length ≤ 105.

[output] char

The first non-repeating character in s, or '_' if there are no characters that do not repeat.


### Solution

There are two important components to the solution: the input is always a lower case string, and the characters are between the range of a-z.

We know that there are 26 characters in the alphabet. So we can make two lists of length 26th, aka char_list and char_sequence. We initialize both lists with 0's.

The char_list is a count of the number of times that a character appears in a string. Each index corresponds to that letter's position in the alphabet, ie a=0, b=1, c=2,..., z=26. 

char_sequence represents the order of the first appearance of a character in a string. So when we find a for the first time, we'll append it to our char_sequence.

In short, we'll go through each letter in the string. We'll find that letter's position in the alphabet and increment it by one. If its the first time we found it in the string, we'll add it to char_sequence.

Once we have transversed the string, we'll iterate through the char_sequence list. We'll cross check that letter's frequency count in the char_list list. If it is 1, we'll return it. If we don't find a char that == 1, we'll return '_'.

char_list is O(26) = O(1)
char_sequence is O(1..26)  = O(1)

Space complexity is therefor O(1)

We transverse the list once, so O(n)
transversing the char_sequence list is max O(26), so O(1)

Our runtime complexity is O(1)