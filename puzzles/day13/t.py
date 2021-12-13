import numpy as np 

input = []
folds = []
with open('input.txt') as f:
    for line in f.readlines():
        if line[:-1].split(' ')[0] == 'fold':
            folds.append(line[:-1].split(' ')[-1].split("="))
        else:
            input.append(line[:-1])
input = [(int(i.split(',')[-1]), int(i.split(',')[0])) for i in input if i != '']  # flip x and y 

arr = np.zeros((max([i[0] for i in input])+1 , max([i[-1] for i in input])+1))
for coord in input:
    arr[coord] = -1

def update_array(arr, diff):
    zeros = np.zeros((diff, arr.shape[-1]))
    return np.concatenate([arr, zeros])

def fold(arr, f):
    print(f[-1])
    if f[0] == 'y':
        h1 = arr[: int(f[-1])]
        h2 = arr[ int(f[-1]) + 1 :]
        # handle uneven folds by resizing arrays using 0s
        if h1.shape[0] != h2.shape[0]:
            if h2.shape[0] < h1.shape[0]:
                h2 = update_array(h2, diff=h1.shape[0]-h2.shape[0])
            else:
                h1 = update_array(h1, diff=h2.shape[0]-h1.shape[0])
        return h1 + h2[::-1]
    if f[0] == "x":
        arr = arr.T
        h1 = arr[: int(f[-1])]
        h2 = arr[int(f[-1])+1:]
        # handle uneven folds by resizing arrays using 0s
        if h1.shape[0] != h2.shape[0]:
            if h2.shape[0] < h1.shape[0]:
                h2 = update_array(h2, diff=h1.shape[0]-h2.shape[0])
            else:
                h1 = update_array(h1, diff=h2.shape[0]-h1.shape[0])
        return (h1 + h2[::-1]).T


# part 1 + 2
for idx, f in enumerate(folds):
    arr = fold(arr, f)
    if idx == 0:
        print(f'part1: {len(arr[arr < 0])}')

print(f'part2: {len(arr[arr < 0])}')

print(arr)


"""
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
    
    for i in ins:
        i=i[0]
        l = int("".join(filter(str.isdigit, i)))
        if "y" in i:
            print(f"Fold around y={l}")
            for j in range(l):
                r = m[m.shape[0]-j-1,:]
                m[j,:] += r
            m = m[:l,:]
        else:
            print(f"Fold around x={l}")
            for j in range(l):
                r = m[:,m.shape[1]-j-1]
                m[:,j] += r
            m = m[:,:l]
    
    print(np.count_nonzero(m))    
    
if __name__ == "__main__":
    main()
"""