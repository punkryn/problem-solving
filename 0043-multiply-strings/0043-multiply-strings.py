class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        if len(num1) < len(num2):
            num1, num2 = num2, num1

        n1 = len(num1)
        n2 = len(num2)

        line_arr = []
        # num2
        line_idx = 0
        for i in range(n2 - 1, -1 , -1):
            line = ''
            carry = 0
            # num1
            for j in range(n1 - 1, -1, -1):
                m = int(num1[j]) * int(num2[i])
                nxt = m + carry
                line = str(nxt % 10) + line
                carry = nxt // 10
            
            if carry > 0:
                line = str(carry) + line

            line = line + '0' * line_idx
            line_arr.append(line)

            line_idx += 1
        
        for i in range(len(line_arr) - 1):
            line_arr[i] = '0' * (len(line_arr[-1]) - len(line_arr[i])) + line_arr[i]
        
        ans = ''
        carry = 0
        for i in range(len(line_arr[-1]) - 1, -1, -1):
            total = 0
            for j in range(len(line_arr)):
                total += int(line_arr[j][i])
            total += carry
            
            carry = total // 10
            ans = str(total % 10) + ans
        
        if carry > 0:
            ans = str(carry) + ans
        return ans