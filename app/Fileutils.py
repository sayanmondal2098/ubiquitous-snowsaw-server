import shutil
import os
import shutil

#  res = archive('INC000001','./downloads/')
def archive(filename, directory):
    shutil.make_archive( base_name = './zipfile/'+filename, format= 'zip' , base_dir= directory)
    return True

def cleanupDirctory(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_dir() and not entry.is_symlink():
                shutil.rmtree(entry.path)
            else:
                os.remove(entry.path)
    return True
