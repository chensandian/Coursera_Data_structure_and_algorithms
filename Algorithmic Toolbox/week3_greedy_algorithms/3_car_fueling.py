# python3
import sys
def compute_min_refills(distance, mile_can_travel, stops):
    i = 0
    all_stops = [0] + stops + [distance]
    num_refill = 0
    while i <= len(stops):
        last = i
        if all_stops[i + 1] - all_stops[i] > mile_can_travel:
            return -1
        while i <= len(stops) and all_stops[i + 1] - all_stops[last] <= mile_can_travel:
                i += 1
        num_refill += 1

    return num_refill - 1

if __name__ == '__main__':
    distance, tank, num_stop, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(distance, tank, stops))
