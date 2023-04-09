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
	var T int
	fmt.Fscan(reader, &T)
	for i := 1; i <= T; i++ {
		fmt.Fscan(reader, &A, &B)
		fmt.Fprintf(writer, "Case #%v: %v\n", i, A + B)
	}
}