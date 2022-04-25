# utilities

Specialized programs to automate boring stuff.

### click_later.py: 
This program will click where your cursor is after your inputted delay or 1 second by default.

Before runnning, install the required library in the terminal: ```pip3 install pynput```

## notes_exporter.py:
A tool to export all notes from MacOS Notes as TXT files.

## go run movie_picker.go
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
