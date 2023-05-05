// https://www.acmicpc.net/problem/4095
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

// var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)
var scanner = bufio.NewScanner(os.Stdin)
var dx = [4]int{-1, 0, 1, 0}
var dy = [4]int{0, 1, 0, -1}

var (
	n, m int
	matrix [][]int
	dp [][]int
)
func main() {
	defer writer.Flush()
	scanner.Split(bufio.ScanWords)

	for {
		n = scanInt()
		m = scanInt()
		if n == 0 && m == 0 {
			return
		}

		matrix = make([][]int, n + 1)
		dp = make([][]int, n + 1)
		for i := 0; i <= n; i++ {
			matrix[i] = make([]int, m + 1)
			dp[i] = make([]int, m + 1)
		}

		for i := 1; i <= n; i++ {
			for j := 1; j <= m; j++ {
				matrix[i][j] = scanInt()
			}
		}

		ans := 0
		for i := 1; i <= n; i++ {
			for j := 1; j <= m; j++ {
				if matrix[i][j] == 0 { continue }
				dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
				ans = max(ans, dp[i][j])
			}
		}
		fmt.Println(ans)
	}
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

func scanInt() int {
	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())
	return n
}