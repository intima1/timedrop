#Import Python libraries we need
import os
import time

#Define path to camera recordings
path="/home/pi/MotionTempFiles/"

def upload_files():
    if not os.path.exists(path):
        return
#   Get files from the directory    
    dir_list = os.listdir(path)
    first_10 = dir_list[:10]
    for file_name in first_10:
#       Define two variables for each file, the full file path and the time it was last modified
        file_full_path = path + file_name
        file_last_modified = os.path.getmtime(file_full_path)
#       Some debug stuff
#        print file_full_path
#        print file_last_modified
#       If the file hasn't been modified in the last three minutes, upload, else leave alone
        if(time.time()-file_last_modified >= 180):
            cmd = "/home/pi/DropboxSync/dropbox_uploader.sh upload " + file_full_path + " /"
#           Upload the file and remove it once uploaded
            os.system(cmd)
            os.remove(file_full_path)
        else:
#           Print the fact that we're doing nothing
            cmd = "echo " + file_full_path + " left alone as it's too recent"     
            os.system(cmd)

if __name__ == "__main__":
    upload_files()
