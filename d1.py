with open("d1_data") as f:
    data = f.readlines()


def p1():
    total = sum(int(x) for x in data)
    print(total)


def generated_frequencies():
    total = 0
    while True:
        for row in data:
            total += int(row)
            yield total


def p2():
    already_seen = set()
    for freq in generated_frequencies():
        if freq in already_seen:
            break
        already_seen.add(freq)

    # print("the result is", freq)


def p22():
    d = {}
    for value in generated_frequencies():
        try:
            d[value]
        except KeyError:
            d[value] = 1
        else:
            # print(value)
            break


if __name__ == "__main__":
    from timeit import timeit

    count = 100
    print("j", timeit("import d1; d1.p2()", number=count))
    print("r", timeit("import d1; d1.p22()", number=count))
