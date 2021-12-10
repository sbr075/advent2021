import numpy as np

def read_input():
    with open("input.txt", "r") as file:
        return file.read().splitlines()

def find_neighbors(arr, y, x):
    neighbors = [p for p in [(y-1,x),(y+1,x),(y,x-1),(y,x+1)] \
        if 0 <= p[0] < arr.shape[0] and 0 <= p[1] < arr.shape[1] and arr[p]!=9]
    return neighbors

def search(arr, new, searched):
    searched += new
    for n in new:
        neighbors = [i for i in find_neighbors(arr, n[0], n[1]) if i not in searched]
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
                basins+=[len(search(arr, neighbors, [(y,x)]))]

    basin = 1
    for b in sorted(basins)[-3:]:
        basin*=b
    print(basin)

if __name__ == "__main__":
    main()