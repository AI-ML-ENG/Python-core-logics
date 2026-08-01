import os
import shutil
folder=os.getcwd()
print(folder)
files=os.listdir(folder)
print(files)
new_folder="non_python_files_or_sunfolder"
for filein in files:
    old_folder_files=os.path.join(folder,filein)
    new_folder_files=os.path.join(new_folder,filein)
    if filein == "Moeezpycharmprojects":
        continue
    if not filein.endswith(".py"):
        shifting=shutil.move(old_folder_files,new_folder_files)
        print(shifting)


