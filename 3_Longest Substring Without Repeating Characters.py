class Solution(object):
    def lengthOfLongestSubstring(self, s):
        list_numbers = []
        max_len = 0
        for i in range(0,len(s)):
            if s[i] in list_numbers:
                if max_len < len(list_numbers):
                    max_len = len(list_numbers)
                list_numbers = [s[i]]
            else:
                list_numbers.append(s[i])

        return max_len

x = Solution()
r = x.lengthOfLongestSubstring("abcabcbb")
print(r)