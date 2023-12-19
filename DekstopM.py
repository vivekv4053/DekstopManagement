import shutil 
import os
print(" Dekstop management started")
ScreenShots = os.path.expanduser("~/Desktop/ScreenShots")
pdf = os.path.expanduser("~/Desktop/pdf")
word = os.path.expanduser("~/Desktop/wordFiles")
xls = os.path.expanduser("~/Desktop/Excel")

desktop_dir = os.path.expanduser("~/Desktop")

# if ss folder doesn't exist
if not os.path.exists(ScreenShots):
    os.makedirs(ScreenShots)
    print('Creating ScreenShot folder')


# check all files on desktop , if its a ss  move it to the screen shots folder
files_on_desktop = os.listdir(desktop_dir)
for file in files_on_desktop :
    file_dir = desktop_dir + '/' + file
    if file.startswith('Screenshot') and file.endswith('.png'):
        shutil.move(file_dir, ScreenShots)  
        print( f'Moving  {file}....')
        
        
    if file.endswith('.pdf'):
        if not os.path.exists(pdf):
            os.makedirs(pdf)
            print("Pdf folder created")
        shutil.move(file_dir,pdf)
        print(f" Moving {file}... to pdf")
        
    # for word files
    if file.endswith('.docx') or file.endswith('.docm') or file.endswith('.dotm'):
        if not os.path.exists(word):
            os.makedirs(word)
            print("word Files folder created")
        shutil.move(file_dir,word)
        print(f" Moving {file}... to word Files")
    
    if file.endswith('.xlsx'):
        if not os.path.exists(xls):
            os.makedirs(xls)
            print("Excel folder created")
        shutil.move(file_dir,xls)
        print(f" Moving {file}... to Excel")
            