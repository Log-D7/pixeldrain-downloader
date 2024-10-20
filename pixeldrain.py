import requests

def download_pixeldrain_file():
    url_input = input("Enter PixelDrain URL: ")
    file_id = extract_file_id(url_input)
    download_link = f"https://pixeldrain.com/api/file/{file_id}?download"
    print(f"\nDownloading from: {download_link}")
    response = requests.get(download_link)
    original_file_name = get_original_file_name(response, file_id)
    print(f"\nThe original file name is: {original_file_name}")
    file_name = choose_file_name(original_file_name)
    save_file(response, file_name)

def extract_file_id(url):
    return url.split('/')[-1]

def get_original_file_name(response, file_id):
    if 'Content-Disposition' in response.headers:
        return response.headers['Content-Disposition'].split('filename=')[-1].strip('"')
    return file_id

def choose_file_name(original_file_name):
    use_original = input("Do you want to use the original name? (y/n): ").lower()
    if use_original == 'y':
        return original_file_name
    else:
        custom_name = input("Enter a custom file name (without extension): ")
        file_extension = original_file_name.split('.')[-1]
        return f"{custom_name}.{file_extension}"

def save_file(response, file_name):
    with open(file_name, "wb") as f:
        f.write(response.content)
    print(f"\nFile downloaded successfully and saved as {file_name}.")

if __name__ == "__main__":
    download_pixeldrain_file()￼Enter
