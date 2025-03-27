import io
import sys

from PIL import Image
import click
import pytesseract


@click.command()
@click.argument("image_path", required=False, type=click.Path(exists=True))
def main(image_path):
    """Extract text from an image file or stdin and print to stdout

    Examples:

    \b
    $ img2txt image.png
    $ cat image.png | img2txt

    For help:
    $ img2txt --help
    """
    try:
        if image_path:
            image = Image.open(image_path)
        else:
            if sys.stdin.isatty():
                click.echo("No image path provided and no input from stdin.", err=True)
                sys.exit(1)

            image_data = sys.stdin.buffer.read()
            image = Image.open(io.BytesIO(image_data))

        text = pytesseract.image_to_string(image)
        click.echo(text.strip())

    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
