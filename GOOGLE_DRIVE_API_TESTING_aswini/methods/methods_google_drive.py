#####################################################################################

# Purpose of the Script

#####################################################################################

#1. This Script has been designed to write python script
# For Google-Drive to create , List, Get, Update , upload,
#  trash and copy methods.

#####################################################################################

############################### Script Details ######################################

# Script name               :       methods_google_drive.py
# Script version            :       1.0
# created By                :       aswini.pathi@infinite.com
# Create Date               :       24-o6-2021
# Last Modification Date    :       28-o6-2021

#####################################################################################

# Below points has been considered in the script:

#####################################################################################

# 1. Writing scripts to test the Google-Drive
# 2. Writting loggers to print all the steps 
# of the process,in log files.

#####################################################################################

# Importing Modules

from apiclient.http import MediaFileUpload
import sys
sys.path.append('/home/aswini/google_drive_aswini/prerequsites')
from quickstart import main
import logging
service = main()


logging.basicConfig(filename="method_scripts.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logging.warning('script is being executed')

logger=logging.getLogger()

logger.setLevel(logging.INFO)

logger.info('collecting the start time')

logger.info('Execution of positive test cases is started')

logging.basicConfig(filename="test_scripts.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
#####################################################################################

# Creating a file method to create file

def create_file():
    service = main()
    file_metadata = {
        'name': 'API',
        'mimeType': 'application/vnd.google-apps.folder'
    }
    file = service.files().create(body=file_metadata,
                                        fields='id').execute()
    print('folder id: %s',file.get('id'))

#####################################################################################

# Creating a file list method to list file

def list_files(size):
    result = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = result.get('files', [])
    if not items:
        print('no Files:')

    else:
        print('files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))

        return items

#####################################################################################

# Creating a upload file method to upload  file

def upload_file(filename, filepath):
    file_metadata = {'name':'file.txt'}
    media = MediaFileUpload('/home/aswini/Desktop/link.txt',
                            mimetype='file/txt')

    file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print('File Id: %s' % file.get('id'))
    return file

#####################################################################################

# Creating a update file  method to update file

def update_file(id):
    file = service.files().get(fileId=id).execute()
    file ['name'] = 'file.txt'
    return file

#####################################################################################

# Creating a copy file method to copy file

def copy_item(id):
    file = service.files().copy(fileId=id).execute()
    print(file)
    return type(id)    

#####################################################################################

# Creating a get file method to get file

def get_file(id):
    files = service.files().get(fileId=id).execute()
    print(files)
    return type(id)

#####################################################################################

# Creating a delete file method to delete file

def delete_file(id):
    file = service.files().delete(fileId=id).execute()
    print(file)
    return type(file)

#####################################################################################

# Creating a empty trash method 

def empty_trash(id):
    file = service.files().emptyTrash().execute()
    print(file)
    return type(file)

#####################################################################################

# Creating a export file method to export file

def export(id):
    file = service.files().export(fileId='1ooSt4RpVAwXwMar6p3WDInGLxK6wgR8K').execute()
    print(file)
    return type(file)

#####################################################################################

# Creating a generate_id method 

def generate_id():
    file = service.files().generateIds().execute()
    print(file)

#upload_file('file.txt', '/home/aswini/Desktop/windows folders/link.txt')

create_file()
#list_files(5)
update_file('1no6xuR5g2JOJAhmz3t-Hi6wAUO1hzzvA')
copy_item('1dw_yh2w7G7h372kXISlAfo6ypDofbSFD')
get_file('1dw_yh2w7G7h372kXISlAfo6ypDofbSFD')
#generate_id()
delete_file('1dw_yh2w7G7h372kXISlAfo6ypDofbSFD')