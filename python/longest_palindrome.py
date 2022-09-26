"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"

"""

def longest_palindrome(s):
	longest = ""
	for i in range(len(s)):
		l = r = i
		while l >= 0 and r < len(s) and s[l] == s[r]:
			if  r - l +1 > len(longest):
				longest = s[l:r+1]
			l -= 1
			r += 1
		l, r = i, i+1
		while l >= 0 and r < len(s) and s[l] == s[r]:
			if r - l + 1 > len(longest):
				longest = s[l:r+1]
			l -= 1
			r +=1
	return longest

print(longest_palindrome('bbcbc'))