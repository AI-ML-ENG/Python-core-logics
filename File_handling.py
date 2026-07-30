import os
import shutil
create_folder = "Moeezpycharmprojects"
os.makedirs(create_folder, exist_ok=True)
current_folder=os.getcwd()
print(current_folder)
files_saved = os.listdir(current_folder)
print(files_saved)
for file in files_saved:
    if file.endswith(".py"):
        new_folder=os.path.join(create_folder,file)
        old_folder=os.path.join(current_folder,file)
        shutil.move(old_folder,new_folder)




        #with open(new_folder,"w") as f:
         #   f.write(file)


#files1 = ['report.log', 'debug.tmp', 'good.py']

#for files_save in files1:
   # files_saved = os.path.join(create_dummy_folder, files_save)

    #with open(files_saved, 'w') as f:
     #   f.write(files_save)

#    if files_saved.endswith(".log"):
 #       size = os.path.getsize(files_saved)

  #      if size > 0:
   #        print("successfully moved to archived folder")
    #    else:
     #       os.remove(files_saved)
      #      print("successfully deleted the unnecessary files")
    #else:
     #   print("all cleared that's it")
