class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums1.extend(nums2)
        nums1 = sorted(nums1)
        ln = len(nums1)
        mid = int(ln/2)
        if ln%2 == 0:
            median = (nums1[mid-1] + nums1[mid])/2
        else:
            median = nums1[mid]
        
        return median

        
