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

	var A, B int
	for {
		fmt.Fscan(reader, &A, &B)
		if A == 0 && B == 0 {
			break
		}
		fmt.Fprint(writer, A + B, "\n")
	}
}