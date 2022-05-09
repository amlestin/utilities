package main

import (
	"context"
	"encoding/json"
	"fmt"
	"strings"
	"io/ioutil"
	"github.com/aws/aws-lambda-go/lambda"
	"log"
)

type ConversionEntry struct {
	Old string
	New string
}

func getVerbalTable() ([]byte, string) {
	text, err := ioutil.ReadFile("verbal_data.txt")
	if err != nil {
		log.Fatal("Failed to read input file!")
	}
	raw_data := string(text)
	log.Println(raw_data)

	cleaned_data := strings.Fields(raw_data)
	num_rows := len(cleaned_data)

	verbal_map := make([]ConversionEntry, num_rows)

	for i, value := range cleaned_data {
		split_row := strings.Split(value, ":")
		old_score := split_row[0]
		new_score := strings.ReplaceAll(split_row[1], ",", "")

		verbal_map[i] = ConversionEntry{old_score, new_score}
	}

	b, err := json.Marshal(verbal_map)
	if err != nil {
		panic("Failed to create JSON!")
	}

	fmt.Println(verbal_map, b, "\n")

	var ce ConversionEntry
	json.Unmarshal(b, &ce)
	fmt.Println(verbal_map, ce)

	return b, raw_data
}

func HandleRequest(ctx context.Context) (string, error) {
	_, verbalTableStr := getVerbalTable()

	return string(verbalTableStr), nil
}

func main() {
	lambda.Start(HandleRequest)
}
