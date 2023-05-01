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


func main() {
	defer writer.Flush()

	var s string
	var cnt [26]int
	fmt.Fscan(reader, &s)
	
	for _, word := range s {
		cnt[word - 'A'] += 1
	}

	odd := 0
	for i := 0; i < 26; i++ {
		if cnt[i] % 2 == 1{
			odd += 1
		}
	}
	if odd > 1 {
		fmt.Println("I'm Sorry Hansoo")
		return
	}

	var tmp []rune = make([]rune, len(s))
	pos := 0
	for i := 0; i < 26; i++ {
		if cnt[i] == 0 { continue }
		if cnt[i] % 2 == 1 {
			tmp[len(s) / 2] = rune(i + 'A')
		}
		for j := 0; j < cnt[i] / 2; j++ {
			tmp[pos] = rune(i + 'A')
			tmp[len(s) - pos - 1] = rune(i + 'A')
			pos += 1
		}
	}

	fmt.Println(string(tmp))
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