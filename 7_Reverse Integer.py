class Solution:

    def reverse(self, x: int) -> int:
        print("*"*30)
        print(f"x for start : {x}")

        reversed_x = 0
        sign = +1

        if "-" == x[0]:
            x = x[1:]
            sign = -1

        print(f"sign is : {sign}")
        print(f"x befor revese x : {x}")

        for i in range(len(x), 0, -1):
            if reversed_x == 0:
                reversed_x = int(x[i-1])
            else:
                reversed_x = (reversed_x*10) + int(x[i-1])

            if (reversed_x * sign) > ((2**31)-1) or (reversed_x * sign) < ((2**31) * -1):
                return 0
        
        return reversed_x * sign


x = Solution()
r = x.reverse(x = "-123")
print(r)
r = x.reverse(x = "-123000")
print(r)
r = x.reverse(x = "-10023")
print(r)
r = x.reverse(x = "120")
print(r)