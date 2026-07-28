# This is a sample Python script.

import shutil
import os

current_folder=os.getcwd()
destination_folder3= "Moeezpycharmprojects"
destination_folder=os.makedirs(destination_folder3,exist_ok=True)


for files in current_folder:
    if files.endswith(".py"):
        current_folder1=os.path.join(current_folder,files)
        destination_folder2=os.path.join(destination_folder,files)
        shifting=shutil.move(current_folder1,destination_folder2)
        print(shifting)
