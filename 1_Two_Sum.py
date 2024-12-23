class Solution(object):
    def twoSum(self, nums, target):
        dict_key = {}
        for i in range(0, len(nums)):
            target_mines = target - nums[i]

            try:
                print(dict_key[str(target_mines)])
                print(i)
                return [dict_key[str(target_mines)], i]
            except:
                dict_key[str(nums[i])] = i