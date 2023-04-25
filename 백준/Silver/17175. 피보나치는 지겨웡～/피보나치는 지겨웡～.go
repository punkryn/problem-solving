// https://www.acmicpc.net/problem/17175
package main

import (
	"bufio"
	"fmt"
	"os"
)
var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)

var MOD int = int(1e9) + 7
func main() {
	defer writer.Flush()
	var n int
	fmt.Fscan(reader, &n)
	dp := make([]int, n + 2)
	
	dp[n] = 1
	for i := n; i >= 2; i-- {
		dp[i - 1] = (dp[i - 1] + dp[i]) % MOD
		dp[i - 2] = (dp[i - 2] + dp[i]) % MOD
	}
	fmt.Println(sum(dp...) % MOD)
}
type IntType interface {
	int | int64 | int32
}
func min[it IntType](x ...it) it {
	var ret it = x[0]
	for _, v := range x[1:] {
		if ret > v {
			ret = v
		}
	}
	return ret
}
func max[it IntType](x ...it) it {
	var ret it = x[0]
	for _, v := range x[1:] {
		if ret < v {
			ret = v
		}
	}
	return ret
}
func sum[it IntType](x ...it) it {
	var ret it = 0
	for _, v := range x {
		ret += v
	}
	return ret
}