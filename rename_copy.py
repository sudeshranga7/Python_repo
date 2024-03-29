import os
import sys
import shutil
import datetime
import re

def sanitize_filename(filename):
    # Replace consecutive underscores with a single underscore
    sanitized_filename = re.sub(r'[_]+', '_', filename)
    # Replace consecutive dots with a single dot
    sanitized_filename = re.sub(r'[.]+', '.', sanitized_filename)
    return sanitized_filename

def copy_file(source_path, destination_path, source_filename_prefix, source_filename_suffix, copy_previous_day):
    try:
        current_time = datetime.datetime.now().time()
        current_date = datetime.datetime.now().date()
        yesterday = current_date - datetime.timedelta(days=1)

        source_file_date = current_date
        source_filename_with_date = source_filename_prefix + source_file_date.strftime("%Y%m%d") + source_filename_suffix

        if copy_previous_day and current_time >= datetime.time(0, 0) and current_time <= datetime.time(0, 10):
            source_file_path = os.path.join(source_path, source_filename_with_date)
            if not os.path.exists(source_file_path):
                source_file_date = yesterday
                source_filename_with_date = source_filename_prefix + source_file_date.strftime("%Y%m%d") + source_filename_suffix

        destination_filename = os.path.basename(source_filename_prefix + source_filename_suffix)

        sanitized_destination_filename = sanitize_filename(destination_filename)
        destination_file_path = os.path.join(destination_path, sanitized_destination_filename)

        source_file_path = os.path.join(source_path, source_filename_with_date)

        if os.path.exists(source_file_path):
            shutil.copy2(source_file_path, destination_file_path)
            os.chmod(destination_file_path, 0o775)
            print("File copied successfully.")
        else:
            print(f"Source file not found: {source_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python script.py source_path destination_path source_filename_prefix source_filename_suffix [copy_previous_day]")
    else:
        try:
            source_path = sys.argv[1]
            destination_path = sys.argv[2]
            source_filename_prefix = sys.argv[3]
            source_filename_suffix = sys.argv[4]

            copy_previous_day = False
            if len(sys.argv) > 5 and sys.argv[5].lower() == 'true':
                copy_previous_day = True

            copy_file(source_path, destination_path, source_filename_prefix, source_filename_suffix, copy_previous_day)
        except Exception as e:
            print(f"An error occurred: {e}")
