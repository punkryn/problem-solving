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
	for  {
		_, err := fmt.Fscan(reader, &A, &B)
		if err != nil {
			break
		}
		fmt.Fprintln(writer, A + B)
	}
}