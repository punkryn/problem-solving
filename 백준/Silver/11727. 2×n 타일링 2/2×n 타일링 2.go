package main

import (
	"bufio"
	"fmt"
	"os"
)
var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)
var dx = [4]int{-1, 0, 1, 0}
var dy = [4]int{0, 1, 0, -1}


func main() {
	defer writer.Flush()

	var n int
	fmt.Fscan(reader, &n)
	
	var dp []int = make([]int, n + 1)
	dp[0] = 1
	dp[1] = 1
	if n == 1 {
		fmt.Println(1)
		return
	}

	for i := 2; i <= n; i++ {
		dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 10007
	}
	fmt.Println(dp[n])
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