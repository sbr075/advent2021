def read_input():
    with open("input.txt", "r") as file:
        return [[s.split(" ") for s in l.split(" | ")] for l in file.read().splitlines()]

digits = {
    0: [5, ["a", "b", "c", "e", "f", "g"]],
    1: [2, ["c, f"]],
    2: [5, ["a", "c", "d", "e", "g"]],
    3: [5, ["a", "c", "d", "f", "g"]],
    4: [4, ["b", "c", "d", "f"]],
    5: [5, ["a", "b", "d", "f", "g"]],
    6: [6, ["a", "b", "d", "e", "f", "g"]],
    7: [3, ["a", "c", "f"]],
    8: [7, ["a", "b", "c", "d", "e", "f", "g"]],
    9: [6, ["a", "b", "c", "d", "f", "g"]]
}

def main():
    data = read_input()

    occs = [0]*10
    for l in data:
        for output in l[1]:
            occs[len(output)] += 1

    occ = 0
    numbers = [1, 4, 7, 8]
    for n in numbers:
        occ += occs[digits[n][0]]
    print(occ)

if __name__ == "__main__":
    main()