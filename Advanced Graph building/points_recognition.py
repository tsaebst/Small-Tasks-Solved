import random
print("Spitkovska Vladyslava")
import matplotlib.pyplot as plt


class Point:


    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    pint_box = []

    def add(self):
        self.pint_box.append(self)
        self.draw()

    def connect(self, q, r, s):
        self.draw_to(q)
        self.draw_to(r)
        self.draw_to(s)

    def draw(self):
        if chosen == "rs1423":
            plt.plot(self.x, self.y, marker='o', markersize=1, markeredgecolor='green', markerfacecolor='pink')
            return 
        plt.plot(self.x, self.y, marker='o', markersize=4, markeredgecolor='green', markerfacecolor='pink')

    def draw_to(self, point):
        plt.plot([self.x, point.x], [self.y, point.y], linestyle='--', linewidth=0.3, color='black')

    def slope_to(self, that):
        # градієнт
        if self == that:
            return float('-inf')
        elif self.y == that.y:
            return 0
        elif self.x == that.x:
            return float('inf')
        else:
            return (that.y - self.y) / (that.x - self.x)

    def __lt__(self, other):
        if self.y < other.y:
            return True
        elif self.y == other.y:
            return self.x < other.x
        return False

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y


txts = ["input40","input50","input56", "input100", "input8", "rs1423"]
chosen = random.choice(txts)

file_path = f"/Users/your/path/txts/{chosen}.txt"


def read_coordinates_from_file(filename):
    with open(file_path, 'r') as fp:
        fp.readline()
        for line in fp:
            coordinates = line.split()
            point = Point(int(coordinates[0]), int(coordinates[1]))
            point.add()


print(f"We've chosen the file {chosen} to check if we can connect any 4 or more pint_box with one line")


# часозатратний варіянт (Завдання 1)
def brute_f():
    lenght = len(Point.pint_box)
    for i in range(lenght):
        for j in range(i+1, lenght):
            for k in range(j+1, lenght):
                for m in range(k+1, lenght):
                    p = Point.pint_box[i]
                    q = Point.pint_box[j]
                    r = Point.pint_box[k]
                    s = Point.pint_box[m]
                    # перевірка градієнту
                    st1 = p.slope_to(q)
                    st2 = p.slope_to(r)
                    st3 = p.slope_to(s)
                    if st1 == st3 == st2:
                        p.connect(r, q, s)
                        print(f"New line was found through next pint_box: {p.x,p.y}, {q.x, q.y}, {r.x, r.y}, {s.x, s.y}")


# Завдання 2
def fast():
    for point_a in Point.pint_box:
        s_all = []
        for point_b in Point.pint_box:
            if point_b != point_a:
                goto = point_a.slope_to(point_b)
                s_all.append((point_b, goto))
        s_all.sort(key=lambda x: x[1])
        matches = 1
        matches_list = []
        for i in range(len(s_all) - 1):
            if s_all[i][1] == s_all[i + 1][1]:
                matches += 1
                if s_all[i][1] not in matches_list :
                    matches_list.append((s_all[i][0].x,s_all[i][0].y))
                if s_all[i+1][1] not in matches_list:
                    matches_list.append((s_all[i+1][0].x, s_all[i][0].y))
            else:
                matches = 1
            if matches >= 3:
                for j in range(i - matches + 2, i + 1):
                    point_a.draw_to(s_all[j][0])
                    if len(matches_list) == 4:
                        print("New line was found through next pint_box:", ",".join( repr(e) for e in matches_list))
                        matches_list = []





read_coordinates_from_file(file_path)
# brute_f()
fast()
plt.show()

