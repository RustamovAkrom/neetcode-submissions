from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = {}
        left = formed = 0
        res = ""
       
        for right, c in enumerate(s):
            have[c] = have.get(c, 0) + 1
            if c in need and have[c] == need[c]:
                formed += 1
            
            while formed == len(need):
                if not res or right - left + 1 < len(res):
                    res = s[left:right + 1]
                c = s[left]
                have[c] -= 1

                if c in need and have[c] < need[c]:
                    formed -= 1
                left += 1
        return res