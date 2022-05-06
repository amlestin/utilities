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

func getQuantitativeTable() ([]byte, string) {
	// TODO: Read data from S3
	text, err := ioutil.ReadFile("quantitative_data.txt")
	if err != nil {
		log.Fatal("Failed to read input file!")
	}
	raw_data := string(text)
	log.Println(raw_data)

	cleaned_data := strings.Fields(raw_data)
	num_rows := len(cleaned_data)

	quantitative_map := make([]ConversionEntry, num_rows)

	for i, value := range cleaned_data {
		split_row := strings.Split(value, ":")
		old_score := split_row[0]
		new_score := strings.ReplaceAll(split_row[1], ",", "")

		quantitative_map[i] = ConversionEntry{old_score, new_score}
	}

	b, err := json.Marshal(quantitative_map)
	if err != nil {
		panic("Cannot create JSON.")
	}

	fmt.Println(quantitative_map, b, "\n")

	var ce ConversionEntry
	json.Unmarshal(b, &ce)
	fmt.Println(quantitative_map, ce)

	return b, raw_data
}

func HandleRequest(ctx context.Context) (string, error) {
	_, quantitativeTableStr := getQuantitativeTable()

	// parsing the ConversionEntry structs is adding work; going to try using a regular string
	return string(quantitativeTableStr), nil
}

func main() {
	lambda.Start(HandleRequest)
}