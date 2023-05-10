import random

import itertools as it

from param import MAX_LNS_NEIGHBORS
from plan import Plan


def rand(plan, num=1):
    def shuffle_tasks():
        perm = plan.perm[:]
        random.shuffle(perm)
        return perm

    return [shuffle_tasks() for _ in range(num)]


def swap(plan):
    """
    1. combination index from perm indexes
    2. swap_perm(i, j)
    """

    def swap_perm(i, j):
        perm = plan.perm[:]
        perm[i], perm[j] = perm[j], perm[i]
        return perm

    indexes = range(len(plan.perm))
    return [swap_perm(*swap_indexes) for swap_indexes in it.combinations(indexes, 2)]


def lns(plan, size=3):
    """ """
    candidates = []
    indexes = range(len(plan.perm))
    neighbors = list(it.combinations(indexes, size))

    random.shuffle(neighbors)

    best_plan = plan

    for subset in neighbors[:MAX_LNS_NEIGHBORS]:
        for ordering in it.permutations(subset):
            if ordering == subset:
                continue
            perm = plan.perm[:]
            for i in range(len(ordering)):
                perm[subset[i]] = plan.perm[ordering[i]]

            curr_plan = Plan(plan.batch, perm)
            if curr_plan.makespan() < best_plan.makespan():
                best_plan = curr_plan
        candidates.append(best_plan.perm)
    return candidates


def idle(plan, size=2):
    candidates = []
    stats = list(plan.job_stats())

    stats.sort(key=lambda x: x[3], reverse=True)

    subset = [s[0] for s in stats[:size]]

    for ordering in it.permutations(subset):
        if ordering == subset:
            continue
        perm = plan.perm[:]
        for i in range(len(ordering)):
            perm[subset[i]] = plan.perm[ordering[i]]
            candidates.append(perm)
    return candidates
