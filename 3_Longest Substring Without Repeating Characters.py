from measure_execution_time import timing_decorator

class Solution(object):

    @timing_decorator
    def lengthOfLongestSubstring_old_version(self, s):
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
    

    @timing_decorator
    def lengthOfLongestSubstring(self, s):
        last_seen = {}
        left = 0
        max_len = 0
        
        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1
                
            last_seen[char] = right
            max_len = max(max_len, right - left + 1)
            
        return max_len


x = Solution()

r = x.lengthOfLongestSubstring_old_version("dvdfaksndasd"*11000)
print(r)

r = x.lengthOfLongestSubstring("dvdfaksndasd"*11000)
print(r)
