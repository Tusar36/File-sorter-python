import os
import shutil

path = input("Enter path name \n")

if(os.path.exists(path)):
    os.chdir(path)
else:
    print("Path dose not exist")    
    exit()

files = os.listdir()

for f in files:
    extName = str(os.path.splitext(f)[1])
    if(extName==''):
        continue
    folderName = extName[1:len(extName)]
    folderPath = os.path.join(path,folderName)
    CurrentFilePath = os.path.join(path,f)
    NewFilePath = os.path.join(folderPath,f)
    if(os.path.exists(folderPath)):
        shutil.move(CurrentFilePath,NewFilePath)
    else:
        os.mkdir(folderName)    
        shutil.move(CurrentFilePath,NewFilePath)

print("files sorted")    

