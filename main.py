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

if os.listdir("D:/").__contains__("DCIM"):
    for file in os.listdir("D:/DCIM"):
        if file.__contains__(".jpg") or file.__contains__(".mov"):
            source_file = os.path.join("D:/DCIM", file)
            destination_file = os.path.join("D:/DCIM", formatted_date + " " + file)
            os.rename(source_file, destination_file)
            shutil.move(destination_file, current_folder_path)
