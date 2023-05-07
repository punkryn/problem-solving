// https://www.acmicpc.net/problem/28014
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

var (
	n int
	h []int
)
func main() {
	defer writer.Flush()

	fmt.Fscan(reader, &n)
	h = make([]int, n)
	
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &h[i])
	}

	ans := 1
	for i := 1; i < n; i++ {
		if h[i - 1] <= h[i] {
			ans += 1
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