package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	px, py := 0, 0
	mx, my := 0, 1

	data, err := os.ReadFile("input.txt")
	if err != nil { panic(err) }

	input := string(data)
	parts := strings.Split(input, ", ")

	for _, part := range parts {

		if part[0] == 'R' {
			mx, my = my, -mx
		} else {
			mx, my = -my, mx
		}

		num, err := strconv.Atoi(part[1:])
		if err != nil { panic(err) }

		px = px + mx * num
		py = py + my * num
	}
	
	fmt.Println(max(px, -px) + max(py, -py))
}