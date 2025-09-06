import math

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        total_operations = 0
        
        for l, r in queries:
            operations = 0
            
            # Iterate over possible values of k (number of operations)
            k = 1
            while True:
                # Calculate the range of numbers requiring k operations
                lower = 4 ** (k - 1)  # Start of the range
                upper = 4 ** k - 1     # End of the range
                
                # If the lower bound exceeds r, break
                if lower > r:
                    break
                
                # Calculate the intersection of [l, r] and [lower, upper]
                intersect_l = max(l, lower)
                intersect_r = min(r, upper)
                
                # If there is an intersection, count the numbers and add to operations
                if intersect_l <= intersect_r:
                    count = intersect_r - intersect_l + 1
                    operations += count * k
                
                # Move to the next group
                k += 1
            
            # Each operation processes two numbers, so divide by 2 and round up
            total_operations += (operations + 1) // 2
        
        return total_operations
