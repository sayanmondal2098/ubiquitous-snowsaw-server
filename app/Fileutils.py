import shutil


shutil.make_archive('/home/user/Desktop/Filename','zip','/home/username/Desktop/Directory')

#  res = archive('INC000001','./downloads/')
def archive(filename, directory):
    shutil.make_archive( base_name = './zipfile/'+filename, format= 'zip' , base_dir= directory)
    return True

