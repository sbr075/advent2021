import numpy as np

def read_input():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()
        data = [d.split(",") for d in data]
        points = [p for p in data if len(p) == 2]
        ins = [i for i in data if len(i) == 1 and len(i[0])!=0]
    return points, ins


def main():
    points, ins = read_input()

    w = max([int(p[0]) for p in points])+1
    h = max([int(p[1]) for p in points])+1

    m = np.zeros((h,w))
    for p in points:
        m[int(p[1]),int(p[0])] = 1
    
    for i in range(len(ins)):
        j=ins[i][0]
        l = int("".join(filter(str.isdigit, j)))
        if "x" in j:
            l = (m.shape[1]-1) // 2
            n_m = np.flip(m[:,l+1:], axis=1)
            m = m[:,:l]
        else:
            l = (m.shape[0]-1) // 2
            n_m = np.flip(m[l+2:,:], axis=0)
            m = m[:l,:]
        m = np.add(m, n_m)

        if i == 0:
            print(np.count_nonzero(m))
    
    for r in m:
        for c in r:
            print("#" if c else " ", end=" ")
        print()
    
if __name__ == "__main__":
    main()