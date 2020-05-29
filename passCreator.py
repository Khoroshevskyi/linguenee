"""
Engine of the program. All information that is writing to database and reading info from it
is using functions form this file (from passCreator)
"""
import hashlib, binascii, os
import pickle
from progData import *

#####################################################################
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

def deletingEndSpace(word):
    word = word.replace(" ", "")
    return(word)

#####################################################################
# searching for directory and if not exsist - create - main directory
def directoryFind(dir):
    try:
        folder_check = os.path.isdir(dir)
        if folder_check == True:
            print("Directory already exsists %s" %dir)
            return(dir)
        else:
            directoryCreate(dir)
            return(dir)
    except OSError as err:
        print("Impossible to create folder" + err)

# create directory
def directoryCreate(dir):
    try:
        os.mkdir(dir)
    except OSError:
        print ("Creation of the directory %s failed" % dir)
    else:
        print ("Successfully created the directory: %s"% dir)

################################################################
# Openings binary files in wich is one array, if not exsists - func create it
def open_list_file(dir, file_name):
    try:

        dir_name_file = directoryFind(dir)+"\\" + file_name
        existFile = os.path.exists(dir_name_file)
        if existFile == True:
            pickle_in = open(dir_name_file, "rb")
            fileData = pickle.load(pickle_in)
            pickle_in.close()
            print("File: %s already exsists" % dir)

        else:
            fileData=[]
            pickle_out = open(dir_name_file, "wb")
            pickle.dump(fileData, pickle_out)
            pickle_out.close()
            print("Creating a file %s" % dir)
        return fileData
    except OSError as err:
        print(err)

###########################
# saving data to userdatafile
def saveUserDataFile(data):
    dir = directoryFind(HOMEDIR)+"\\"+ USERINFOFILE
    dataList = open_list_file(HOMEDIR,USERINFOFILE)
    dataList.append(data)
    pickle_out = open(dir, "wb")
    pickle.dump(dataList, pickle_out)
    pickle_out.close()

# creating folders with User and users for tests and sets
def create_user_file(login):
    directoryFind(USERFILESDIR)
    userDir = USERFILESDIR + "\\" + login
    directoryFind(userDir)

    u_sets_dir = userDir + "\\" + "u_sets"
    directoryFind(u_sets_dir)
    u_tests_dir = Usets_dir = userDir + "\\" + "u_tests"
    directoryFind(u_tests_dir)

    # creating file where will be info with sets that user created
    open_list_file(userDir, USERSETSFILE)
############

# creating set file with info file, who have this set in use
def create_set_file(login, lang, set_name):
    dir = directoryFind(SETSDIR)
    file_name = set_name + ""
    file_dir_name = dir + "\\" + file_name

    #data = { "#language": lang }
    word_list = open_list_file(dir, file_name)

    pickle_out = open(file_dir_name, "wb")
    pickle.dump(word_list, pickle_out)
    pickle_out.close()

    add_words_user_use(login, set_name, [])
    add_words_user_test(login, set_name, [])

    open_and_add_set_file(login, set_name)
    add_array_of_users(login, set_name)

# function for addsetlist to add new set for user
def add_words2(login, set_name):
    dir = directoryFind(SETSDIR)
    file_name = set_name
    file_dir_name = dir + "\\" + file_name
    word_list = open_list_file(dir, file_name)
    add_words_user_use(login, set_name, word_list)
    add_words_user_test(login, set_name, word_list)

###################################################
# adding file with learn set in user directory
def add_words_user_use(login, set_name, words_added):
    # words_added = [{"word": word, "meaning":''},{...},...]
    userDir = USERFILESDIR + "\\" + login + "\\u_sets"
    set_name_file = set_name + ""
    file_dir_name = userDir + "\\" + set_name_file
    learn_list = []
    for word in words_added:
         word["score"] = 0
         learn_list.append(word)
    pickle_out = open(file_dir_name, "wb")
    pickle.dump(learn_list, pickle_out)
    pickle_out.close()

