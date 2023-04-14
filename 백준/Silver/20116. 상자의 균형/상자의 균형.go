package main

import (
	"bufio"
	"fmt"
	"os"
)

var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)
var n, L int
var X []int
func main() {
	defer writer.Flush()

	fmt.Fscanln(reader, &n, &L)
	X = make([]int, n + 1)
	for i := n; i > 0; i-- {
		fmt.Fscan(reader, &X[i])
	}

	ans := "stable"
	ps := 0
	var xl, xr int
	for i := 1; i < n; i++ {
		ps += X[i]
		xl = X[i + 1] - L
		xr = X[i + 1] + L
		
		avg := ps
		if !(xl * i < avg && avg < xr * i) {
			ans = "unstable"
			break
		}
	}
	fmt.Fprintln(writer, ans)
}