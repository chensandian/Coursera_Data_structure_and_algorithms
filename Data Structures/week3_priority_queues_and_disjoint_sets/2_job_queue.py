# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def build_heap(workers):
    start = (n_workers - 2) // 2
    for index in range(start, -1, -1):
        sift_down(index)


def compare_workers(worker1, worker2):
    if worker1[1] != worker2[1]:
        return worker1[1] < worker2[1]
        # the one that will finish work earlier
    else:
        return worker1[0] < worker2[0]
        # the one with a smaller thread num will take work earlier


def sift_down(i):
    min_index = i
    while i < n_workers:
        left = left_child(i)
        if left < n_workers and compare_workers(workers[left], workers[min_index]):
            min_index = left
        right = right_child(i)
        if right < n_workers and compare_workers(workers[right], workers[min_index]):
            min_index = right
        if i != min_index:
            workers[i], workers[min_index] = workers[min_index], workers[i]
            i = min_index
        else:
            break


def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


def change_priority(i, p):
    old_p = workers[i][1]
    workers[i][1] = p
    if p > old_p:
        sift_down(i)
    elif p < old_p:
        # not intended to handle this case
        return -1


if __name__ == "__main__":
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    workers = []
    for i in range(n_workers):
        workers.append([i, jobs[i]])
        print(i, 0)

    build_heap(workers)

    for i in range(n_workers, n_jobs):
        index = workers[0][0]
        started_at = workers[0][1]
        print(index, started_at)
        change_priority(0, started_at + jobs[i])