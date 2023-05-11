import random

from plan import Plan


def rand(ctx, plan, candidates):
    return random.choice(candidates)


def hillclimbing(ctx, plan, candidates):
    """
    choose best from candidates
    """
    plans = [ctx.cache[c] for c in candidates]
    plans.sort(key=lambda x: x.makespan())

    return plans[0].perm


def random_hillclimbing(ctx, plan, candidates):
    plans = [ctx.cache[c] for c in candidates]
    plans.sort(key=lambda x: x.makespan())

    subset_size = int(len(plans) / 2)
    subset = plans[:subset_size]

    return random.choice(subset).perm
