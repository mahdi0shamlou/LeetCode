class Solution(object):

    def lengthOfLongestSubstring(self, s):
        max_len = 0
        lists = []
        for i in range(0, len(s)):
            for z in range(i, len(s)):
                if s[z] in lists:
                    lists = []
                    break
                else:
                    lists.append(s[z])

                if max_len < len(lists):
                    max_len = len(lists)

        return max_len



x = Solution()
r = x.lengthOfLongestSubstring("abbcds")
print(r)
r = x.lengthOfLongestSubstring("abcabc")
print(r)
r = x.lengthOfLongestSubstring(" ")
print(r)
r = x.lengthOfLongestSubstring("")
print(r)
r = x.lengthOfLongestSubstring("aabbccc")
print(r)
r = x.lengthOfLongestSubstring("dvdf")
print(r)
