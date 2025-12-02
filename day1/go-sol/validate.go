package main

import (
	"fmt"
	"os"
	"bufio"
	"strconv"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func main() {

	file , err	:= os.Open("validate.txt")
	dial := 50
	rotations := []string{}
	password := 0
	check(err)

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
        line := scanner.Text()
        rotations = append(rotations,line)
    }
	for _ , r := range rotations {
		rotation, err := strconv.Atoi(r[1:])
		check(err)

		if r[0] == 'R' {
			dial += rotation
			dial = dial % 100
		} else {
			dial -= rotation
			dial = dial % 100
		}

		if dial == 0 {
			password += 1
		}

	}

	fmt.Println(password)
	//fmt.Println(strings.Join(rotations, ", "))
    fmt.Println("Go-sol - by 0xkatana")
}
