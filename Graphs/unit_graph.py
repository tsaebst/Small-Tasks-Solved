import networkx as nx
import matplotlib.pyplot as plt
from percolation import *
G = nx.Graph()

class test:

    def __init__ (self, i, j):
        self.i = i
        self.j = j


n = Percolation()

G.add_nodes_from([1, n])

G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(2, 5)
G.add_edge(5, 6)
G.add_edge(6, 9)
G.add_edge(4, 7)
G.add_edge(7, 8)


print(nx.has_path(G, 1, 8))


obj1 = test(1, 1)
obj2 = test(1, 2)
obj3 = test(2, 1)
obj4 = test(2, 2)

F = nx.Graph()

F.add_node(obj1)
F.add_node(obj2)
F.add_node(obj3)
F.add_node(obj4)

F.add_edge(obj1, obj2)
F.add_edge(obj2, obj3)

print(nx.has_path(F, obj1, obj3))
print(nx.has_path(F, obj1, obj4))
