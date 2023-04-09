package main

import (
	"bufio"
	"fmt"
	"os"
)

const MAX int = 10000

var arr [MAX]int64
var stackPointer int64 = -1

func push(X int64) {
	stackPointer += 1
	arr[stackPointer] = X
}

func pop() int64 {
	if empty() == 1 {
		return -1
	}
	ret := arr[stackPointer]
	stackPointer -= 1
	return ret
}

func size() int64 {
	return stackPointer + 1
}

func empty() int64 {
	if stackPointer == -1 {
		return 1
	}
	return 0
}

func top() int64 {
	if empty() == 1 {
		return -1
	}
	return arr[stackPointer]
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n int
	var str string
	fmt.Fscanln(reader, &n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &str)
		if str == "push" {
			var X int64
			fmt.Fscan(reader, &X)
			push(X)
		} else if str == "top" {
			fmt.Fprintln(writer, top())
		} else if str == "pop" {
			fmt.Fprintln(writer, pop())
		} else if str == "size" {
			fmt.Fprintln(writer, size())
		} else {
			fmt.Fprintln(writer, empty())
		}
	}
}
