def read_input():
    with open("input.txt") as file:
        return [[s.split(" ") for s in l.split(" | ")] for l in file.read().splitlines()]

def get_ttbl(l):
    l = ["".join(sorted(s)) for s in l]
    l.sort(key=len)

    # Translate table
    ttbl = {l[0]: 1, l[2]: 4, l[1]: 7, l[9]: 8}

    # list of all unknowns and order they are found in
    orders = [[2, 3, 5], [9, 0, 6]]
    all_unknowns = [l[i] for i in range(3, 9)]
    all_unknowns = [all_unknowns[:3], all_unknowns[3:]]
    
    for unknowns, order in zip(all_unknowns, orders):
        # Find number that shares more or less than three letters with 4
        for unknown in unknowns:
            if len(set(unknown) & set(l[2])) != 3:
                ttbl[unknown] = order[0]
            elif len(set(unknown) & set(l[0])) == 2:
                ttbl[unknown] = order[1]
            else:
                ttbl[unknown] = order[2]
        
    return ttbl

def main():
    data = read_input()

    tot = 0
    for l in data:
        ttbl = get_ttbl(l[0])

        nr = ""
        for o in l[1]:
            os = "".join(sorted(o))
            nr += str(ttbl[os])
        tot += int(nr)

    print(tot)

if __name__ == "__main__":
    main()