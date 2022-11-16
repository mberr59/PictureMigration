from datetime import date
import os
import shutil
import ctypes


current_date = date.today()
home_directory = os.path.expanduser('~')
date_format = '%B %d, %Y'
formatted_date = current_date.strftime(date_format)
folder_path = os.path.join(home_directory, "Desktop", "Hunting Camera")
current_folder_path = os.path.join(folder_path, formatted_date)

if not os.path.exists(current_folder_path):
    os.makedirs(current_folder_path)

if os.listdir("F:/").__contains__("DCIM"):
    if os.listdir("F:/DCIM").__contains__("100MFCAM"):
        for file in os.listdir("F:/DCIM/100MFCAM"):
            if file.__contains__(".jpg") or file.__contains__(".mov"):
                source_file = os.path.join("F:/DCIM/100MFCAM", file)
                destination_file = os.path.join("F:/DCIM/100MFCAM", formatted_date + " " + file)
                os.rename(source_file, destination_file)
                shutil.move(destination_file, current_folder_path)
                ctypes.windll.user32.MessageBoxW(0, "Pictures have been moved successfully!", "Files Moved!", 0)
    if os.listdir("F:/DCIM").__contains__("100STLTH"):
        for file in os.listdir("F:/DCIM/100STLTH"):
            if file.__contains__(".jpg") or file.__contains__(".mov"):
                source_file = os.path.join("F:/DCIM/100STLTH", file)
                destination_file = os.path.join("F:/DCIM/100STLTH", formatted_date + " " + file)
                os.rename(source_file, destination_file)
                shutil.move(destination_file, current_folder_path)
                ctypes.windll.user32.MessageBoxW(0, "Pictures have been moved successfully!", "Files Moved!", 0)
