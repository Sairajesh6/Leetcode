class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        sums_lens = []
        prev_len = 0
        cur_len = 0
        for num in nums:
            if num == 1:
                cur_len += 1
            else:
                sums_lens.append(prev_len + cur_len)
                prev_len = cur_len
                cur_len = 0
    
        sums_lens.append(prev_len + cur_len)
        res = max(sums_lens)
        if len(sums_lens) == 1:
            res -= 1
        return res