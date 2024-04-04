class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_set = set(positive_feedback)
        negative_set = set(negative_feedback)

        n = len(report)
        candidate = []
        for i in range(n):
            r = report[i]
            sid = student_id[i]
            score = 0
            for word in r.split():
                if word in positive_set:
                    score += 3
                if word in negative_set:
                    score -= 1
            
            candidate.append((score, sid))
        
        return map(lambda x: x[1], sorted(candidate, key=lambda x: (-x[0], x[1]))[:k])