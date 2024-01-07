class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        dic = dict()
        
        for i in range(len(groupSizes)):
            s = groupSizes[i]
            if s not in dic:
                dic[s] = []
            
            dic[s].append(i)

            if len(dic[s]) == s:
                ans.append(dic[s])
                dic[s] = []
            
        return ans
            