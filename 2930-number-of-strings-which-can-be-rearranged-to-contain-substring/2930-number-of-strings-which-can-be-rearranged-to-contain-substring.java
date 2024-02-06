class Solution {
    private final int mod = 1_000_000_007;
    public int stringCount(int n) {
        if (n < 4) return 0;

        long total = pow(26, n) % mod;
        long c1 = (pow(25, n) + pow(25, n) + pow(25, n) + n * pow(25, n - 1)) % mod;
        long c2 = (pow(24, n) + pow(24, n) + n * pow(24, n - 1) + pow(24, n) + n * pow(24, n - 1)) % mod;
        long c3 = (pow(23, n) + n * pow(23, n - 1)) % mod;
        return (int)((total - c1 + c2 - c3) % mod + mod) % mod;
    }

    private long pow(long p, long n) {
        long ret = 1;
        p %= mod;
        
        while (n > 0) {
            if ((n & 1) != 0) {
                ret = (ret * p) % mod;
            }
            p = (p * p) % mod;
            n >>= 1;
        }
        return ret;
    }
}