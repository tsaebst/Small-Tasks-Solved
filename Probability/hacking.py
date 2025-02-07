
from generation import *


def random_print():
    list_of_pass = []
    for i in range(10):
        passw = joiner()
        list_of_pass.append(passw)
    print("Here`s a list of passwords among which there`s the right one:")
    for i in list_of_pass:
        print(i[0])
    index_choose = random.randint(0, len(list_of_pass)-1)
    return list_of_pass, index_choose

def similarities(password, guess):
    matches = []
    for i in range(len(guess)):
        try:
            if guess[i] == password[i].lower():
                matches.append(i)
        except:
            pass
    if len(matches) == 0:
        print("No similarities found between this word and the word from password.")
        return
    print("Some matches found on next positions:")
    if len(matches) == len(password):
        print("Congrats! Now you know the password.")
        guessed = True
        return guessed
    for i in matches:
        print(i+1, end=" ")
    print(" ")
    guessed = False
    return guessed

gen_data = random_print()
list=gen_data[0]
rand = gen_data[1]
joiner_worked = list[rand]
password = joiner_worked[0]
main_word = joiner_worked[1]
print("\tFOR THE TEST:",main_word)
def guesser():
    attempts = 10
    while attempts > 0:
        if attempts == 9:
            hint = input("Do you want to get a hint?").lower()
            if hint.startswith("y"):
                print(f"The word has {len(main_word)} letters in it.")
        print(f"You have {attempts} attempt/s left!")
        ask = input("Try to guess the word > ").lower()
        check_if_guessed = similarities(main_word, ask)
        if check_if_guessed:
            print(f"The password is: {password}")
            break
        attempts -= 1
    if attempts == 0:
        print(f"You`ve used all attempts.. The password was: {password}")

guesser()



