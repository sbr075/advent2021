import numpy as np

class Scanner():
    def __init__(self, id):
        self.id = id
        self.pos = (0,0,0)
        self.beacons = []
        self.dists = {}

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
    s.dists = {}
    for i in range(len(s.beacons)):
        for j in range(i+1, len(s.beacons)):
            d = np.linalg.norm(s.beacons[i]-s.beacons[j])
            updt(s.dists, d, [s.beacons[i], s.beacons[j]])

def in_list(l, v):
    for i in l:
        if np.array_equal(i, v):
            return True
    return False

def find_pairs(s1, s2):
    pos = {}
    for d in s1.dists:
        if d in s2.dists:
            p1 = tuple(s1.dists[d][0])
            p2 = tuple(s1.dists[d][1])
            updt(pos, p1, s2.dists[d])
            updt(pos, p2, s2.dists[d])
    
    if len(pos) < 12:
        return None

    pairs = []
    for k,v in pos.items():
        seen = []
        for p in v:
            if in_list(seen, p):
                break
            seen.append(p)
        pairs.append([k,p])
    return pairs

def shift_coords(s):
    for i in range(len(s.beacons)):
        s.beacons[i] = np.add(s.beacons[i], s.pos)

def rotate_x(s):
    rot_mat = np.array([[1,0,0],[0,0,-1],[0,1,0]])
    for i in range(len(s.beacons)):
        s.beacons[i] = rot_mat.dot(s.beacons[i])

def rotate_y(s):
    rot_mat = np.array([[0,0,1],[0,1,0],[-1,0,0]])
    for i in range(len(s.beacons)):
        s.beacons[i] = rot_mat.dot(s.beacons[i])

def rotate_z(s):
    rot_mat = np.array([[0,-1,0],[1,0,0],[0,0,1]])
    for i in range(len(s.beacons)):
        s.beacons[i] = rot_mat.dot(s.beacons[i])

def main():
    scanners = read_input()

    found = [scanners[0]]
    queue = [scanners[0]]
    while queue:
        s1 = queue.pop()
        calc_dists(s1)

        for s2 in scanners:
            if s1 == s2 or s2 in found:
                continue

            is_found = False
            for _ in range(4):
                for _ in range(4):
                    for _ in range(4):
                        calc_dists(s2)
                        pairs = find_pairs(s1, s2)
                        if not pairs:
                            continue

                        k = [tuple(np.subtract(p[0], p[1])) for p in pairs]
                        if len(set(k)) == 1:
                            s2.pos = tuple(np.add(k[0], s1.pos))
                            queue.append(s2)
                            found.append(s2)
                            is_found = True
                    
                        if is_found: break
                        rotate_z(s2)
                    if is_found: break
                    rotate_y(s2)
                if is_found: break
                rotate_x(s2)
    
    beacons = []
    for s in scanners:
        shift_coords(s)
        beacons += [tuple(b) for b in s.beacons]
    print(f"Part 1 {len(set(beacons))}")

    l = 0
    for s1 in scanners:
        for s2 in scanners:
            if s1 == s2: continue
            s = sum(abs(np.subtract(s1.pos,s2.pos)))
            if s > l:
                l = s
    print(f"Part 2 {l}")

if __name__ == "__main__":
    main()