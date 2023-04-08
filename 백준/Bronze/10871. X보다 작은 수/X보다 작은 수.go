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

	var n, x int
	fmt.Fscan(reader, &n, &x)
	var A int
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &A)
		if A < x {
			fmt.Fprint(writer, A, " ")
		}
	}
}