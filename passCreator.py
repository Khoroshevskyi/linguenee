import hashlib, binascii, os
import pickle
from progData import *

# coding password
def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

# verifiing existing password
def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

# searching for directory of file
def directoryFind():
    import os
    #nameOfFolder = "\\linguenee"
    try:
        #homeDir = os.path.expanduser('~') + "\\Documents" + nameOfFolder
        folder_check = os.path.isdir(HOMEDIR)
        if folder_check == True:
            return(HOMEDIR)
        else:
            directoryCreate()
            return(HOMEDIR)
    except OSError as err:
        print("Impossible to create folder" + err)

# create directory if does not exists
def directoryCreate():
    print("Creating a new directory...")
    try:
        os.mkdir(HOMEDIR)
    except OSError:
        print ("Creation of the directory %s failed" % HOMEDIR)
    else:
        print ("Successfully created the directory")

# creating or open existing binary user file
def openUserDataFile():
    try:
        dir = directoryFind()+"\\" + USERINFOFILE
        existFile = os.path.exists(dir)
        if existFile == True:
            pickle_in = open(dir, "rb")
            fileData = pickle.load(pickle_in)
            pickle_in.close()
            print("File already exsists")
        else:
            fileData=[]
            pickle_out = open(dir, "wb")
            pickle.dump(fileData, pickle_out)
            pickle_out.close()
            print("Creating a file")
        return fileData
    except OSError as err:
        print(err)

# saving data to userdatafile
def saveUserDataFile(data):
    dir = directoryFind()+"\\"+ USERINFOFILE
    dataList = openUserDataFile()

    dataList.append(data)
    pickle_out = open(dir, "wb")
    pickle.dump(dataList, pickle_out)
    pickle_out.close()
'''
if __name__=="__main__":
    directoryFind()
'''
