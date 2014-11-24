package main

import "fmt"

func double(nums ...int) <-chan int {
	out := make(chan int)

	go func() {
		for i := range nums {
			out <- i * 2
		}
		close(out)
	}()

	return out
}

func main() {
	c := double(1, 2, 3, 4, 5)
	for i := range c {
		fmt.Println(i)
	}
}
