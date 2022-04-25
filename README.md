# utilities

Specialized programs to automate boring stuff.

### click_later.py: 
This program will click where your cursor is after your inputted delay or 1 second by default.

Before runnning, install the required library in the terminal: ```pip3 install pynput```

### Usage
1. ```python3 click_later.py```
2. Place mouse over the desired spot to click later within START_DELAY (in code) seconds
3. The mouse will click after SLEEP_DUR (in code) seconds

## notes_exporter.py:
A tool to export all notes from MacOS Notes as TXT files.
### Usage
1. ```python3 notes_exporter.py```
2. Click on Notes app within START_DELAY (in code) seconds

## movie_picker.go:
### Setup

To access VLC from the Terminal on MacOS, add this to ~/.bashrc and ```source ~/.bashrc```

```
alias vlc='/Applications/VLC.app/Contents/MacOS/VLC'
export PATH=$PATH:/Applications/VLC.app/Contents/MacOS/
```

### Usage
To pick from the dir containing the .go file

```go run movie_picker.go``` 

OR

To pick from path_to_movies_directory

```go run movie_picker.go path_to_movies_directory```
