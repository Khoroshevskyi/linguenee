import numpy as np
import os

def main(folder, w_file_name):
    all_arrays = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    directory = dir_path + "\\"+ folder
    print(dir_path)
    for filename in os.listdir(directory):
        true_arr_list1 = xml_to_list_dict(directory+"//"+filename)
        all_arrays = np.concatenate((all_arrays, true_arr_list1), axis=0)

    f_name = dir_path+"\\"+w_file_name
    write_to_file(all_arrays, f_name)

    #for k in all_arrays:
    #    print(k)

# making list of dictionaries for words on one letter
def xml_to_list_dict(filename):
    data = open(filename, "r", encoding="utf8")
    contents = data.read()
    contents = contents.replace("   ", "")
    list_of_words = contents.split("\n")
    dict_list = make_word_list(list_of_words, "<entry")
    dict_list = delete_not_word(dict_list)
    list_item_nr = 0
    for k in dict_list:
        dict_list[list_item_nr] = make_word_list(k, '<sense level="0"')
        list_item_nr = list_item_nr + 1

    diction_arr = dict_creator(dict_list)
    diction_arr = ref_in_id_to_sense0(diction_arr)

    true_arr_list = tru_arr_creator(diction_arr)
    return(true_arr_list)

# write words to file
def write_to_file(list, filename):
    k = 0
    with open(filename, 'w+', encoding="utf8") as filehandle:
        for listitem in list:
            filehandle.write('%s\n' % listitem)
            k += 1
    print('file', filename, 'with', k,'lines has been created' )

# main array of dicts creator
def tru_arr_creator(diction_arr):
    list_item_nr = 0
    true_arr_list = []
    while (list_item_nr < len(diction_arr)):
        translit_arr = []
        k = 0
        while k < len(diction_arr[list_item_nr]["sense_0"]):
            translit_arr.append(sense0_modifier(diction_arr[list_item_nr]["sense_0"][k]))
            k = k + 1

        for item in diction_arr[list_item_nr]["id_word"]:
            if len(item) > len("<pos>"):
                if (item[0:len("<pos>")] == "<pos>"):
                    pos = item
                    break
                else:
                    pos = ""
        true_arr ={
        "id":  word_modifier(diction_arr[list_item_nr]["id_word"][0],'<entry xml:id="', '>"'),
        "word": word_modifier(diction_arr[list_item_nr]["id_word"][2], '<orth>', '</orth>' ),
        "pron": word_modifier(diction_arr[list_item_nr]["id_word"][3],  '<pron>', '</pron>' ),
        "pos": word_modifier(pos, '<pos>', '</pos>' ),
        "translit": translit_arr
        }
        list_item_nr = list_item_nr + 1
        true_arr_list.append(true_arr)

    k = 0
    while (k < len(true_arr_list)):
        if (true_arr_list[k]["pos"] != ''):
            true_arr_list[k]["translit"][0]["pos"] = true_arr_list[k]["pos"]
        del true_arr_list[k]["pos"]
        k = k + 1
    return(true_arr_list)

# word meaning creator, making all together
def sense0_modifier(sense_list):
    translate = {
                    "pos": "",
                    "translation": [],
                    "english_m":{
                                "eng": "",
                                "idarex": "",
                                "translation": []
                                },
                }

    ref = '<ref>'
    ref_back = '</ref>'

    word0 = '<quote xml:lang="en">'
    word0_back = "</quote>"

    word01 = '<note type="idarex" xml:lang="en">'
    word01_back = '</note>'

    word1 = "<quote>"
    word1_back = "</quote>"

    word2 = '<pos>'
    word2_back = '</pos>'

    item = 0
    cit_nr = 0
    word_status = 0
    while (item < len(sense_list)):

        if (cit_nr == 0):
            word_status = 0

        if (word_status == 1):
            if (sense_list[item][0:len('<cit')] == '<cit'):
                cit_nr = cit_nr + 1
            elif (sense_list[item] == '</cit>'):
                cit_nr = cit_nr - 1
            elif (sense_list[item][0:len(word1)] == word1):
                translate["english_m"]["translation"].append(word_modifier(sense_list[item], word1, word1_back))
                word_status = 0
            elif (len(sense_list[item]) > len(word01)):
                if (sense_list[item][0:len(word01)] == word01):
                    translate["english_m"]["idarex"] = word_modifier(sense_list[item], word01, word01_back)

        if (len(sense_list[item]) > len(ref)):
            if (sense_list[item][0:len(ref)] == ref):
                translate["translation"].append(word_modifier(sense_list[item], ref, ref_back))

        if (len(sense_list[item]) > len(word0)):
            if (sense_list[item][0:len(word0)] == word0):
                translate["english_m"]["eng"] = word_modifier(sense_list[item], word0, word0_back)
                word_status = 1
                cit_nr = cit_nr + 1

        if (len(sense_list[item]) > len(word1)):
            if (sense_list[item][0:len(word1)] == word1):
                translate["translation"].append(word_modifier(sense_list[item], word1, word1_back))

        if (len(sense_list[item]) > len(word2)):
            if (sense_list[item][0:len(word2)] == word2):
                translate["pos"] = (word_modifier(sense_list[item], word2, word2_back))
        item = item +1

    return(translate)

# deleting xml poznachky
def word_modifier(word, item_front_del, item_back_del ):
    word = word[len(item_front_del):]
    word = word[:-len(item_back_del)]
    return word

# if there is meaning in id_slowo put this meaning to sense_0 first item
def ref_in_id_to_sense0(diction_arr):
    list_nb = 0
    for list_item in diction_arr:
        for each_slowo in list_item["id_word"]:
            if len(each_slowo) >= len("<ref>"):
                if each_slowo[0:len("<ref>")] == "<ref>":
                    diction_arr[list_nb]["sense_0"][0].append(each_slowo)
        list_nb = list_nb + 1
    return(diction_arr)

# creating list of dictionaries with items: id_word and selnse_0
# id_word is word, pron and language used
def dict_creator(dict_list):
    diction_arr = []
    for m in dict_list:
        diction = {
            "id_word": m[0],
            "sense_0": m[1:]
        }
        diction_arr.append(diction)
    return diction_arr

# separating words to few arrays by delimiter (delim)
# this function we use to separate words and meanings
def make_word_list(list, delim):
    dict_list = []
    list_number = 0
    list_elements = []
    for i in list:
        if (len(i) > len(delim)):
            if (i[0:len(delim)] == delim):
                dict_list.append(list_elements)
                list_number = list_number +1
                list_elements = []
        list_elements.append(i)
    dict_list.append(list_elements)

    return dict_list

# deleting items in array without pointer <entry
def delete_not_word(dict_list):
    entry = "<entry"
    for nr in dict_list:
        for i in range(0, 5):
            if nr[0][i] != entry[i]:
                dict_list.pop(0)
                break
    return(dict_list)

# initializing main function
if __name__ == '__main__':
    main("all_words", 'dictionary.txt')
