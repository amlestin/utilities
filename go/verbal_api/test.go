package main

import (
	"encoding/json"
	"fmt"
	"strings"
)

type ConversionEntry struct {
	Old string
	New string
}

func getVerbalTable() []byte {
	raw_data := `
	"170":"800",
	"169":"750",
	"168":"730",
	"167":"710",
	"130":"230"`

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
		return nil
	}

	fmt.Println(verbal_map, b)
	fmt.Println()

	var ce ConversionEntry
	json.Unmarshal(b, &ce)
	fmt.Println(verbal_map, ce)

	return b
}

func main() {
	// verbalTableStr :=  getVerbalTable()
	getVerbalTable()
}
