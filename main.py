from datetime import date
import os
import shutil


current_date = date.today()
home_directory = os.path.expanduser('~')
date_format = '%B %d, %Y'
formatted_date = current_date.strftime(date_format)
folder_path = os.path.join(home_directory, "Desktop", "Hunting Camera")
current_folder_path = os.path.join(folder_path, formatted_date)

if not os.path.exists(current_folder_path):
    os.makedirs(current_folder_path)

for file in os.listdir("D:/"):
    if file.__contains__(".jpg") or file.__contains__(".mov"):
        shutil.move("D:/" + file, current_folder_path)

print(os.listdir("D:/"))
