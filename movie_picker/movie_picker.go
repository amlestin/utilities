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

	movies := make([]string, len(files))
	for i, v := range files {
		filename := v.Name()
		is_dir := v.IsDir()

		movies[i] = filename
		fmt.Println(filename, is_dir)
	}

	fmt.Println("\n")

	// TODO: Pick a random value in list if it ends in a movie fmt
	chosen_movie := "test"
	fmt.Println("Your next movie is: " + chosen_movie)
}
