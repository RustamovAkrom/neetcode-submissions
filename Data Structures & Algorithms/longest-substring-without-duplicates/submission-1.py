class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = res = 0

        for right, c in enumerate(s):
            while c in seen:
                seen.remove(s[left])
                left += 1
            seen.add(c)
            res = max(res, right - left + 1)
        return res