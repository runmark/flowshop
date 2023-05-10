import random

from plan import Plan


def rand(plan, candidates):
    return random.choice(candidates)


def hillclimbing(plan, candidates):
    """
    choose best from candidates
    """
    plans = [Plan(plan.batch, c) for c in candidates]
    plans.sort(key=lambda x: x.makespan())

    return plans[0].perm


def random_hillclimbing(plan, candidates):
    plans = [Plan(plan.batch, c) for c in candidates]
    plans.sort(key=lambda x: x.makespan())

    subset_size = int(len(plans) / 2)
    subset = plans[:subset_size]

    return random.choice(subset).perm
