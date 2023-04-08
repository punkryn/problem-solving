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

	var n int64
	fmt.Fscan(reader, &n)

	if n % 2 == 0 {
		fmt.Fprint(writer, (1 + n) * (n / 2))
	} else {
		fmt.Fprint(writer, (1 + n) * (n / 2) + (1 + n) / 2)
	}
}