
# PixelDrain File Downloader

This Python script allows users to download files from [PixelDrain](https://pixeldrain.com) by providing the URL. The script automatically retrieves the original file name from the server, gives the user the option to either use the original name or provide a custom name, and downloads the file accordingly.

## Features

- Extracts file ID from PixelDrain URL.
- Retrieves the original file name from the response headers.
- Option to use the original file name or provide a custom name.
- Saves the downloaded file to your local directory.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/pixeldrain-downloader.git
   cd pixeldrain-downloader
   ```

2. Install the required dependencies:

   ```bash
   pip install requests
   ```

3. Run the script:

   ```bash
   python downloader.py
   ```

4. Enter the PixelDrain file URL when prompted.

5. Choose whether to use the original file name or specify a custom one.

## Example

```bash
Enter PixelDrain URL: https://pixeldrain.com/u/fileid12345

Downloading from: https://pixeldrain.com/api/file/fileid12345?download

The original file name is: example.txt
Do you want to use the original name? (y/n): y

File downloaded successfully and saved as example.txt.
```

## Requirements

- Python 3.x
- `requests` module

## License

This project is licensed under the MIT License.

## Credits

- Script created by [Log-D7].
- Join the Telegram channel for updates: [Log - D7](https://t.me/Decode7Channel)
