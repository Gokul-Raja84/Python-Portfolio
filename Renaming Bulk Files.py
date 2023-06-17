'''

Import the module - library
Enter exact path of the Folder - Files, you want to Rename
Run the Program and check the Renamed Files

'''


import os

def main():
    i = 0
    path = "C:/Users/"  #Enter exact path of the Files here
    for filename in os.listdir(path):
        my_dest = "img" + str(i) + ".jpg" #You can also convert the File Type, by entering the File type you want
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1

if __name__ == '__main__':
    main()