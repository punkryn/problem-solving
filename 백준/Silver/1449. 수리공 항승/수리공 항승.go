package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)
var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)
var dx = [4]int{-1, 0, 1, 0}
var dy = [4]int{0, 1, 0, -1}

var (
	n, l int
	pos []int
)

func main() {
	defer writer.Flush()

	fmt.Fscan(reader, &n, &l)
	
	pos = make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &pos[i])
	}
	sort.Ints(pos)

	cur := l
	ans := 1
	for i := 1; i < n; i++ {
		diff := pos[i] - pos[i - 1]
		if diff + 1 > cur {
			cur = l
			ans += 1
			continue
		}

		cur -= diff
	}
	fmt.Fprintln(writer, ans)
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