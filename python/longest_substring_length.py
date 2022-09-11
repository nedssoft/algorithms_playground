
"""
Given a string s, find the length of the longest substring without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        d = {}
        i = 0
        res = 0
        for j in range(n):
            char = s[j]
            if char in d:
                i = max(i, d[char])
            res = max(res, j - i + 1)
            d[char] = j + 1
        return res


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))