
## Problem 1:
"""
Given an array of strings, group anagrams together.
https://leetcode.com/problems/group-anagrams/
Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
All inputs will be in lowercase.
The order of your output does not matter.

Time: Complexity: O(m*n * 26)
n = size of input provided
m = avg size of each word

Space Complexity: O(n)

"""

class Solution:
    def get_tuple_word(self, word):
        #get 26 charcter array for each word and return it
        tup = [ 0 for i in range(26)]
        
        for char in word:
            tup[ ord(char) - ord('a') ] += 1
            
        return tuple(tup)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d  = {}
        
        for word in strs:
            tup = self.get_tuple_word(word)
            #find if 26 char array is in the dict (Hashmap), if not, add the entry
            if tup not in d:
                d[tup] = []
            d[tup].append(word)
            
        output = []
        for v in d.values():
            output.append( v )
        
        return output