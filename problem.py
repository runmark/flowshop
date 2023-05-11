import random
import time

from plan import Plan, PlanCache
from strategies import StrategyList
from utils import shape
import param


class Problem:
    def __init__(self, batch, time_limit=100):
        self.batch = batch
        self.time_limit = time_limit
        self.strategies = StrategyList()
        self.iteration = 0
        self.cache = PlanCache(self.batch)

    def solve(self):
        num_machines, num_jobs = shape(self.batch)
        init_perm = list(range(num_jobs))
        random.shuffle(init_perm)
        best_plan = Plan(self.batch, init_perm)
        start_time = time.time()

        while time.time() - start_time < self.time_limit:
            iteration_start_time = time.time()

            strategy = self.strategies.pick()

            candidates = strategy.finder(self, best_plan)
            perm = strategy.chooser(self, best_plan, candidates)

            curr_plan = self.cache[perm]

            self.iteration += 1

            time_spent = time.time() - iteration_start_time
            improvements = best_plan.makespan() - curr_plan.makespan()
            strategy.update_usage(time_spent, improvements)

            if curr_plan.makespan < best_plan.makespan():
                best_plan = curr_plan

            if (self.iteration % param.STEP_ITERATION) == 0:
                percent = (time.time - start_time) / self.time_limit
                print(
                    f"Iteration {self.iteration}, progress {percent *100:.1f}%, strategy: {strategy.name}"
                )

        return best_plan

    def dump(self, result_plan):
        print(f"Went through {self.iteration}")
        print()
        result_plan.dump()
