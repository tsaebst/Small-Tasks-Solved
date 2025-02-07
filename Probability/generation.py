list_of_words = ["player","understand","myth","muse","music","olivia", "union", "onion", "plenty", "abundance", "admission", "permission", "fracture", "structured", "panic", "liliac", ]
import random
import string

set_len = 10
def password_gen(set_len):
    characters = string.digits + string.punctuation
    password = ""
    for i in range(set_len):
        symb =''.join(random.choice(characters))
        password += symb
    return password



def joiner():
    passw = password_gen(set_len)
    index = random.randint(0, len(passw))
    sep = passw[index-1]
    lines = passw.split(sep,1)
    index2 = random.randint(0,len(list_of_words)-1)
    word_to_add = list_of_words[index2].upper()
    passwordik = lines[0]+word_to_add+lines[1]
    return passwordik, word_to_add

password = joiner()[0]
main_word = joiner()[1]
