from collections import UserList
from functools import partial
import random

from algorithm import find_neighbors as fn
from algorithm import choose_neighbor as cn


class Strategy:
    def __init__(self, name, finder, chooser):
        self.name = name
        self.finder = finder
        self.chooser = chooser


class StrategyList(UserList):
    def __init__(self):
        finders = [("Random Permutation", partial(fn.rand, num=1000))]
        choosers = [("Random Selection", cn.rand)]

        strateties = [
            Strategy("%s / %s" % (fname, cname), f, c)
            for fname, f in finders
            for cname, c in choosers
        ]

        super().__init__(strateties)

    def pick(self):
        return random.choice(self)
