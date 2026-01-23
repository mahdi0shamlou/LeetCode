class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
            first of all i think change x from int to str 
            secend i think i can find center of str and expand around the center with consider odd or even x_str
            three if any one of them is not equal we can return False else return True 
        """
        x_str = str(x)
        x_is_palindrome = False   
        
        print(f"x : {x_str} and type : {type(x_str)}")

        if len(x_str) % 2 == 0:
            
            print(f"x is even and len is : {len(x_str)}")
            mid_of_str_num = len(x_str) / 2

            left = mid_of_str_num - 1
            right = mid_of_str_num 
            print(f"left for start is : {left}")
            print(f"right for start is : {right}")
            while left >= 0 and right < len(x_str) and x_str[int(left)] == x_str[int(right)]:
                left -= 1
                right += 1

            left = left + 1 
            right = right - 1
            
            print(f"left in end is : {left}")
            print(f"right in end is : {right}")

            return (left == 0) and (right == len(x_str)-1) 

        else:
            pass
        
        mid_of_str_num = len()

        return x_is_palindrome


x = Solution()
res = x.isPalindrome(x=1221)
print(res)
