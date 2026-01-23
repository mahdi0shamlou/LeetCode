class Solution:
    def myAtoi(self, s: str) -> int:
        """
        first of all i think i can just jump empty section of s

        """
        # Step 1: Skip whitespaces
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1

        if i == n:
            return 0
        
        # Step 3: find sign
        sign = +1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        # Step 4: read the s for findig ints 
        result = 0
        INT_MAX_OF_OVERFELLOW = 2**31 - 1   # 2147483647
        INT_MIN_OF_OVERFELLOW = -2**31      # -2147483648
        
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            
            if result > (INT_MAX_OF_OVERFELLOW - digit) // 10:
                return INT_MAX_OF_OVERFELLOW if sign == 1 else INT_MIN_OF_OVERFELLOW
            
            result = result * 10 + digit
            i += 1
        
        
        return result * sign