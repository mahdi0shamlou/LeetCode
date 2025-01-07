class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        list3 = nums1 + nums2 # merge lists
        list3 = sorted(list3) # sort lists
        print(list3)
        mid = len(list3)/2
        print(f'mid is {mid}')
        print(f'mid is /2 {mid/2}')
        print(f'mid is /2 %2 {(mid / 2)%2}')

        if (len(list3))%2 == 0: # if number is not odd
            return (list3[int(mid)]+list3[int(mid-1)])/2
        else:
            return list3[int(mid)]

x = Solution()
r = x.findMedianSortedArrays([],[2,3])
print(f"resault is {r}")