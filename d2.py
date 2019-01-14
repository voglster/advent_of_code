from itertools import combinations

with open("d2_data") as f:
    data = f.readlines()


def part1():
    from collections import Counter

    def has_count(box, count):
        return any((x == count for x in Counter(box).values()))

    two_count = sum(1 if has_count(d, 2) else 0 for d in data)
    three_count = sum(1 if has_count(d, 3) else 0 for d in data)

    val = two_count * three_count
    print(val)

    assert has_count("babaqc", 2), "it didnt find a double"
    assert has_count("babaqac", 3), "it didnt find a triple"
    assert not has_count("bawaqac", 2), "found a double when it shouldnt"
    assert not has_count("bawaqc", 3), "found a triple when it shouldnt"


def different_letters(a, b):
    for b1_letter, b2_letter in zip(a, b):
        if b1_letter != b2_letter:
            yield b1_letter


def common_letters(a, b):
    for b1_letter, b2_letter in zip(a, b):
        if b1_letter == b2_letter:
            yield b1_letter


def has_1_character_different(box1, box2):
    different_letter_count = sum(1 for _ in different_letters(box1, box2))
    return different_letter_count == 1


for box1_code, box2_code in combinations(data, 2):
    if has_1_character_different(box1_code, box2_code):
        print("".join(common_letters(box1_code, box2_code)))
        break

if __name__ == "__main__":
    # assert not compare("aa", "aa"), "same should be false"
    # assert compare("ab", "aa"), "same should be true"
    # assert not compare("bb", "aa"), "same should be false"

    pass
    # print(get_remaining_letters("abc", "aqc"))
