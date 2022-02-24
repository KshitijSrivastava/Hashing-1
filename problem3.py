## Problem 3:
"""
https://leetcode.com/problems/word-pattern/

Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:
Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

Time Complexity: O(n)
n = number of words in s string
Space Complexity: O(2 * n) _. To maintain two dict
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_lst = s.split(" ")
        
        if len(s_lst) != len(pattern):
            return False
        n = len(pattern)
        
        word_d = {}
        d = {}
        i = 0
        while i < n:
            # if pattern word not in dictionary
            if pattern[i] not in d and s_lst[i] not in word_d:
                d[ pattern[i] ] = s_lst[i]
                word_d[ s_lst[i] ] = pattern[i]
            #if pattern word in dict and current word not equal to current word
            elif pattern[i] in d and d[ pattern[i] ] != s_lst[i]:
                return False
            # if word is in the dict and current word does not match the pattern
            elif s_lst[i] in word_d and word_d[s_lst[i]] != pattern[i]:
                return False
            
            i += 1
            
        return True