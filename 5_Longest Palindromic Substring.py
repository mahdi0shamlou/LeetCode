class Solution:

    def check_is_string_is_palindromic(self, str):
        for i in range(0, len(str)):
            if str[i] != str[len(str)-1-i]:
                return False
        return True

    def longestPalindrome(self, s: str) -> str:
        """
        Given a string s, return the longest
        palindromic(A string is palindromic if it reads the same forward and backward) substring (A substring is a contiguous non-empty sequence of characters within a string)
        in s.
        :param s:
        :return:
        """
        max_len = 0
        final_res = ""
        for i in range(0, len(s)):
            list_str = ""
            for j in range(i, len(s)):
                list_str = list_str + s[j]
                if self.check_is_string_is_palindromic(list_str):
                    if len(list_str) > max_len:
                        max_len = len(list_str)
                        final_res = list_str
        return final_res


x = Solution()
res = x.longestPalindrome("cbbd")
print(res)