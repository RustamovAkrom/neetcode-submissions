from typing import List

class Solution:
    def maxArea(self, h: List[int]) -> int:
        l, r, ans = 0, len(h) - 1, 0
        while l < r:
            ans = max(ans, min(h[l], h[r]) * (r - l))
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
        return ans
        # left = 0
        # right = len(heights) - 1
        # max_water = 0

        # while left < right:
        #     width = right - left
        #     height = min(heights[left], heights[right])

        #     max_water = max(max_water, width * height)

        #     if heights[left] < heights[right]:
        #         left += 1
        #     else:
        #         right -= 1
        # return max_water