class Solution:
    def reverse(self, x: int) -> int:

        reversed_x = 0 # create reverse_x to return 

        # Try to Handle the sign separately
        if x >= 0:
            sign = 1
        else:
            sign = -1

        x = abs(x)
        
        while x > 0:
            digit = x % 10
            x = x // 10
            
            # checks for overflow before adding the new digit
            # 2**31 - 1 is equals = 2147483647
            # -2**31    is equals = -2147483648

            if reversed_x > (2147483647 - digit) // 10: # but you can use dynamic number calculation like 2**31-1
                return 0
            if reversed_x < (-2147483648 + digit) // 10:
                return 0
                
            reversed_x = reversed_x * 10 + digit
        
        return sign * reversed_x