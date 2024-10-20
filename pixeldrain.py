#Log-D7
#https://t.me/Decode7Channel

import os
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
    
    # Ask the user where they want to save the file
    folder_choice = input("\nDo you want to save the file in the 'Downloads' folder? (y/n): ").lower()
    
    if folder_choice == 'y':
        # Automatically save in the Downloads folder
        download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    else:
        # Allow the user to choose a custom folder
        download_folder = input("Enter the full path of the folder where you want to save the file: ")
    
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)  # Create the directory if it doesn't exist

    file_path = os.path.join(download_folder, file_name)
    save_file(response, file_path)

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

def save_file(response, file_path):
    with open(file_path, "wb") as f:
        f.write(response.content)
    print(f"\nFile downloaded successfully and saved as {file_path}.")

if __name__ == "__main__":
    download_pixeldrain_file()
