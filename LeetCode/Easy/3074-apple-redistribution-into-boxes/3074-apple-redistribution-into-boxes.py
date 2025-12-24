class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        a = sum(apple)
        s =0
        for i in range(len(capacity)):
            s+= capacity[i]
            if s >= a:
                return i + 1
        