class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def go(depth, st, cur):
            if depth == n:
                cur += ')' * len(st)
                return [cur]
            
            ret = []
            st.append('(')
            ret += go(depth + 1, st, cur + '(')
            st.pop()

            if len(st) > 0:
                st.pop()
                ret += go(depth, st, cur + ')')
                st.append('(')
            return ret
        
        return go(0, [], '')