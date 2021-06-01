# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile
import os

def backupToZip(folderPath):
    #Backup the entire contents of the folder into a ZIP file
    
    #make sure folder is abssolute
    folderPath = os.path.abspath(folderPath)
    
    #Figure out the filename
    #The file name should be based on what file already exists
    number = 1
    while True:
        zipFilename = os.path.basename(folderPath) + '-' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1
        
    #Create the zip file and open it for writing
    print('Creating %s ...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    
    #Walk the ebbtire folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folderPath):
        print('Adding  files in %s ...' % (foldername))
        
        #Add current folder to the ZIP file
        backupZip.write(foldername)
        
        #Add all the files in this folder to the ZIP file
        for filename in filenames:
            if filename.startswith(os.path.basename(folderPath) + '_') and filename.endswith('.zip'):
                continue # Don't backup the backup zip files.
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')
            
os.chdir('C:\\Users\\Heidi\\Python_Class')
backupToZip(os.getcwd())