# adding file with test set in user directory
def add_words_user_test(login, set_name, words_added):
    # words_added = [{"word": word, "meaning"},{...},...]
    userDir = USERFILESDIR + "\\" + login + "\\u_tests"
    set_name_file = set_name + ""
    file_dir_name = userDir + "\\" + set_name_file
    list_prev = open_list_file(userDir, set_name_file)
    list_prev = []
    for word in words_added:
         word["passed"] = False
         list_prev.append(word)
    pickle_out = open(file_dir_name, "wb")
    pickle.dump(list_prev, pickle_out)
    pickle_out.close()
#####################################

# saving changed data in learning set of user
def edit_user_learing_set(UserID, SetName, data):
    userDir = USERFILESDIR + "\\" + UserID + "\\u_sets"
    file_dir_name = userDir + "\\" + SetName
    pickle_out = open(file_dir_name, "wb")
    pickle.dump(data, pickle_out)
    pickle_out.close()

# saving changed data in test set of user
def edit_user_test_set(UserID, SetName, data):
    userDir = USERFILESDIR + "\\" + UserID + "\\u_sets"
    file_dir_name = userDir + "\\" + SetName
    pickle_out = open(file_dir_name, "wb")
    pickle.dump(data, pickle_out)
    pickle_out.close()
####################################

# creating, or open file in user folder with array
def open_and_add_set_file(login, set):
    userDir = USERFILESDIR + "\\" + login
    file_dir_name = userDir +"\\"+ USERSETSFILE   # USERSETSFILE = user_sets.txt
    data = open_list_file(userDir, USERSETSFILE)
    data.append(set)
    pickle_out = open(file_dir_name, "wb")
    pickle.dump(data, pickle_out)
    pickle_out.close()

# adding in folder of sets file with array of users who use it
def add_array_of_users(login, set_name):
    dir = directoryFind(SETSDIR)
    file_name = set_name + '.info'
    file_dir_name = dir + "\\" + file_name

    data = open_list_file(dir, file_name)

    data.append(login)
    pickle_out = open(file_dir_name, "wb")
    pickle.dump(data, pickle_out)
    pickle_out.close()

# checking if this set already exsists
def set_exsists(set):
    file_path = SETSDIR + "\\" + set + ''
    if (os.path.exists(file_path)):
        return(True)
    else:
        return(False)

# open list of users who is using this set
def openUserSetList(login):
    userDir = USERFILESDIR + "\\" + login
    file_name = userDir +"\\"+ USERSETSFILE
    sets = open_list_file(userDir, USERSETSFILE)
    return(sets)

# open user sets
def open_set_in_use(login):
    dir = USERFILESDIR + "\\"+ login +"\\" + "u_sets"
    sets_in_use = []
    for root, dirs, files in os.walk(dir):
        for filename in files:
            sets_in_use.append(filename)
    return(sets_in_use)

# all sets avaliable in the program
def openSetsAvailable():
    dir = SETSDIR
    sets_in_use = []
    for root, dirs, files in os.walk(dir):
        for filename in files:
            if filename[-5:] != ".info":
                sets_in_use.append(filename)
    return(sets_in_use)

# saving modified set
def save_set(set, set_name):
    # set = [{"word": "word", "meaning": "meaning"},{},{}]
    dir = SETSDIR+"\\"+ set_name
    pickle_out = open(dir, "wb")
    pickle.dump(set, pickle_out)
    pickle_out.close()

# saving sets to users directories
def seve_test_score(UserID, setName, set_doc):
    userDir = USERFILESDIR + "\\" + UserID + "\\u_tests"
    file_dir_name = userDir + "\\" + setName

    pickle_out = open(file_dir_name, "wb")
    pickle.dump(set_doc, pickle_out)
    pickle_out.close()

# making percent in userWindow
def add_percents(UserID):
    plus = 0
    minus = 0
    user_sets = open_set_in_use(UserID)

    for set in user_sets:
        userDir = USERFILESDIR + "\\" + UserID + "\\u_tests"
        file_dir_name = userDir + "\\" + set
        words_in_set = open_list_file(userDir, set)
        for word in words_in_set:
            if word["passed"] == True:
                plus += 1
            else:
                minus += 1
    if (plus+minus == 0):
        plus = 1
    percent = plus*100/(plus+minus)
    return(percent)
