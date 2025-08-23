class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:  # Add this edge case check
            return 0
            
        l, r = 0, len(height) - 1
        leftmax, rightmax = height[l], height[r]
        res = 0
        
        while l < r:
            if height[l] < height[r]:
                if height[l] >= leftmax:
                    leftmax = height[l]
                else:
                    res += leftmax - height[l]
                l += 1
            else:
                if height[r] >= rightmax:
                    rightmax = height[r]
                else:
                    res += rightmax - height[r]
                r -= 1
                
        return res