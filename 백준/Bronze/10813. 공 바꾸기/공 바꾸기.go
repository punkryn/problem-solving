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

	var n, m, x, y int64
	fmt.Fscan(reader, &n)
	fmt.Fscan(reader, &m)

	arr := make([]int64, n + 1)
	for i := int64(0); i <= n; i++ {
		arr[i] = i
	}

	for i := int64(0); i < m; i++ {
		fmt.Fscan(reader, &x)
		fmt.Fscan(reader, &y)
		
		arr[x], arr[y] = arr[y], arr[x]
	}

	for i := int64(1); i <= n; i++ {
		fmt.Fprint(writer, arr[i], " ")
	}
}