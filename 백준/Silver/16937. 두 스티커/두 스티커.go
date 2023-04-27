package main

import (
	"bufio"
	"fmt"
	"os"
)
var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)

type sticker struct {
	r int
	c int
}

var (
	h, w, n int
	stickers []sticker
)

func check(x, y int) bool {
	s1 := stickers[x]
	s2 := stickers[y]

	// o o
	if (h >= s1.r && w - s1.c >= s2.c && h >= s2.r) || (w >= s1.c && h - s1.r >= s2.r && w >= s2.c) {
		return true
	}

	// o x
	if (h >= s1.r && w - s1.c >= s2.r && h >= s2.c) || (w >= s1.c && h - s1.r >= s2.c && w >= s2.r) {
		return true
	}

	// x o
	if (h >= s1.c && w - s1.r >= s2.c && h >= s2.r) || (w >= s1.r && h - s1.c >= s2.r && w >= s2.c) {
		return true
	}

	// x x
	if (h >= s1.c && w - s1.r >= s2.r && h >= s2.c) || (w >= s1.r && h - s1.c >= s2.c && w >= s2.r) {
		return true
	}

	return false
}

func main() {
	defer writer.Flush()

	fmt.Fscan(reader, &h, &w)
	fmt.Fscan(reader, &n)
	
	stickers = make([]sticker, n)
	var r, c int
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &r, &c)
		stickers[i] = sticker{r, c}
	}

	ans := 0
	for i := 0; i < n - 1; i++ {
		for j := i + 1; j < n; j++ {
			if check(i, j) {
				ans = max(ans, stickers[i].r * stickers[i].c + stickers[j].r * stickers[j].c)
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