package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	current_dir, err := os.Getwd()

	if err != nil {
		log.Println(err)
	}

	fmt.Println("Scanning foler: " + current_dir)

	// TODO: List files
	f, err := os.Open(current_dir)
	if err != nil {
		fmt.Println(err)
		return
	}
	files, err := f.Readdir(0)
	if err != nil {
		fmt.Println(err)
		return
	}

	for _, v := range files {
		fmt.Println(v.Name(), v.IsDir())
	}

	fmt.Println("\n")

	// TODO: Pick a random value in list if it ends in a movie fmt
	chosen_movie := "test"
	fmt.Println("Your next movie is: " + chosen_movie)
}
