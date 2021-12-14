import numpy as np

def read_input():
    points = []
    folds  = []
    with open("input.txt", "r") as file:
        for l in file.read().splitlines():
            if "fold" in l:
                folds.append([l[11:12], int(l[13:])])
            elif "," in l:
                points.append(tuple([int(p) for p in l.split(",")])[::-1]) # reversed because numpy
    return points, folds

def main():
    points, folds = read_input()

    w = max([p[1] for p in points])+1
    h = max([p[0] for p in points])+1
    m = np.zeros((h,w))
    for p in points:
        m[p] = 1

    for i in range(len(folds)):
        axis = 0 if folds[i][0] == "y" else 1
        line = folds[i][1]

        if axis: # x
            n = np.flip(m[:,line+1:], axis=axis)
            m = m[:,:line]
        else:    # y
            n = np.flip(m[line+1:,:], axis=axis)
            m = m[:line,:]
        dy,dx = np.subtract(m.shape, n.shape)

        for y in range(n.shape[0]):
            for x in range(n.shape[1]):
                m[y+dy,x+dx] += n[y,x]
        
        if i == 0:
            print(f"Part 1: {np.count_nonzero(m)}")
    
    print("\nPart 2:")
    for r in m:
        for c in r:
            print("#" if c else " ", end=" ")
        print()
    
    
if __name__ == "__main__":
    main()