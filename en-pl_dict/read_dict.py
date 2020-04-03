import ast

def main(filename):
    meaning_list = read_finished_file('dictionary.txt')
    find_word(meaning_list)

# read created file
def read_finished_file(filename):
    words = []
    # open file and read the content in a list
    with open(filename, 'r', encoding="utf8") as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentPlace = line[:-1]
            words.append(ast.literal_eval(currentPlace))

    return(words)

# find word
def find_word(true_arr_list):
    while True:
        try:
            word_find=input("Type the word you want to find? ")
            try:
                slowo = next(item for item in true_arr_list if item["word"] == word_find)
                for xx in slowo["translit"]:
                    for x in (xx["translation"]):
                        print(x)
                print(slowo)
            except:
                print("There is no word")
        except EOFError:
            break

if __name__ == '__main__':
    main('dictionary.txt')
