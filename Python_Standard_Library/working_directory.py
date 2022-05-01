from pathlib import Path
from time import ctime
import shutil

path = Path("context.txt")
# result = path.exists()
# result = path.rename("init.txt")
# result = path.unlink() # delete a file
# print(ctime(path.stat().st_ctime)) # get the creation date of a file

# path.read_bytes()

"""This is better than """
# print(path.read_text()) 

with open("context.txt", "r") as f:
    pass
    
# print(path.write_text("hello there!"))   

"""copy file from source to target"""
print(shutil.copy(source, target))