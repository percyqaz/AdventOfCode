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

    for _, line := range lines {
		parts := strings.FieldsFunc(line, func(c rune) bool { return c == ' ' })
		a, err := strconv.Atoi(parts[0])
		if err != nil { panic(err) }
		b, err := strconv.Atoi(parts[1])
		if err != nil { panic(err) }
		c, err := strconv.Atoi(parts[2])
		if err != nil { panic(err) }

		if a + b > c && a + c > b && b + c > a { possible++ }
    }
    
    fmt.Println(possible)
}