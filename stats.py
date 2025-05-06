def get_nWords(words_string):
    words_list=words_string.split()
    n_words=len(words_list)
    return n_words

def get_nChar(words_string):
    char_list=list(words_string.lower())
    char_dict={}
    for i in char_list:
        char_dict[i]=char_dict.get(i,0)+1
    return char_dict