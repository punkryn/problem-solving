package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter((os.Stdout))
	defer writer.Flush()

	var n int
	var ans int
	fmt.Fscan(reader, &n)
	for i := 0; i <= n; i++ {
		r, _, _ := reader.ReadRune()
		m, _ := strconv.Atoi(string(r))
		ans += m
	}
	fmt.Fprint(writer, ans, "\n")
}