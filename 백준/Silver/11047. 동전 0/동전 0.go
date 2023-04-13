package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n, k int
	fmt.Fscanln(reader, &n, &k)
	coins := make([]int, n)
	var A int
	for i := 0; i < n; i++ {
		fmt.Fscanln(reader, &A)
		coins[i] = A
	}

	ans := 0
	for i := n - 1; i >= 0; i-- {
		ans += k / coins[i]
		k %= coins[i]
	}
	fmt.Fprintln(writer, ans)
}