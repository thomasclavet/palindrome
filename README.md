# Palindrome Checker

This Python script provides a function to check if a given phrase is a palindrome based on the following definition:
> A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as madam or racecar, the date "22/02/2022" and the sentence: "A man, a plan, a canal – Panama".

## Requirements

- Python 3.10
- Poetry

## Usage
Make commands are provided to use this script

### Installation
```
make install
```

### Example
```
make run PHRASE=" man, a plan, a canal – Panama"
```

### Running tests
```
make test
```



This will output whether the provided phrase is a palindrome or not.

## Implementation

The `is_palindrome` function takes a string as input and performs the following steps:

1. Checks if the input is a string. If not, it raises a `TypeError`.
2. Removes any punctuation characters from the string using the `string` module.
3. Converts the string to lowercase and removes any spaces.
4. Checks if the cleaned string is equal to its reverse (using slice notation `[::-1]`).
5. Returns `True` if the string is a palindrome, `False` otherwise.
