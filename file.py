import os
import shutil
import time

def is_modified_in_last_24_hours(file_path):
    current_time = time.time()
    st = os.stat(file_path)
    mtime = st.st_mtime
    ctime = st.st_ctime
    return max(mtime, ctime) > current_time - 24*60*60

def update_file(file_path):
    with open(file_path, 'a') as f:
        f.write('\n' + time.ctime())

def move_file(file_path, new_folder):
    shutil.move(file_path, new_folder)

def main():
    files = os.listdir()
    if not os.path.exists('last_24hours'):
        os.makedirs('last_24hours')

    for file_name in files:
        if is_modified_in_last_24_hours(file_name):
            update_file(file_name)
            move_file(file_name, 'last_24hours')

if __name__ == "__main__":
    main()
