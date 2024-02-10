class Solution {
    private final int mod = 1_000_000_007;
    public int monkeyMove(int n) {
        return (int)(pow(2, n) - 2 + mod) % mod;
    }

    private long pow(long n, long p) {
        long ret = 1;
        while (p > 0) {
            if ((p & 1) != 0) {
                ret = (ret * n) % mod;
            }
            n = (n * n) % mod;
            p >>= 1;
        }
        return ret % mod;
    }
}