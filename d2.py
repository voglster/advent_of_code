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


def compare(box1, box2):
    if box1 == box2:
        return False

    count_miss = 0
    for c1, c2 in zip(box1, box2):
        if c1 != c2:
            count_miss += 1
        if count_miss > 1:
            return False
    else:
        return True


def get_remaining_letters(box1_code, box2_code):
    saved_letters = []
    for b1_letter, b2_letter in zip(box1_code, box2_code):
        if b1_letter == b2_letter:
            saved_letters.append(b1_letter)
    final = "".join(saved_letters)
    return final


from itertools import combinations

for box1_code, box2_code in combinations(data, 2):
    if compare(box1_code, box2_code):
        print(get_remaining_letters(box1_code, box2_code))
        break

        # print("".join(q for q, r in zip(a, b) if q == r))
        # break


if __name__ == "__main__":
    # assert not compare("aa", "aa"), "same should be false"
    # assert compare("ab", "aa"), "same should be true"
    # assert not compare("bb", "aa"), "same should be false"

    print(get_remaining_letters("abc", "aqc"))
