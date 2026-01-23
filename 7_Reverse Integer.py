class Solution:
    def reverse(self, x: int) -> int:
        
        reversed_x = 0
        sign = +1

        if "-" == x[0]:
            x = x[1:]
            sign = -1

        print(f"sign is : {sign}")
        
        for i in range(len(x)):
            pass
        
        return reversed_x * sign


x = Solution()
r = x.reverse(x = "-123")
print(r)