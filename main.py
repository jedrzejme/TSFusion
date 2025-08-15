import requests
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich import print
import re

url_template = input("Enter a URL: ")
url_template = re.sub(r'seg-(\d+)', r'seg-{number}', url_template)
folder = input("Enter a folder name to save the visited URLs: ")

os.makedirs(folder, exist_ok=True)

MAX_WORKERS = 100
MAX_FILES = 1000

def download_ts(n):
    url = url_template.replace("{number}", str(n))
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            filename = os.path.join(folder, f"{n}.ts")
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"Downloaded {n}.ts")
            return True
        else:
            print(f"Stopped at {n}, status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error at {n}: {e}")
        return False

def tsToMp4(folder):
    ts_files = sorted(
        (f for f in os.listdir(folder) if f.endswith('.ts')),
        key=lambda x: int(os.path.splitext(x)[0])
    )
    if not ts_files:
        exit(1)

    file_list_path = os.path.join(folder, 'files.txt')

    with open(file_list_path, 'w', encoding='utf-8') as f:
        for ts_file in ts_files:
            f.write(f"file '{ts_file}'\n")

    output_path = os.path.join(folder, f'{folder}.mp4')
    command = [
        'ffmpeg',
        '-f', 'concat',
        '-safe', '0',
        '-i', file_list_path,
        '-c', 'copy',
        '-bsf:a', 'aac_adtstoasc',
        output_path
    ]

    subprocess.run(command)

    os.remove(file_list_path)

    for ts_file in ts_files:
        os.remove(os.path.join(folder, ts_file))

# === Pobieranie plików ===
with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    futures = {executor.submit(download_ts, i): i for i in range(1, MAX_FILES + 1)}

    for future in as_completed(futures):
        success = future.result()
        if not success:
            print("Download stopped due to error or end of stream.")
            break

# === Konwersja do MP4 ===
print("Converting to MP4...")
tsToMp4(folder)
print("[bold red]Conversion complete.[/bold red]")
print("[bold blue]Press Enter to exit...[/bold blue]")
input()
