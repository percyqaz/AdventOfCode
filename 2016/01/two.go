package main

import (
    "fmt"
    "os"
    "strconv"
    "strings"
)

type Coord struct {
    X, Y int
}

func main() {
    visited := make(map[Coord]bool)

    px, py := 0, 0
    mx, my := 0, 1

    data, err := os.ReadFile("input.txt")
    if err != nil { panic(err) }

    input := string(data)
    parts := strings.Split(input, ", ")

	outerLoop:
    for _, part := range parts {

        if part[0] == 'R' { mx, my = my, -mx } else { mx, my = -my, mx }

        num, err := strconv.Atoi(part[1:])
        if err != nil { panic(err) }

        for i := 0; i < num; i++ {
			px = px + mx
			py = py + my

			key := Coord{px, py}
			if visited[key] { break outerLoop }
			visited[key] = true
		}
    }
    
    fmt.Println(max(px, -px) + max(py, -py))
}