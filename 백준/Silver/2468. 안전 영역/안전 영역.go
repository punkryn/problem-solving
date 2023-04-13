package main

import (
	"bufio"
	"container/list"
	"fmt"
	"os"
)

func bfs(x int, y int, cnt int, h int) {
	q := list.New()
	q.PushBack([]int{x, y})
	visited[x][y] = 1

	for q.Len() > 0 {
		f := q.Front()
		q.Remove(f)
		a := f.Value.([]int)
		x, y = a[0], a[1]

		for i := 0; i < 4; i++ {
			nx := x + dx[i]
			ny := y + dy[i]
			if !(0 <= nx && nx < n && 0 <= ny && ny < n) {
				continue
			}
			if visited[nx][ny] != 0 || area[nx][ny] <= h {
				continue
			}
			visited[nx][ny] = cnt
			q.PushBack([]int{nx, ny})
		}
	}
}


var n int
var area [][]int
var dx [4]int = [4]int{-1, 0, 1, 0}
var dy [4]int = [4]int{0, 1, 0, -1}
var visited [][]int
var ans int = 1
func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	fmt.Fscanln(reader, &n)
	
	area = make([][]int, n)
	for i := range area {
		area[i] = make([]int, n)
	}
	var minHeight, maxHeight int = 101, 0
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			fmt.Fscan(reader, &area[i][j])
			if minHeight > area[i][j] {
				minHeight = area[i][j]
			}
			if maxHeight < area[i][j] {
				maxHeight = area[i][j]
			}
		}
	}

	for i := minHeight; i <= maxHeight; i++ {
		visited = make([][]int, n)
		for j := range visited {
			visited[j] = make([]int, n)
		}
		cnt := 0
		for j := 0; j < n; j++ {
			for k := 0; k < n; k++ {
				if visited[j][k] != 0 || area[j][k] <= i {
					continue
				}
				cnt += 1
				bfs(j, k, cnt, i)
			}
		}
		if ans < cnt {
			ans = cnt
		}
	}
	fmt.Fprint(writer, ans)
}