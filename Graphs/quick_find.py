from abc import ABC, abstractmethod
import uf

class QuickFind(uf.UF):
    def __init__(self, number_of_elements):
        self._elemets = [i for i in range(number_of_elements)]
        self._count = number_of_elements

    def union(self, p, q):
        pid = self.find(p)
        qid = self.find(q)
        if pid == qid:
            return
        for i in range(len(self._elemets)):
            if self._elemets[i] == pid:
                self._elemets[i] = qid
        self._count = self._count-1

    def find(self, p):
        return self._elemets[p]

    def count(self):
        return self._count

    def print(self):
        print(",".join([str(el) for el in self._elemets]))


