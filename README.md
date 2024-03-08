# Wordcount

Wordcount is a versatile command-line tool designed to provide quick statistics on text input, including the number of words, characters, bytes, and lines. This tool is inspired by wc and the first challenge from John Cricket's coding challenge, built for ease of use and integration into larger text processing pipelines.

## Features

- Count words, lines, characters, and bytes in text files or standard input.
- Flexible usage: Read from a file or pipe input from other commands.
- Customizable output: Choose what statistics to display with simple command-line options.

## Installation

To install Wordcount, ensure you have Python version 3.7 or higher. You can install Wordcount directly from the source code using the following steps:

1. Clone the repository from GitHub:

```bash
git clone https://github.com/AbhilashBharadwaj/wc-cli-tool
cd wordcount
```

2. Install the package:
```bash
python setup.py install
```
This command installs the wordcount package along with its dependencies.

## Usage
After installation, you can use the ccwc command to count words, characters, lines, or bytes. Here are some examples of how to use it:

Count lines in a file:
```bash
ccwc -l <filename>
```
Count words from standard input:
```bash

cat <filename> | ccwc -w
```
## Options
- -c, --bytes : Returns the number of bytes.
- -w, --words : Returns the number of words.
- -l, --lines : Returns the number of lines.
- -m, --characters : Returns the number of characters.

## Arguments
filename : The name of the file to process. If omitted, ccwc will read from standard input.

## Dependencies
Wordcount requires Python version 3.7 or higher. Dependencies required for the tool are listed in the requirements.txt file and are automatically installed during the setup process.

## Contributing
Contributions to Wordcount are welcome! To contribute, please follow these steps:

Fork the repository on GitHub.
Create a new branch for your feature or bug fix.
Develop your changes in your branch.
Submit a pull request with a comprehensive description of your changes.
License
Wordcount is released under the MIT License. See the LICENSE file in the source repository for more information.