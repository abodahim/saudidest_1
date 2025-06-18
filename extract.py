import zipfile
import os

def extract_zip_if_needed(zip_path, extract_to):
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

if __name__ == "__main__":
    if os.path.exists("templates.zip"):
        extract_zip_if_needed("templates.zip", "templates")
    if os.path.exists("static.zip"):
        extract_zip_if_needed("static.zip", "static")
