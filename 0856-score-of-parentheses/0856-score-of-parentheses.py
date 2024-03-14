class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n = len(s)
        st = []
        for i in range(n):
            if s[i] == '(':
                st.append(0)
            else:
                if st[-1] == 0:
                    st[-1] = 1
                else:
                    curSum = 0
                    while len(st) > 0 and st[-1] > 0:
                        curSum += st.pop()
                    st[-1] = curSum * 2
        return sum(st)