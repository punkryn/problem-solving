class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        curString = ''
        blockFlag = False
        tmp = ''
        for line in source:
            for alpha in line:
                if blockFlag:
                    tmp += alpha
                    if len(tmp) >= 4 and tmp[-2:] == '*/':
                        blockFlag = False
                        tmp = ''
                    continue

                curString += alpha
                if len(curString) >= 2 and curString[-2:] == '//':
                    curString = curString[:-2]
                    break
                
                if len(curString) >= 2 and curString[-2:] == '/*':
                    blockFlag = True
                    curString = curString[:-2]
                    tmp += '/*'
                    continue
                
            if not blockFlag:
                if curString != '':
                    ans.append(curString)
                curString = ''

        return ans