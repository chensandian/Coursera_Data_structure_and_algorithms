# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    ''' mark all the starting points, ending points and points on a line,
        sort them in non-descending order. O(n*logn)
        iterate through the list, count the number of starting points, ending points. just O(n)
        if we find a point, then num_covered_range = num_starting - num_ending.
        we don't care which starting points pair with which ending point.
        if point land on starting or ending point, we should also count this segment
        so when we sort the list, starting < point < ending if they have some value
    '''
    cnt = [0] * len(points)

    starting, point, ending = -1, 0, 1
    marks = []
    point_index = {}
    for s in starts:
        marks.append((s, starting))
    for e in ends:
        marks.append((e, ending))
    for index, p in enumerate(points):
        marks.append((p, point))
        if p not in point_index:
            point_index[p] = [index]
        else:
            point_index[p].append(index)

    marks.sort()

    starting_count = 0
    ending_count = 0
    for mark in marks:
        if mark[1] == starting:
            starting_count += 1
        elif mark[1] == ending:
            ending_count += 1
        elif mark[1] == point:
            for index in point_index[mark[0]]:
                cnt[index] = starting_count - ending_count

    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    #input = input()
    data = list(map(int, input.split()))
    num_segments = data[0]
    num_points = data[1]
    starts = data[2:2 * num_segments + 2:2]
    ends = data[3:2 * num_segments + 2:2]
    points = data[2 * num_segments + 2:]
    #use fast_count_segments
    #cnt = naive_count_segments(starts, ends, points)
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
