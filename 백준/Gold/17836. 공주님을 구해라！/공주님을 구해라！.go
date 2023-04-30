package main

import (
	"bufio"
	"container/list"
	"fmt"
	"os"
)
var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)
var dx = [4]int{-1, 0, 1, 0}
var dy = [4]int{0, 1, 0, -1}

var (
	n, m, t int
	maze [101][101]int
	visited [101][101][2]int
)

type Node struct {
	x int
	y int
	flag int
}

type Queue struct {
	v *list.List
}

func NewQueue() *Queue {
	return &Queue{list.New()}
}

func (q *Queue) Push(v interface{}) {
	q.v.PushBack(v)
}

func (q *Queue) Pop() interface{} {
	front := q.v.Front()
	if front == nil {
		return nil
	}

	return q.v.Remove(front)
}

func main() {
	defer writer.Flush()

	fmt.Fscan(reader, &n, &m, &t)

	for i := 1; i <= n; i++ {
		for j := 1; j <= m; j++ {
			fmt.Fscan(reader, &maze[i][j])
			visited[i][j][0] = -1
			visited[i][j][1] = -1
		}
	}

	q := NewQueue()
	q.Push(Node{1, 1, 0})
	visited[1][1][0] = 0

	for q.v.Len() > 0 {
		cur := q.Pop()
		c, _ := cur.(Node)

		x := c.x
		y := c.y
		flag := c.flag
		for i := 0; i < 4; i++ {
			nx := x + dx[i]
			ny := y + dy[i]

			if !(1 <= nx && nx <= n && 1 <= ny && ny <= m) { continue }
			if flag == 0 && maze[nx][ny] == 1 { continue }
			
			if maze[nx][ny] == 2 {
				if visited[nx][ny][1] != -1 { continue }
				q.Push(Node{nx, ny, 1})
				visited[nx][ny][1] = visited[x][y][flag] + 1
			} else if flag == 1 && maze[nx][ny] == 1 {
				if visited[nx][ny][flag] != -1 { continue }
				visited[nx][ny][flag] = visited[x][y][flag] + 1
				q.Push(Node{nx, ny, flag})
			} else if maze[nx][ny] == 0 {
				if visited[nx][ny][flag] != -1 { continue }
				q.Push(Node{nx, ny, flag})
				visited[nx][ny][flag] = visited[x][y][flag] + 1
			}
		}
	}

	if visited[n][m][0] == -1 && visited[n][m][1] == -1 {
		fmt.Println("Fail")
	} else if visited[n][m][0] == -1 {
		if visited[n][m][1] <= t {
			fmt.Println(visited[n][m][1])
		} else {
			fmt.Println("Fail")
		}
	} else if visited[n][m][1] == -1 {
		if visited[n][m][0] <= t {
			fmt.Println(visited[n][m][0])
		} else {
			fmt.Println("Fail")
		}
	} else {
		ans := min(visited[n][m][0], visited[n][m][1])
		if ans <= t {
			fmt.Println(ans)
		} else {
			fmt.Println("Fail")
		}
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