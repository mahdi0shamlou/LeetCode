class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        n = len(nums)

        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        best_sum_calc = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):

            left = i + 1
            right = n - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                # Update best_sum_calc
                if abs(total - target) < abs(best_sum_calc - target):
                    best_sum_calc = total

                # Move pointers
                if total < target:
                    left += 1

                elif total > target:
                    right -= 1

                else:
                    return total

        return best_sum_calc
        