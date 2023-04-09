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

	var n int
	fmt.Fscan(reader, &n)
	for i := 1; i <= n - 1; i++ {
		for j := 0; j < n - i; j++ {
			fmt.Fprint(writer, " ")
		}
		for j := 0; j < i * 2 - 1; j++ {
			fmt.Fprint(writer, "*")
		}
		fmt.Fprint(writer, "\n")
	}
	for i := 0; i < n * 2 - 1; i++ {
		fmt.Fprint(writer, "*")
	}
	fmt.Fprint(writer, "\n")
	for i := 1; i <= n - 1; i++ {
		for j := 0; j < i; j++ {
			fmt.Fprint(writer, " ")
		}
		for j := 0; j < (n - i) * 2 - 1; j++ {
			fmt.Fprint(writer, "*")
		}
		fmt.Fprint(writer, "\n")
	}
}