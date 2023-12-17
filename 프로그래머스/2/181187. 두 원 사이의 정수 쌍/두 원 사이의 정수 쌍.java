// r1^2 <= a^2 + b^2 <= r2^2
// 1.xx <= b <= 2.xx

// class Solution {
//     public long solution(int r1, int r2) {
//         long answer = 0;
//         answer += (long)(r2 - r1 + 1) * 4;
        
//         for (int i = 1; i < r2; i++) {            
//             int left = (int)Math.sqrt(Math.pow(r2, 2) - Math.pow(i, 2));
//             int right = (int)Math.sqrt(Math.pow(r1, 2) - Math.pow(i, 2));
//             long count = (long)(left - right);
            
//             if (i < r1 && Math.sqrt(Math.pow(r2, 2) - Math.pow(i, 2)) % 1 == 0) {
//                 count += 1L;
//             }
//             answer += count * 4;
//         }
        
//         return answer;
//     }
// }

class Solution {
    public long solution(int r1, int r2) {
    // x축 위의 점의 수 *4축
    long answer = (long)(r2-r1+1)*4L;
    int smallY = 0;
    int bigY = 0;
    // 1사분면의 격자점의 개수 *4사분면
    for(int x=1;x<r2;x++){
        smallY = (int)Math.sqrt((long)r1*r1-(long)x*x);
        bigY = (int)Math.sqrt((long)r2*r2-(long)x*x);
        answer += (long)(bigY-smallY)*4;
        // 작은원의 테두리가 격자점을 지나면 하나 추가 *4사분면
        if(x<r1 && Math.sqrt((long)r1*r1-(long)x*x)%1 ==0) answer+=4L;
    }
    return answer;
}
}
