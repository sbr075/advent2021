import numpy as np

def read_input():
    with open("input.txt", "r") as file:
        return file.read().splitlines()

def main():
    arr = np.array([[int(m) for m in n] for n in read_input()])

    risks = []
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            neighbors = []
            if y != 0:
                neighbors += [arr[y-1,x]]
            if y != len(arr)-1:
                neighbors += [arr[y+1,x]]
            if x != 0:
                neighbors += [arr[y,x-1]]
            if x != len(arr[y])-1:
                neighbors += [arr[y,x+1]]
            if all(n > arr[y,x] for n in neighbors):
                risks += [arr[y,x]+1]
    print(sum(risks))

if __name__ == "__main__":
    main()