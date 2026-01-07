class Solution(object):
    def twoSum(self, nums, target):
        dict_key = {}
        
        for i, num in enumerate(nums):
            target_less = target - num

            if target_less in dict_key:
                return [dict_key[target_less], i]
            
            dict_key[num] = i