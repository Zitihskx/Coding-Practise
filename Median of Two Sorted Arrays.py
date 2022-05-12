class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        
        nums = nums1 + nums2
        merged = nums1 + nums2
        merged.sort()
        length = int(len(merged))
        if length % 2 == 0:
            res = (float(merged[length/2]) + float(merged[(length/2)-1]))/2
            return(res)
        else:
            return(merged[(length-1)/2])
