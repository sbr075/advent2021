def read_input():
    with open("input.txt", "r") as file:
        data = [line.split(" -> ") for line in file.read().splitlines()]
        data = [[coords.split(",") for coords in line] for line in data]

    return data

def main():
    data = read_input()

    coords = {}
    for l in data:
        c1 = [int(val) for val in l[0]]
        c2 = [int(val) for val in l[1]]
        d = [abs(v1 - v2) for v1, v2 in zip(c1, c2)]

        # Horizontal lines
        if d[0] > 0 and d[1] == 0:
            start = c1[0] if c1[0] < c2[0] else c2[0]
            for i in range(start, start + d[0] + 1):
                if i in coords:
                    coords[i].append(c1[1])
                else:
                    coords[i] = [c1[1]]

        # Vertical lines
        if d[1] > 0 and d[0] == 0:
            start = c1[1] if c1[1] < c2[1] else c2[1]
            for j in range(start, start + d[1] + 1):
                if c1[0] in coords:
                    coords[c1[0]].append(j)
                else:
                    coords[c1[0]] = [j]
        
        # Diagonal lines
        if d[0] > 0 and d[1] > 0:
            step_x = 1 if c1[0] < c2[0] else -1
            step_y = 1 if c1[1] < c2[1] else -1
            c2[0] += -1 if c2[0] < c1[0] else 1
            while (c1[0] != c2[0]):
                if c1[0] in coords:
                    coords[c1[0]].append(c1[1])
                else:
                    coords[c1[0]] = [c1[1]]

                c1[0] += step_x
                c1[1] += step_y

    # Find dupes
    num_duplicates = 0
    for _, coords in coords.items():
        duplicates = []
        [duplicates.append(val) for val in coords if coords.count(val) > 1 and val not in duplicates]
        num_duplicates += len(duplicates)

    print(num_duplicates)
        
if __name__ == "__main__":
    main()