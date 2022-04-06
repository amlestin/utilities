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

	fmt.Println("Scanning foler: " + current_dir + "\n")

	// TODO: List files
	// TODO: Pick a random value in list if it ends in a movie fmt
	chosen_movie := "test"
	fmt.Println("Your next movie is: " + chosen_movie)
}
