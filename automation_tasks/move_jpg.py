import os
import shutil
print(os.listdir())
print(os.getcwd())
current_folder="D:\\CODEALPHA_INTERNSHIP\\automation_tasks"
destination_folder="D:\\CODEALPHA_INTERNSHIP\\all_jpg_files"
for file_name in os.listdir(current_folder):
    if(file_name.lower().endswith(".jpg") or file_name.lower().endswith(".jpeg")):
        source_path=os.path.join(current_folder,file_name)
        destination_path=os.path.join(destination_folder,file_name)
        shutil.move(source_path,destination_path)
        print(f"moved {file_name} from {current_folder} to {destination_folder}")