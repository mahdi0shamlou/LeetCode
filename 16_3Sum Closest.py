class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        n = len(nums)

        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]


        