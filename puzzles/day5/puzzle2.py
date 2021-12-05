import numpy as np

def read_input():
    with open("input.txt", "r") as file:
        return [[[int(val) for val in coords.split(",")] for coords in line.split(" -> ")] for line in file]

def main():
    data = read_input()
    diagram = np.zeros((1000, 1000))
    for l in data:
        if l[0][0] != l[1][0]:
            m = (l[0][1] - l[1][1]) / (l[0][0] - l[1][0])
            c = l[0][1] - l[0][0] * m

            step = 1 if l[0][0] < l[1][0] else -1
            for x in range(l[0][0], l[1][0] + step, step):
                y = int(m * (l[0][0] + x - l[0][0]) + c)
                diagram[x, y] += 1
        else:
            step = 1 if l[0][1] < l[1][1] else -1
            for y in range(l[0][1], l[1][1] + step, step):
                diagram[l[0][0], y] += 1

    print(np.count_nonzero(diagram > 1))
        
if __name__ == "__main__":
    main()