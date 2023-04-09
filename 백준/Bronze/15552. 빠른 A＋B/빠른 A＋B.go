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

	var T int
	fmt.Fscan(reader, &T)
	var A, B int	
	for i := 0; i < T; i++ {
		fmt.Fscan(reader, &A, &B)
		fmt.Fprintln(writer, A + B)
	}
}