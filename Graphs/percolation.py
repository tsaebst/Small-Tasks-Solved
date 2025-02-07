import networkx as nx
import matplotlib.pyplot as plt
import random
import math
import statistics
print("Spitkovska Vladyslava AM BP-1")

# розмір сітки n*n
size = 5


class Vert:
    verts = []

    def __init__(self, i, j, state=False):
        self.i = i
        self.j = j
        self.state = state

    def append_vert(self):
        self.verts.append(self)

    def __repr__(self):
        return f"{self.i, self.j, self.state}"


class Percolation:

    def __init__(self, number):
        self.number = number
        self.num_of_el = (number * number)

        self.bottom = Vert(0, -1, True)
        self.top = Vert(-1, 0, True)

    def get_opened_count(self):
        opened = []
        for vert in Vert.verts:
            if vert.state == True:
                print(f"Block on position {vert.i, vert.j} is opened")
                opened.append(vert)
        return opened

    def check_if_block_exist(self, i, j):
        if i in range(1, self.number + 1) and j in range(1, self.number + 1):
            if i > 0 and j > 0:
                return True
        print("Block with this index does not exist in the board")
        return False

    def find_chosen_block(self, i, j):
        try:
            block_find = [block for block in Vert.verts if block.i == i and block.j == j]
            return block_find[0]
        except:
            return False

    def open(self, i, j):
        block = self.find_chosen_block(i, j)
        if block:
            block.state = True

    def add_edge(self, graph):
        opened = self.get_opened_count()
        for i in opened:
            for j in opened:
                if i != j and self.try_add_edge(i, j):
                    graph.add_edge(i, j)
                    res = nx.has_path(graph, i, j)
                    print("The path exist:", i, j, res)
                elif i != j:
                    res = nx.has_path(graph, i, j)
                    print("Path does not exist:", i, j, res)
        return

    def connect_with_im_verts(self, graph):
        verts = Vert.verts
        for vert in verts:
            if vert.i == 1:
                graph.add_edge(self.top, vert)
            elif vert.i == size:
                graph.add_edge(self.bottom, vert)

    def percolation(self, graph):
        res = nx.has_path(graph, self.top, self.bottom)
        return res

    def try_add_edge(self, ver1, ver2):
        if self.check_if_block_exist(ver1.i, ver1.j) and self.check_if_block_exist(ver2.i, ver2.j):
            if ver1.i == ver2.i and ver1.j == ver2.j + 1:
                return True
            elif ver1.i == ver2.i and ver1.j == ver2.j - 1:
                return True
            elif ver1.j == ver2.j and ver1.i == ver2.i + 1:
                return True
            elif ver1.j == ver2.j and ver1.i == ver2.i - 1:
                return True
        return False


board = Percolation(size)


def gen_board():
    for i in range(1, board.number + 1):
        for j in range(1, board.number + 1):
            vert = Vert(i, j)
            vert.append_vert()


def stats(n):
    t_list = []
    i = 0
    while i < n:
        q = experiment()
        T = q / board.num_of_el
        t_list.append(T)
        i += 1
    mean = statistics.mean(t_list)

    stddev_list = []
    for i in t_list:
        o = ((i - mean) ** 2)
        stddev_list.append(o)
    stddev = math.sqrt(sum(stddev_list) / (len(t_list) - 1))

    conf1 = mean - ((1.96 * stddev) / math.sqrt(len(t_list)))
    conf2 = mean + ((1.96 * stddev) / math.sqrt(len(t_list)))

    print(f"So in proportion to the number of blocks in system, the average amont of opened after {n} experiments is {mean} out of 1(full amount")
    print("The deviation after found limit is: ", stddev)
    print(f"The point of percolating is between {conf1} and {conf2}. It`s 95% confidence interval")




def experiment():
    for i in Vert.verts:
        i.state = False
    Graph.remove_edges_from(list(n for n in Graph.edges))
    board.connect_with_im_verts(Graph)
    iterration = 0
    while True:
        if board.percolation(Graph) == False:
            new_block_to_open = random.choice(Vert.verts)
            if new_block_to_open.state == False:
                board.open(new_block_to_open.i, new_block_to_open.j)
                board.get_opened_count()
                board.add_edge(Graph)
                iterration += 1
        else:
            break
    nx.draw(Graph, with_labels=True, font_weight='bold')
    plt.show()
    print(f"The system has a path from top to the bottom now. Program used {iterration} try/ies to cause the percolation.")
    res = len(board.get_opened_count())
    return res

# генеруємо систему
gen_board()
# створюємо граф
Graph = nx.Graph()
print(Vert.verts)
for i in Vert.verts:
    Graph.add_nodes_from([i])
board.get_opened_count()
#задаємо кількість експериментів
# statistics = PercolationStats(40)
stats(40)
# statistics.std_dev()
