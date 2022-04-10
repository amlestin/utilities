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

func main() {
	raw_data := `
	"170":"800",
	"169":"750",
	"168":"730",
	"167":"710",
	"166":"700",
	"165":"690",
	"164":"670",
	"163":"650",
	"162":"640",
	"161":"620",
	"160":"610",
	"159":"590",
	"158":"580",
	"157":"560",
	"156":"550",
	"155":"530",
	"154":"520",
	"153":"500",
	"152":"490",
	"151":"470",
	"150":"450",
	"149":"440",
	"148":"420",
	"147":"410",
	"146":"400",
	"145":"380",
	"144":"370",
	"143":"360",
	"142":"340",
	"141":"330",
	"140":"320",
	"139":"310",
	"138":"300",
	"137":"290",
	"135":"280",
	"134":"270",
	"133":"260",
	"132":"250",
	"131":"240",
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
		return
	}

	fmt.Println(verbal_map, b, "\n")

	var ce ConversionEntry
	json.Unmarshal(b, &ce)
	fmt.Println(verbal_map, ce)
}
