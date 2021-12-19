from os import pardir
import numpy as np
from numpy.lib.index_tricks import fill_diagonal

rotations = [
    # Facing x-axis
    np.array([(1,0,0), (0,0,-1), (0,1,0)]),

    # Facing y-axis
    np.array([(0,0,1), (0,1,0), (-1,0,0)]),

    # Facing z-axis
    np.array([(0,-1,0), (1,0,0), (0,0,1)])
]

class Scanner():
    def __init__(self, id):
        self.id = id
        self.pos = (0,0,0)
        self.beacons = []
        self.dists = {}

    def set_pos(self, pos):
        self.pos = pos

def read_input():
    with open("input.txt", "r") as file:
        p = file.read().splitlines()
        s=[]
        for l in p:
            if "scanner" in l:
                t = Scanner(len(s))
                s.append(t)
            elif len(l):
                t.beacons.append(np.array([int(i) for i in l.split(",")]))
        return s

def updt(d, k, v):
    d[k] = v if k not in d else d[k] + v

def calc_dists(s):
    for p1 in s.beacons:
        for p2 in s.beacons:
            if (p1==p2).all():
                continue
            
            d = np.linalg.norm(p1-p2)
            updt(s.dists, d, [[p1,p2]])

def find_pairs(s1, s2):
    p = {}
    for d in s1.dists:
        if d in s2.dists:
            p1 = tuple(s1.dists[d][0][0])
            p2 = tuple(s1.dists[d][0][1])
            updt(p, p1, s2.dists[d])
            updt(p, p2, s2.dists[d])
    
    pairs = []
    for k,v in p.items():
        c = set([tuple(l) for l in v[0]])
        for cs in v[1:]:
            c &= set([tuple(l) for l in cs])
        pairs.append([k, c.pop()])


    return pairs

def main():
    scanners = read_input()
    
    for s in scanners:
        calc_dists(s)
    
    u = {}
    for i in range(len(scanners)):
        s1 = scanners[i]
        print(f"Scanner {s1.id}")
        for j in range(i+1, len(scanners)):
            s2 = scanners[j]
            
            pairs = find_pairs(s1, s2)
            print(f"->\tScanner {s2.id} {len(pairs)}")
            if len(pairs) != 12:
                continue

            for p in pairs:
                updt(u, p[0], p[1])
                updt(u, p[1], p[0])
            continue
            
            # brute force s2 directions
            dirs = [(1,1,1),(-1,1,1),(1,-1,1),(1,1,-1),(-1,-1,1),(1,-1,-1),(-1,1,-1),(-1,-1,-1)]
            for dir in dirs:
                r = []
                for p in pairs:
                    d = abs(np.subtract(p[0], p[1]*dir))
                    r.append(tuple(d*np.multiply(dir, -1)))
                
                if len(set(r)) == 1:
                    s1.pos = r[0]
                    break
        print()

    for k in u:
        print(k)
    print(len(u))

if __name__ == "__main__":
    main()