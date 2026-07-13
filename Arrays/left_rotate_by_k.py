class Solution:
    def rotateArray(self, nums, k):
        n = len(nums)

        if n == 0:
            return

        k %= n
        # function to reverse a portion of the array
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Reverse first k elements
        reverse(0, k - 1)

        # Reverse remaining elements
        reverse(k, n - 1)

        # Reverse the entire array
        reverse(0, n - 1)