def open_dict(file_name):
    data = open(file_name,"r")
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

    for k in diction_arr:
        print(k)

    true_arr_list = tru_arr_creator(diction_arr )

    #for k in true_arr_list:
    #    print(k)

def tru_arr_creator(diction_arr):
    # creating true array of words
    list_item_nr = 0
    true_arr_list = []
    while (list_item_nr < len(diction_arr)):
        for item in diction_arr[list_item_nr]["id_word"]:
            if len(item) > len("<pos>"):
                if (item[0:len("<pos>")] == "<pos>"):
                    pos = item
                    break
                else:
                    pos = ""
        true_arr ={
        "id":  diction_arr[list_item_nr]["id_word"][0],
        "word": diction_arr[list_item_nr]["id_word"][2],
        "pron": diction_arr[list_item_nr]["id_word"][3],
        "pos": pos
        }
        list_item_nr = list_item_nr + 1
        true_arr_list.append(true_arr)
    true_arr_list = array_modifier(true_arr_list, "id", '<entry xml:id="', '>"' )
    true_arr_list = array_modifier(true_arr_list, "word", '<orth>', '</orth>' )
    true_arr_list = array_modifier(true_arr_list, "pron", '<pron>', '</pron>' )
    true_arr_list = array_modifier(true_arr_list, "pos", '<pos>', '</pos>' )

    return(true_arr_list)

# deleting all unneccery char elements
def array_modifier(true_arr_list, key, item_front_del, item_back_del ):
    item_nr = 0
    while (item_nr  < len(true_arr_list)):
        if (true_arr_list[item_nr][key] != ""):
            true_arr_list[item_nr][key] = true_arr_list[item_nr][key][len(item_front_del):]
            true_arr_list[item_nr][key] = true_arr_list[item_nr][key][:-len(item_back_del)]
        item_nr = item_nr + 1
    return(true_arr_list)

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

# separating words to few arrays by word
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

if __name__ == '__main__':
    open_dict("E://Przyrod-master//1//1.1-pracownia inform//a.xml")
