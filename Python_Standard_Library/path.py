from pathlib import Path

print(dir(Path))
path = input("Enter the name of your file: ")
file_name = Path(path)
"""Check if is a file"""
# print(file_name.is_file()) 

"""Check if file exist"""
if not file_name.exists():
    print("File doesn't exist")
if not file_name.is_file():
    print(f"{path} if not a file")
else:
    print(f"{file_name.absolute()}")    
  
