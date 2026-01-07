class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start = 0
        end = 0
        
        def expand_around_center_v2(left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1
        
        for i in range(len(s)):
            
            # Case 1: Odd length palindrome (center is a single character)
            # Example: "aba" → center at 'b'
            l1, r1 = expand_around_center_v2(i, i)
            
            # Case 2: Even length palindrome (center is between two characters)
            # Example: "bb" → center between the two 'b's
            l2, r2 = expand_around_center_v2(i, i + 1)
            
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
                
            print(f"start : {start} and end : {end}")
            print("#" * 100)
        
        return s[start:end + 1]


x = Solution()
res = x.longestPalindrome("cbbd")
print(res)
