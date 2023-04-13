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

	var n, m int
	fmt.Fscanln(reader, &n, &m)
	bucket := make([]int, n + 1)
	var x, y, z int
	for i := 0; i < m; i++ {
		fmt.Fscanln(reader, &x, &y, &z)
		for j := x; j <= y; j++ {
			bucket[j] = z
		}
	}

	for i := 1; i <= n; i++ {
		fmt.Fprint(writer, bucket[i], " ")
	}
}