package main

import (
    "fmt"
    "os"
    "strings"
)

func main() {
    x, y := 2, 2

    data, err := os.ReadFile("input.txt")
    if err != nil { panic(err) }

    input := string(data)
    lines := strings.Split(strings.Trim(input, "\n"), "\n")

	code := ""
    keypad := [5]string{"  1  ", " 234 ", "56789", " ABC ", "  D  "}

    for _, line := range lines {
		for _, char := range line {
			if char == 'U' && y > max(x - 2, 2 - x) { y-- }
			if char == 'D' && y < 4 - max(x - 2, 2 - x) { y++ }
			if char == 'L' && x > max(y - 2, 2 - y) { x-- }
			if char == 'R' && x < 4 - max(y - 2, 2 - y) { x++ }
		}

		code += string(keypad[y][x])
    }
    
    fmt.Println(code)
}