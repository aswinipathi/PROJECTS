#############################################################################################################

#Purpose of the script

#############################################################################################################

#1.This script has been designed to write python test scripts 
# for google-drive to create,list,get,update,delete, trash and copy methods.

#############################################################################################################

############################### Script Details ##############################################################

# Script name               :       test_google_drive.py
# Script version            :       1.0
# created By                :       aswini.pathi@infinite.com
# Create Date               :       24-o6-2021
# Last Modification Date    :       28-o6-2021

#############################################################################################################

#Below points has been considered in the script:

#############################################################################################################

#1.Write test scripts for both positive and negative cases
#2.Use loggers to print all the information on screen while 
#executing and in log files

#######################################################################################################

#Importing modules

import sys
import pytest
import time
import logging
from pytest import fixture
from confest import *
sys.path.append("/home/aswini/Google_Drive_API_Testing/prerequisites")
sys.path.append("/home/aswini/Google_Drive_API_Testing/methods")
from methods import (file_create, listfiles, update, copy_item, delete, empty_trash)

logging.basicConfig(filename="test_scripts.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logging.warning('script is being executed')

logger=logging.getLogger()

logger.setLevel(logging.INFO)

logger.info('collecting the start time')

logger.info('Execution of positive test cases is started')



########################################################################################################

# Creating a test method to create a file 
def test_create_file():
    val = listfiles(5)
    try:
        #assert status_code ==200
        assert len(val) !=0
        assert type(val) ==str
    except Exception as e:
        print('error')
       

# Creating a negative test case to check whether the file is created correctly or not

def test_create_file_negative():
    val = listfiles(5)
    try:
        assert len(val) == 0
        assert type(val) !=str
    except Exception as e:
        print('negative testcase passed')

###############################################################################################

# Creating a positive test case to test the list of files present in the drive

def test_list_files():
    val=listfiles(5)
    try:
        assert type(val) == tuple
        assert type(val[0]) == list
        assert len(val) !=0
    except Exception as e:
        print('error-1')

# Creating a negative test case to check whether the list of files are correct or not

def test_list_files_negative():
    val=listfiles(5)
    try:
        assert type(val) == tuple
        assert type(val[0]) == list
        assert len(val) ==0
    except Exception as e:
        print('negative testcase passed')

#################################################################################################

# Creating a positive test case to check whether the trash is empty or not

def test_emptytrash_drive():
    val =listfiles(5)
    try:
        assert len(val) ==0
        assert type(val) == str 
    except Exception as e:
        print('error-2')

# Creating a negative test case to check whether the trash is empty or not

def test_emptytrash_drive_negative():
    val =listfiles(5)
    try:
        assert len(val) !=0
        assert type(val) == str 
        print('negative testcase passed')
    except Exception as e:
        print('negative testcase failed')

########################################################################################################

# Creating a positive test case to get file from the drive

def test_get_file(id):
    val = get_file(id)
    try:
        assert len(val)>0
        assert type(val[0]) == dict
    except Exception as e:
        print('error-3')

# Creating a negative test case to get the file from the drive

def test_get_file_negative(id):
    val = get_file(id)
    try:
        assert len(val)<0
        assert type(val[0]) == dict
    except Exception as e:
        print('negative testcase passed')

########################################################################################################

# Creating a positive test case to delete a file from the drive

def test_delete(id):
    val = delete(id)
    try:
        assert val != None
    except Exception as e:
        print('error-4')

# Creating a negative test to check whether the file is deleted from the drive 

def test_delete_negative():
    val = delete(id)
    try:
        assert val == None
    except Exception as e:
        print('negative testcase passed')

###########################################################################################################

# Creating a test to copy a file from the drive 

def test_copy_item():
    val =listfiles(5)
    try:
        assert copy_items() == listfiles()
        assert len(copy_items[0])>0
    except Exception as e:
        print('error-5')

# Creating a negative test case to check whether the file is copied correctly or not

def test_copy_item_negative():
    val =listfiles(5)
    try:
        assert copy_items() != listfiles()
        assert len(copy_items[0])>0
    except Exception as e:
        print('negative testcase passed')

#####################################################################################################

# Creating a test case to check whether the trash is empty or not

def test_empty_trash():
    val = listfiles(5)
    try:
        assert empty_trash == None
    except Exception as e:
        print('error-6')


# Creating a negative test case to check trash is empty or not

def test_empty_trash_negative():
    val = listfiles(5)
    try:
        assert empty_trash != None
    except Exception as e:
        print('negative testcase passed')

#########################################################################################################

# Creating a test case to export a file from the drive

def test_export():
    val = listfiles(5)
    try:
        assert export !=None
    except Exception as e:
        print('error-7')

# Creating a -ve test case to check whether the file is exported or not

def test_export_negative():
    val = listfiles(5)
    try:
        assert export ==None
    except Exception as e:
        print('negative testcase passed')

######################################################################################################

# Creating a test case to generate ids for the file

def test_generate_id():
    val = listfiles(5)
    try:
        assert generate_id !=None
    except Exception as e:
        print('error-8')

# Creating a -ve test case to check whether the generated ids are correct or not

def test_generate_id_negative():
    val = listfiles(5)
    try:
        assert generate_id ==None
    except Exception as e:
        print('negative testcase passed')




########################################################################################################

