package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)
var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)


func main() {
	defer writer.Flush()

	var s string
	fmt.Fscan(reader, &s)
	
	arr := make([]string, 0)
	for i, _ := range s {
		arr = append(arr, s[i:])
	}

	sort.Strings(arr)
	for _, s := range arr {
		fmt.Fprintln(writer, s)
	}
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