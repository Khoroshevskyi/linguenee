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
    try:
        #homeDir = os.path.expanduser('~') + "\\Documents" + nameOfFolder
        folder_check = os.path.isdir(HOMEDIR)
        if folder_check == True:
            return(HOMEDIR)
        else:
            directoryCreate(HOMEDIR)
            return(HOMEDIR)
    except OSError as err:
        print("Impossible to create folder" + err)

# create directory if does not exists
def directoryCreate(dir):
    print("Creating a new directory...")
    try:
        os.mkdir(dir)
    except OSError:
        print ("Creation of the directory %s failed" % dir)
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

def deletingEndSpace(word):
    word = word.replace(" ", "")
    return(word)

# saving data to userdatafile
def saveUserDataFile(data):
    dir = directoryFind()+"\\"+ USERINFOFILE
    dataList = openUserDataFile()

    dataList.append(data)
    pickle_out = open(dir, "wb")
    pickle.dump(dataList, pickle_out)
    pickle_out.close()

def create_user_file(login):
    try:
        folder_check = os.path.isdir(USERFILESDIR)
        if folder_check == True:
            pass
        else:
            directoryCreate(USERFILESDIR)
    except OSError as err:
        print("Impossible to create folder" + err)

    #CREATING login.txt
    file_name = USERFILESDIR+ "\\"+ login + ".txt"
    f= open(file_name,"w+")
    f.close()

def create_set_folder():
    try:
        folder_check = os.path.isdir(SETSDIR)
        if folder_check == True:
            pass
        else:
            directoryCreate(SETSDIR)
    except OSError as err:
        print("Impossible to create folder" + err)

def create_user_file(login):
    try:
        folder_check = os.path.isdir(USERFILESDIR)
        if folder_check == True:
            pass
        else:
            directoryCreate(USERFILESDIR)
    except OSError as err:
        print("Impossible to create folder" + err)

    #CREATING login.txt
    file_name = USERFILESDIR+ "\\"+ login + ".txt"
    f= open(file_name,"w+")
    f.close()

def create_set_file(lang, set):
    try:
        folder_check = os.path.isdir(SETSDIR+"//"+lang)
        if folder_check == True:
            pass
        else:
            directoryCreate(SETSDIR+"//"+lang)
    except OSError as err:
        print("Impossible to create folder" + err)

    file_name = SETSDIR+ "\\"+ lang +"\\"+ set + ".txt"
    f= open(file_name,"w+")
    f.close()

def set_exsists(lang, set):
    try:
        f = open(SETSDIR+ "\\"+ lang +"\\"+ set + ".txt")
        f.close()
    except IOError:
        print("File not accessible")
        return(False)


'''
if __name__=="__main__":
    directoryFind()
'''
