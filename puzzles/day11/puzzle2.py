import numpy as np

def read_input():
    with open("input.txt", "r") as file:
        return [[int(j) for j in i] for i in file.read().splitlines()]

def main():
    data = np.array(read_input())

    start = time.time()
    flashes = 0
    steps = 0
    while flashes != 100:
        flashes = 0
        data=np.add(data, 1)

        while (data > 9).sum() > 0:
            for y in range(len(data)):
                for x in range(len(data[y])):
                    if data[y,x] < 10: continue
                    data[max(0,y-1):y+2, max(0,x-1):x+2] += 1
                    data[y,x] = -10

        flashes = (data < 0).sum()
        data[data < 0] = 0
        steps += 1
    print(steps)

if __name__ == "__main__":
    main()