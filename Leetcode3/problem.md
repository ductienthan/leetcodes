Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Constraints:

0 <= s.length <= 105
s consists of English letters, digits, symbols and spaces.

reason to use sliding window

because we need to accumulate the length of substring
when stop the substring - when we see the first duplicate character.
what should be next move - There are 2 cases here

1. The duplicate is near the previous duplicate (fast - slow) == 1. then the slow should be the current fast one
2. If the duplicate is far from precious one, then the slow should be the previous duplicate + 1
   the condition to check if the char is consider as a duplicate if its position is in the range of fast and slow.

what should be the first start? start at 0,0

loop through the string

if the current chat is already in substring:

- need to move the slow to next char based on the last occurance because the last position definitely smaller than current fast one, because the duplicate is already there, so all of the char before that could be igore because the string will be end at current char
- update the slow index to the last duplicate data position +1
- Move the fast one to next

if the substring is still without duplciate
then checking current length compare with pervious max len, and then update max len
move the fast pointer

sliding window always move the faster pointer
