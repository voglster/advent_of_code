from itertools import combinations
import re
from common import load_day_data
from parse import parse

data = load_day_data(3)


def parse_input_line(a_single_input_line):
    """#1 @ 493,113: 12x14"""
    plan_number, other = a_single_input_line.split("@")
    plan_number = int(plan_number.strip()[1:])
    start_coord, wh = other.split(":")
    x, y = start_coord.strip().split(",")
    x, y = int(x), int(y)
    w, h = wh.strip().split("x")
    w, h = int(w), int(h)
    return plan_number, x, y, w, h


def parse_input_line2(a_single_input_line):
    """#1 @ 493,113: 12x14"""
    return parse("#{:d} @ {:d},{:d}: {:d}x{:d}", a_single_input_line).fixed


def get_points(x, y, w, h):
    ret = set()
    for mx in range(x, x + w):
        for my in range(y, y + h):
            ret.add((mx, my))
    return ret


class ElfPlan:
    def __init__(self, plan_number, x, y, w, h):
        self.plan_number = plan_number
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.points = get_points(x, y, w, h)

    @classmethod
    def from_line(cls, line):
        return ElfPlan(*parse_input_line2(line))

    def overlapping_points(self, other):
        return self.points & other.points

    def contains(self, point):
        x, y = point
        xin = self.x <= x < (self.x + self.w)
        yin = self.y <= y < (self.y + self.h)
        return xin and yin


def get_plans():
    for line in data:
        yield ElfPlan.from_line(line)


def print_overlaps():
    plans = list(get_plans())
    points = set()
    for a, b in combinations(plans, 2):
        for point in a.overlapping_points(b):
            points.add(point)
    print(len(points))


def print_best_one():
    plans = list(get_plans())
    points = set()
    for a, b in combinations(plans, 2):
        for point in a.overlapping_points(b):
            points.add(point)

    for plan in plans:
        if not any(plan.contains(p) for p in points):
            print(plan.plan_number)
            break


if __name__ == "__main__":
    a = ElfPlan.from_line("#25 @ 0,0: 2x2")
    assert a.contains((0, 0))
    assert a.contains((1, 0))
    assert a.contains((0, 1))
    assert a.contains((1, 1))
    assert not a.contains((-1, 1))
    assert not a.contains((1, 2))

    # b = ElfPlan.from_line("#25 @ 1,1: 2x2")
    # print(a.overlapping_points(b))

    print_best_one()

