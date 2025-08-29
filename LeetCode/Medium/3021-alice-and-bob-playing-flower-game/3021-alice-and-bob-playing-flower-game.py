class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # return  (n * m) // 2
        ans = 0
        for i in range(1,n+1):
            if i % 2:
                ans += m // 2
            else:
                ans += (m+1) // 2
        return ans