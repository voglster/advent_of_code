def read_file():
    with open("d1_data") as f:
        while True:
            data = f.readline()
            if not data:
                break
            yield data


def p1():
    total = sum(int(x) for x in data)
    print(total)


sum()
