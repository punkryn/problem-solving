class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        a = max(milestones)
        b = sum(milestones)
        c = b - a

        if a - 1 <= c:
            return b

        return c * 2 + 1