// https://www.acmicpc.net/problem/1722
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
	n, p, k int
	seq []int
	factorial []int
)
func main() {
	defer writer.Flush()

	fmt.Fscan(reader, &n)
	fmt.Fscan(reader, &p)

	factorial = make([]int, n + 1)
	factorial[0] = 1
	for i := 1; i <= n; i++ {
		factorial[i] = factorial[i - 1] * i
	}

	cand := make([]int, n + 1)
	for i := 0; i <= n; i++ {
		cand[i] = i
	}

	if p == 1 {
		fmt.Fscan(reader, &k)
		k -= 1
		ans := make([]int, n)
		for i := 0; i < n; i++ {
			// if k <= factorial[n - i - 1] {
			// 	ans[i] = cand[1]
			// 	cand = append(cand[:1], cand[2:]...)
			// } else {
				m := k / factorial[n - i - 1]
				k %= factorial[n - i - 1]

				ans[i] = cand[m + 1]
				cand = append(cand[:m + 1], cand[m + 2:]...)
			// }
		}

		for i := 0; i < n; i++ {
			fmt.Print(ans[i], " ")
		}
	} else if p == 2 {
		seq = make([]int, n)
		for i := 0; i < n; i++ {
			fmt.Fscan(reader, &seq[i])
		}

		ans := 1
		for i := 0; i < n - 1; i++ {
			ans += factorial[n - i - 1] * indexOf(cand, seq[i])
		}
		fmt.Println(ans)
	}
}

func indexOf(x []int, target int) int {
	for i, v := range x {
		if v == target {
			x = append(x[:i], x[i + 1:]...)
			return i - 1
		}
	}
	return -1
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