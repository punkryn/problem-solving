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

	ans := 1
	flag := false
	var prev rune
	for {
		word, _, _ := reader.ReadRune()
		if word == '\n' {
			if prev == ' ' {
				ans -= 1
			}
			break
		}

		if word == ' ' && flag {
			ans += 1
			flag = false
		} else {
			flag = true
		}
		prev = word
	}
	fmt.Fprint(writer, ans)
}