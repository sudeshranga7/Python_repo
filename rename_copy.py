import os
import sys
import shutil
import datetime

def copy_file(source_path, destination_path, source_filename):
    current_time = datetime.datetime.now().time()
    current_date = datetime.datetime.now().date()
    yesterday = current_date - datetime.timedelta(days=1)

    source_file_date = current_date
    if current_time >= datetime.time(0, 0) and current_time <= datetime.time(0, 10):
        if not os.path.exists(os.path.join(source_path, f"{source_filename}{current_date.strftime('%Y%m%d')}")):
            source_file_date = yesterday

    source_filename_with_date = source_filename + source_file_date.strftime("%Y%m%d")
    destination_filename = os.path.basename(source_filename) + ".txt"

    source_file_path = os.path.join(source_path, source_filename_with_date)
    destination_file_path = os.path.join(destination_path, destination_filename)

    if os.path.exists(source_file_path):
        shutil.copy2(source_file_path, destination_file_path)
        os.chmod(destination_file_path, 0o775)
        print("File copied successfully.")
    else:
        print("Source file not found.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py source_path destination_path source_filename")
    else:
        source_path = sys.argv[1]
        destination_path = sys.argv[2]
        source_filename = sys.argv[3]

        copy_file(source_path, destination_path, source_filename)
