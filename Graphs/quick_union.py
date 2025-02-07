from abc import ABC, abstractmethod
import uf

class QuickUnion(uf.UF):
    def __init__(self, number_of_elements):
        self._elemets = [i for i in range(number_of_elements)]
        self._count = number_of_elements

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        self._elemets[p_root] = q_root
        self._count = self._count-1

    def find(self, p):
        while p!=self._elemets[p]:
            p = self._elemets[p]
        return p

    def count(self):
        return self._count

    def print(self):
        print(",".join([str(el) for el in self._elemets]))




