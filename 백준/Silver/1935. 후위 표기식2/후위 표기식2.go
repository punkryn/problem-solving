// https://www.acmicpc.net/problem/1935
package main

import (
	"bufio"
	"fmt"
	"os"
)
var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)
var dx = [4]int{-1, 0, 1, 0}
var dy = [4]int{0, 1, 0, -1}

var (
	n int
	m float64
	s string
	an map[rune]float64
)
func main() {
	defer writer.Flush()

	fmt.Fscan(reader, &n)
	fmt.Fscan(reader, &s)

	an = make(map[rune]float64)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &m)
		an[rune('A' + i)] = m
	}

	stack := make([]float64, 0)
	for _, w := range s {
		if 'A' <= w && w <= 'Z' {
			stack = append(stack, an[w])
		} else {
			a := stack[len(stack) - 2]
			b := stack[len(stack) - 1]
			
			var tmp float64
			if w == '+' {
				tmp = a + b
			} else if w == '-' {
				tmp = a - b
			} else if w == '*' {
				tmp = a * b
			} else {
				tmp = a / b
			}

			stack = stack[:len(stack) - 2]
			stack = append(stack, tmp)
		}
	}
	fmt.Printf("%.2f\n", stack[0])
}
type IntType interface {
	int | int64 | int32
}
func min[it IntType](x ...it) it {
	var ret it = x[0]
	for _, v := range x[1:] {
		if ret > v {
			ret = v
		}
	}
	return ret
}
func max[it IntType](x ...it) it {
	var ret it = x[0]
	for _, v := range x[1:] {
		if ret < v {
			ret = v
		}
	}
	return ret
}
func sum[it IntType](x ...it) it {
	var ret it = 0
	for _, v := range x {
		ret += v
	}
	return ret
}