def read_input():
    with open("input.txt") as file:
        return [[s.split(" ") for s in l.split(" | ")] for l in file.read().splitlines()]

def get_ttbl(l):
    """
    1, 4, 7 and 8 have unique lengths
    1 = 2 (0)
    4 = 4 (2)
    7 = 3 (1)
    8 = 7 (8)
    Therefor we immediatly known what numbers they belong to

    By using the number 8 we can find all numbers
    First we find the difference between 8 and the unknowns

    We can find 3 by:
    2 and 5 share no letters
    3 share 1 letter with both 2 and 5
    
    We can find 2 and 5 by;
    4 shares 1 letter with 5
    4 shares 2 letters with 2

    We can find 9 by:
    0 and 6 share 1 letter with 4
    9 shares no letters with 4

    We can find 0 and 6 by:
    1 shares 1 letter with 6
    1 shares no letters wih 0
    """
    l = ["".join(sorted(s)) for s in l]
    l.sort(key=len)

    # Translate table
    ttbl = {
        l[0]: 1,
        l[2]: 4,
        l[1]: 7,
        l[9]: 8
    }

    all_unknowns = []
    for i in [3, 4, 5, 6, 7, 8]:
        all_unknowns.append(l[i])
    
    # Finding first number
    unknowns = []
    for j in all_unknowns[:3]:
        unknowns.append([n for n in l[9] if n not in j])

    idx = [3,4,5]
    nrs = [3,5,2]
    # Find the one who shares one letter with both
    for j in range(len(unknowns)):
        if (set(unknowns[j]) & set(unknowns[(j+1)%3])) and (set(unknowns[j]) & set(unknowns[(j+2)%3])):
            break

    ttbl[l[idx[j]]] = nrs[0]
    del unknowns[j]
    del idx[j]

    # Finding second and third, nrs 2 and 3
    for j in range(len(unknowns)):
        if len(set(unknowns[j]) & set(l[2])) == 1:
            ttbl[l[idx[j]]] = nrs[1]
        else:
            ttbl[l[idx[j]]] = nrs[2]
    
    # Finding first number
    unknowns = []
    for j in all_unknowns[3:]:
        unknowns.append([n for n in l[9] if n not in j])

    idx = [6,7,8]
    nrs = [9,0,6]
    # Find index that shares no letter with 4
    for j in range(len(unknowns)):
        if len(set(unknowns[j]) & set(l[2])) == 0:
            break

    ttbl[l[idx[j]]] = nrs[0]
    del unknowns[j]
    del idx[j]

    # Finding second and third, nrs 2 and 3
    for j in range(len(unknowns)):
        if len(set(unknowns[j]) & set(l[0])) == 0:
            ttbl[l[idx[j]]] = nrs[1]
        else:
            ttbl[l[idx[j]]] = nrs[2]
    
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