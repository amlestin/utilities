package main

import (
	"fmt"
	"log"
	"os"
	"os/exec"
	"math/rand"
	crypto_rand "crypto/rand"
	"encoding/binary"
	"strings"
)

func isMovie(title string) bool {
	if strings.Contains(title, ".mp4") {
		return true
	}
	return false
}

func main() {
	// seed the random number generator
	var b [8]byte
	_, err := crypto_rand.Read(b[:])
	if err != nil {
		return
	}
	rand.Seed(int64(binary.LittleEndian.Uint64(b[:])))

	// Scans the dir given if there is a command line argument, else uses dir the program is running in
	var current_dir string
	if len(os.Args) > 1 {
		current_dir = os.Args[1]
	} else {
		current_dir, err = os.Getwd()
	}

	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Scanning foler: " + current_dir)

	f, err := os.Open(current_dir)
	if err != nil {
		log.Fatal(err)
		return
	}
	files, err := f.Readdir(0)
	if err != nil {
		log.Fatal(err)
		return
	}

	// save valid movies to the array "movies"
	movies := make([]string, len(files))
	movieCtr := 0
	for _, v := range files {
		filename := v.Name()

		if isMovie(filename) {
			movies[movieCtr] = filename
			movieCtr++
		}

	}

	// quit if no movies were found
	if movieCtr == 0 {
		fmt.Println("No movies found at", current_dir)
		return
	}

	chosen_movie := movies[rand.Intn(movieCtr)]
	fmt.Println("Your next movie is: " + chosen_movie)
	path := current_dir + "/" + chosen_movie
	
	// open the movie in VLC
	// TODO: confirm VLC is in $PATH
	cmd := exec.Command("vlc", path)
	err = cmd.Start()

	if err != nil {
		log.Fatal(err)
	}

}
