
word = input("Input:")
word_len = len(word)
def split(word):
    plur = ""
    if word_len % 2 == 0:
        n1 = int((word_len/2)-1)
        n2 = (n1 + 1)
        res  = plur + word[n1] + word[n2]
        return res
    else:
        n = int(((word_len + 1)/2) - 1)
        res = word[n]
        return res
print(split(word))
