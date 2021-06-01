# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile
import os

def backupToZip(folderPath):
    #Backup the entire contents of the folder into a ZIP file
    
    #make sure folder is abssolute
    folder = os.path.abspath(folder)
    
    #Figure out the filename
    #The file name should be based on what file already exists
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '-' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1
        
    #Create the zip file and open it for writing
    print('Creating %s ...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')


backupToZip(os.cwd())