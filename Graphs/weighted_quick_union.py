from abc import ABC, abstractmethod
import uf, os

class WeightedQuickUnion(uf.UF):
    def __init__(self, number_of_elements):
        self._elemets = [i for i in range(number_of_elements)]
        self._size = [1 for i in range(number_of_elements)]
        self._count = number_of_elements

    def union(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot == qRoot:
            return
        if self._size[pRoot]< self._size[qRoot]:
            self._elemets[pRoot] = qRoot
            self._size[qRoot]+=1
        else:
            self._elemets[qRoot] = pRoot
            self._size[pRoot]+=1
        self._count -= 1

    def find(self, p):
        try:
            while p!=self._elemets[p]:
                p = self._elemets[p]
        except:
            print(f"This object does not exist: {p}")
            return
        print(f"Object does exist: {p}")
        return p

    def count(self):
        return self._count

    def print(self):
        print(",".join([str(el) for el in self._elemets]))


obj = WeightedQuickUnion(5)
obj.find(6)
obj.count()
obj.print()
