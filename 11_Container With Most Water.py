class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
            i solve this problem with brute force then i reach to the time limit in leetcode and then switch to this one 
            consider some points if you write this code in c++ and test with that you reach 1ms 
        """
        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:

            width = right - left

            current_area = width * min(
                height[left],
                height[right]
            )

            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area