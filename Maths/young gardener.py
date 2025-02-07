print("Spitkovska Vladyslava AM BP-1")
layers = int(input(">>>"))


def layers_count(layers):
    if layers == 0:
        return 1
    elif layers < 0:
        print("Wrong integer.")
        return
    res = layers*(layers+1)
    return res+1


print(layers_count(layers))