# img2txt

A simple command-line tool to extract text from images using Tesseract OCR.

## Features

- Extracts text from images using Tesseract OCR
- Supports common image formats (JPEG, PNG, etc.)
- Works as a single binary

## Installation

### 1. Install Tesseract OCR

Ensure [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) is installed on your system.

### 2. Install img2txt

#### Prebuilt Binary

Download the latest release for your platform from the [Releases](https://github.com/KhiemNguyen15/img2txt/releases) page and extract it:

```sh
# For Linux (amd64)
wget https://github.com/KhiemNguyen/img2txt/releases/download/v0.1.0/img2txt-0.1.0-linux-amd64.tar.gz

# Extract the archive
tar -xvzf img2txt-0.1.0-linux-amd64.tar.gz

# Move to a location in your PATH
mv img2txt $HOME/.local/bin/
```

#### From Source

Ensure you have Python and `uv` installed, then run:

```sh
# Clone and enter the repository
git clone https://github.com/KhiemNguyen15/img2txt.git && cd img2txt

# Install project dependencies
uv sync

# Enter the virtual environment
source .venv/bin/activate

# Build the binary using PyInstaller
pyinstaller -F img2txt/img2txt.py

# Move the binary to a directory in your system's PATH
mv dist/img2txt $HOME/.local/bin/
```

## Usage

Just run the command with the file path:

```sh
img2txt image.jpg
```

Or pipe it in from your clipboard:

```sh
xclip -sel clip -o | img2txt
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contributing

Pull requests are welcome! Feel free to open an issue for feature requests or bug reports.
