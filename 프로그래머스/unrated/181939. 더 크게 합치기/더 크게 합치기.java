class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        String ab = Integer.toString(a) + Integer.toString(b);
        String ba = Integer.toString(b) + Integer.toString(a);
        int abi = Integer.parseInt(ab);
        int bai = Integer.parseInt(ba);
        if (abi >= bai) {
            return abi;
        }
        
        return bai;
    }
}