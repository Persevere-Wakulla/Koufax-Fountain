# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file creation and modification times)

import shutil

shutil.copyfile('test.txt', 'c:\\Users\\PCC-04\\Desktop\\copy.txt') #src,dst