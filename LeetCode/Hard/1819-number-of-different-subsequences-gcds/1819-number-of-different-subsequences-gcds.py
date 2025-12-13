import math

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: list[int]) -> int:
        # Initialize array with size 200001, similar to the Java int[200001]
        factor = [0] * 200001
        
        for num in nums:
            # Find all factors of num
            j = 1
            while j * j <= num:
                if num % j == 0:
                    factor1 = j
                    factor2 = num // j

                    # Find gcd of all nums having factor1 as a divisor
                    # Note: math.gcd(0, x) returns x, so initialization to 0 works perfectly
                    factor[factor1] = math.gcd(factor[factor1], num)
                    
                    # Find gcd of all nums having factor2 as a divisor
                    factor[factor2] = math.gcd(factor[factor2], num)
                j += 1
        
        ans = 0
        # Check if factor[i] equals i
        for i in range(1, 200001):
            if factor[i] == i:
                ans += 1
                
        return ans