
ln1 = input("Створити стрічку 1:")
ln2 = input ("Створити стрічку 2:")

n1=len(ln1)
n2=len(ln2)
result = n1 == n2

i=0
processed_chars = ""
while i < n1 and result:

    is_ln1_char_processed = processed_chars.__contains__(ln1[i])
    is_ln2_char_processed = processed_chars.__contains__(ln2[i])

    if not is_ln1_char_processed and not is_ln2_char_processed:
        processed_chars = processed_chars + ln1[i] + ln2[i]
        ln1_char_indexes = [i]
        ln2_char_indexes = [i]
        j = i + 1

        while j < n1:
            if ln1[i] == ln1[j]:
                ln1_char_indexes.append(j)
            if ln2[i] == ln2[j]:
                ln2_char_indexes.append(j)
            j = j + 1

        print("Індексний лист стрічки 1, елем.", ln1[i], ":", ln1_char_indexes)
        print("Індексний лист стрічки 2, елем.", ln2[i], ":", ln2_char_indexes)
        print("Порівнюємо", ln1[i], "і", ln2[i])

        result = ln1_char_indexes == ln2_char_indexes
    elif is_ln1_char_processed and not is_ln2_char_processed:
        result = False
    elif not is_ln1_char_processed and is_ln2_char_processed:
        result = False
    i = i + 1
print(result)