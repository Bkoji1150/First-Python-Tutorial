from pathlib import Path 
from pprint import pprint

from zipfile import ZipFile 

"""open file in write mode"""
'''
with ZipFile("files.zip", "w") as zip:
    for path in Path("../Functions").rglob("*.*"):
        zip.write(path)
'''
with ZipFile("files.zip", "r") as zip:
    zip_files = zip.namelist()
    for each_file in zip_files:
        info = zip.getinfo(each_file)
        print(f"file name: {each_file}, size is: {info.file_size}, compress size: {info.compress_size}")
        zip.extractall("extract")
  