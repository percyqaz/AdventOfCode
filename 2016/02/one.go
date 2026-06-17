package main

import (
    "fmt"
    "os"
    "strings"
)

func main() {
    x, y := 1, 1

    data, err := os.ReadFile("input.txt")
    if err != nil { panic(err) }

    input := string(data)
    lines := strings.Split(strings.Trim(input, "\n"), "\n")

	code := 0

    for _, line := range lines {
		for _, char := range line {
			if char == 'U' && y > 0 { y-- }
			if char == 'D' && y < 2 { y++ }
			if char == 'L' && x > 0 { x-- }
			if char == 'R' && x < 2 { x++ }
		}

		code *= 10
		code += 1 + x + 3 * y
    }
    
    fmt.Println(code)
}