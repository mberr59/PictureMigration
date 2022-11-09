from datetime import date
from pathlib import Path
import os


current_date = date.today()
home_directory = os.path.expanduser('~')
date_format = '%A, %B %d, %Y'
folder_path = os.path.join(home_directory, "Desktop", "Hunting Camera")
current_folder_path = os.path.join(folder_path, current_date.strftime(date_format))

if not os.path.exists(current_folder_path):
    os.makedirs(current_folder_path)

print("Today's date is ", current_date)
