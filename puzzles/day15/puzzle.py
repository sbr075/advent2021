import numpy as np

def read_input():
    with open("input.txt", "r") as file:
        return [[int(c) for c in l] for l in file.read().splitlines()]

def get_neighbors(grid, y, x, v):
    neighbors = [p for p in [(y-1,x),(y+1,x),(y,x-1),(y,x+1)] \
        if 0 <= p[0] < grid.shape[0] and 0 <= p[1] < grid.shape[1] and p not in v]
    return neighbors

def ext_grid(grid):
    for ax in [0,1]:
        tmp = grid.copy()
        for i in range(4):
            tmp += 1
            tmp[tmp > 9] = 1
            grid = np.concatenate((grid, tmp), axis=ax)

    return grid

def dijkstra(grid, ext):
    if ext:
        grid = ext_grid(grid)
    e = tuple(np.subtract(grid.shape, (1,1)))

    stack = [[0, (0,0)]]
    v = set([(0,0)])
    while True:
        c = stack[0][0]
        p = stack[0][1]
        if p == e:
            break

        vs = get_neighbors(grid, p[0], p[1], v)
        v|=set(vs)

        del stack[0]
        stack += [[c+grid[p], p] for p in vs]
        stack = sorted(stack, key=lambda x: x[0])

    print(stack[0][0])

def main():
    grid = np.array(read_input())
    dijkstra(grid, False)
    dijkstra(grid, True)

if __name__ == "__main__":
    main()