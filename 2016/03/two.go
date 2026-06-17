package main

import (
    "fmt"
    "os"
	"strconv"
    "strings"
)

func main() {
    data, err := os.ReadFile("input.txt")
    if err != nil { panic(err) }

	possible := 0

    input := string(data)
    lines := strings.Split(strings.Trim(input, "\n"), "\r\n")
	lines2 := make([][] string, len(lines))
	for i, line := range lines {
		lines2[i] = strings.FieldsFunc(line, func(c rune) bool { return c == ' ' })
	}

	for i := 0; i < len(lines2); i += 3 {
		for x := 0; x < 3; x++ {
			a, err := strconv.Atoi(lines2[i][x])
			if err != nil { panic(err) }
			b, err := strconv.Atoi(lines2[i+1][x])
			if err != nil { panic(err) }
			c, err := strconv.Atoi(lines2[i+2][x])
			if err != nil { panic(err) }

			if a + b > c && a + c > b && b + c > a { possible++ }
		}
	}
    
    fmt.Println(possible)
}