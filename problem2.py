## Problem 2:
"""

Given two strings s and t, determine if they are isomorphic.

https://leetcode.com/problems/isomorphic-strings/

Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.

Time Complexity: O(N)
Space Complexity: O(N)
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        d = {}
        d_inv = {}
        for char_s, char_t in zip(s, t):
            #if both key are not present in the dict
            if char_s not in d and char_t not in d_inv:
                d[char_s] = char_t
                d_inv[char_t] = char_s
            # if one key is in d dict but it does not matches
            elif char_s in d and d[char_s] != char_t:
                return False
            # if one key is in d dict but it does not matches
            elif char_t in d_inv and d_inv[ char_t ] != char_s:
                return False
            
        return True
