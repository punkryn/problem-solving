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

	var ans int64
	var idx int64
	var a int64
	for i := 1; i <= 9; i++ {
		fmt.Fscan(reader, &a)
		if a > ans {
			idx = int64(i)
			ans = a
		}
	}
	fmt.Fprint(writer, ans, "\n", idx)
}