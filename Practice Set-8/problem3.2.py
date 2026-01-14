import shutil
import os

shutil.copy("tasks.txt", "my_folder")
shutil.move("notes.txt", "my_folder")
os.remove("tasks.txt")
