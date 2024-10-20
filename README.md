
# PixelDrain File Downloader

This Python script allows users to download files from [PixelDrain](https://pixeldrain.com) by providing the URL. The script automatically retrieves the original file name from the server, gives the user the option to either use the original name or provide a custom name, and downloads the file accordingly.

## Features

- **Automatic File ID Extraction**: The script automatically extracts the file ID from the given PixelDrain URL.
- **Original File Name Detection**: It checks the file's original name from the server, if available.
- **Custom File Naming**: You can choose to either use the original file name or enter a custom name.
- **Download to Local**: The file is downloaded and saved locally with the desired name and extension.

## Requirements

- Python 3.x
- `requests` module (install via `pip`)

### Install `requests` Module
To install the required module, run the following command:

```bash
pip install requests

## How to Use

1. Clone the Repository

git clone https://github.com/yourusername/pixeldrain-downloader.git

2. Navigate to the Project Directory

cd pixeldrain-downloader

3. Install the Required Dependencies

pip install requests

4. Run the Script

python downloader.py

5. Enter the PixelDrain URL

You will be prompted to input the URL from PixelDrain.

6. Choose File Name

The script will show the original file name (if available) and ask if you want to use that name. You can confirm or provide a custom file name.


## Credits
[Log-D7](https://t.me/Decode7Channel)
