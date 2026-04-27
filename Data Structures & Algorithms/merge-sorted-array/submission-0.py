class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = m - 1
        right = m + n - 1
        k = n - 1

        while left > -1 and right > left and k > -1:
            if nums1[left] > nums2[k]:
                nums1[right] = nums1[left]
                left -= 1
            else:
                nums1[right] = nums2[k]
                k -= 1
            right -= 1

        while k > -1 and right > -1:
            nums1[right] = nums2[k]
            k -= 1
            right -= 1