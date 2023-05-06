from utils import shape


class Plan:
    def __init__(self, batch, perm):
        self.batch = batch
        self.perm = perm
        # _times store the (i, j)'s best makespan ever
        self._times = None
        self._makespan = None

    def makespan(self):
        self.calc()
        return self._makespan

    def get_task_time(self, i, j):
        return self.batch[i][self.perm[j]]

    def get_end_time(self, i, j):
        return self._times[i][j] + self.get_task_time(i, j)

    def calc(self):
        if self._makespan is not None:
            return

        def get_time(row, col):
            if row < 0 or col < 0:
                return 0
            return self._times[row][col] + self.get_task_time(row, col)

        num_machines, num_tasks = shape(self.batch)
        self._times = [([0] * num_tasks) for _ in range(num_machines)]

        for i in range(num_machines):
            for j in range(num_tasks):
                self._times[i][j] = max(get_time(i - 1, j), get_time(i, j - 1))

        self._makespan = self.get_end_time(num_machines - 1, num_tasks - 1)
