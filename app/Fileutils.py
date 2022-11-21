import shutil

#  res = archive('INC000001','./downloads/')
def archive(filename, directory):
    shutil.make_archive( base_name = './zipfile/'+filename, format= 'zip' , base_dir= directory)
    return True

