import numpy as np

def read_input():
    with open("input.txt", "r") as file:
        return file.read().splitlines()

def find_neighbors(arr, y, x):
    neighbors = []
    if y != 0:
        neighbors += [(y-1,x)]
    if y != len(arr)-1:
        neighbors += [(y+1,x)]
    if x != 0:
        neighbors += [(y,x-1)]
    if x != len(arr[y])-1:
        neighbors += [(y,x+1)]
    neighbors = [n for n in neighbors if arr[n] != 9]
    return neighbors

def search(arr, new, searched):
    for n in new:
        searched += [n]
        neighbors = find_neighbors(arr, n[0], n[1])
        neighbors = [i for i in neighbors if i not in searched]

        if neighbors:
            search(arr, neighbors, searched)
        
    return searched

def main():
    arr = np.array([[int(m) for m in n] for n in read_input()])

    basins = []
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            neighbors = find_neighbors(arr, y, x)
            if all(arr[i,j] > arr[y,x] for i,j in neighbors):
                neighbors = list(set(search(arr, neighbors, [(y,x)])))
                basins+=[len(neighbors)]

    basin = 1
    for b in sorted(basins)[::-1][:3]:
        basin*=b
    print(basin)

if __name__ == "__main__":
    main()