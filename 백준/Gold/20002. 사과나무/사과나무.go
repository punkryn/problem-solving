// https://www.acmicpc.net/problem/20002
package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)
var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)
var dx = [4]int{-1, 0, 1, 0}
var dy = [4]int{0, 1, 0, -1}

var (
	n int
	orchard [][]int
)
func main() {
	defer writer.Flush()

	fmt.Fscan(reader, &n)
	orchard = make([][]int, n + 1)
	for i := 0; i <= n; i++ {
		orchard[i] = make([]int, n + 1)
	}

	for i := 1; i <= n; i++ {
		for j := 1; j <= n; j++ {
			fmt.Fscan(reader, &orchard[i][j])
		}
	}
	
	for i := 1; i <= n; i++ {
		for j := 1; j <= n; j++ {
			orchard[i][j] += orchard[i][j - 1]
		}
	}

	for j := 1; j <= n; j++ {
		for i := 1; i <= n; i++ {
			orchard[i][j] += orchard[i - 1][j]
		}
	}

	ans := math.MinInt
	for i := 1; i <= n; i++ {
		for j := 1; j <= n; j++ {
			for k := 1; k <= min(i, j); k++ {
				ans = max(ans, orchard[i][j] - orchard[i][j - k] - orchard[i - k][j] + orchard[i - k][j - k])
			}
		}
	}
	fmt.Println(ans)
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