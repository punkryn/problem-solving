class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        s = list(s)

        r = n - 1

        st = []
        st2 = []
        ans = 0
        for l in range(n):
            if l >= r:
                break
            while l < r:
                if s[r] == ']':
                    st2.append(']')
                else:
                    if len(st2) == 0:
                        break
                    
                    if st2[-1] == '[':
                        break
                    
                    st2.pop()

                r -= 1
            
            if s[l] == '[':
                st.append('[')
            else:
                if len(st) == 0 or st[-1] == ']':
                    s[l], s[r] = s[r], s[l]
                    ans += 1

                    st.append('[')
                    st2.append(']')
                    r -= 1
                    continue
                
                st.pop()
        return ans