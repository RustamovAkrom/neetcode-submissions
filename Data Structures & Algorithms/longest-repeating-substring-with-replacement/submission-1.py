class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = maxf = res = 0

        for right, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            maxf = max(maxf, count[c])

            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res