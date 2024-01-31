class Solution {
    private final int MOD = 1337;
    public int superPow(int a, int[] b) {
        return calc(a % MOD, b, b.length - 1);
    }

    private int calc(int a, int[] b, int idx) {
        if (idx == -1) {
            return 1;
        }

        return powmod(calc(a, b, idx - 1), 10) * powmod(a, b[idx]) % MOD;
    }

    private int powmod(int a, int cnt) {
        int ret = 1;
        for (int i = 0 ; i < cnt; i++) {
            ret = (ret * a) % MOD;
        }
        return ret;
    }
}