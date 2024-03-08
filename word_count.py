import click
import sys


@click.command()
@click.option(
    "-c",
    "--bytes",
    is_flag=True,
    help="Returns number of bytes",
)
@click.option(
    "-w",
    "--words",
    is_flag=True,
    help="Returns number of words",
)
@click.option(
    "-l",
    "--lines",
    is_flag=True,
    help="Returns number of lines",
)
@click.option(
    "-m",
    "--characters",
    is_flag=True,
    help="Returns number of characters",
)
@click.argument("filename", required=False, type=click.Path(exists=True))
def count_file_details(bytes, words, lines, characters, filename):
    """Print counts of bytes, words, lines, and/or characters for the
    specified FILENAME, or stdin, tab-separated."""
    output = []
    line_count = 0
    word_count = 0
    byte_count = 0
    characters_count = 0

    # Function to count details from text
    def count_details(text):
        nonlocal line_count, word_count, characters_count, byte_count
        characters_count += len(text)
        byte_count += len(text.encode("utf-8"))
        words = text.split()
        word_count += len(words)
        line_count += 1

    if filename:
        with open(filename, "r", encoding="utf-8") as fh:
            for line in fh:
                count_details(line)
    else:
        for line in sys.stdin:
            count_details(line)

    if bytes:
        output.append(str(byte_count))
    if words:
        output.append(str(word_count))
    if lines:
        output.append(str(line_count))
    if characters:
        output.append(str(characters_count))

    if not bytes and not words and not lines and not characters:
        output.extend([str(line_count), str(word_count), str(byte_count)])

    source = filename if filename else ""
    output.append(source)

    click.echo("\t".join(output))
