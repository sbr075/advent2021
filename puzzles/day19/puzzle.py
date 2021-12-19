import numpy as np

class Matrix():
    def rotate_x(self):
        rot_mat = np.array([[1,0,0],[0,0,-1],[0,1,0]])
        for i in range(len(self.beacons)):
            self.beacons[i] = rot_mat.dot(self.beacons[i])

    def rotate_y(self):
        rot_mat = np.array([[0,0,1],[0,1,0],[-1,0,0]])
        for i in range(len(self.beacons)):
            self.beacons[i] = rot_mat.dot(self.beacons[i])

    def rotate_z(self):
        rot_mat = np.array([[0,-1,0],[1,0,0],[0,0,1]])
        for i in range(len(self.beacons)):
            self.beacons[i] = rot_mat.dot(self.beacons[i])
    
    def calc_dists(self):
        dists = {}
        for i in range(len(self.beacons)):
            for j in range(i+1, len(self.beacons)):
                d = np.linalg.norm(self.beacons[i]-self.beacons[j])
                dists[d] = [self.beacons[i], self.beacons[j]]
        return dists

class Scanner(Matrix):
    def __init__(self, id):
        self.id = id
        self.pos = (0,0,0)
        self.rotation = 0
        self.data = {}
        self.dists = None
        self.beacons = []

    def update_data(self):
        for i in range(64):
            if i != 0:
                self.rotate_z()
                if i % 4 == 0: self.rotate_y()
                if i % 16 == 0: self.rotate_x()

            self.data[i] = [self.calc_dists(), self.beacons.copy()]

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

def main():
    scanners = read_input()
    for s in scanners:
        s.update_data()

    found = [scanners[0]]
    queue = [scanners[0]]
    while queue:
        s1 = queue.pop()
        s1.dists = s1.data[s1.rotation][0]

        for s2 in scanners:
            if s1 == s2 or s2 in found:
                continue
            
            for _ in range(64):
                s2.dists = s2.data[s2.rotation][0]
                pairs = find_pairs(s1, s2)
                if not pairs:
                    continue
                
                k = [tuple(np.subtract(p[0], p[1])) for p in pairs]
                if len(set(k)) == 1:
                    s2.pos = tuple(np.add(k[0], s1.pos))
                    queue.append(s2)
                    found.append(s2)
                    break
                
                s2.rotation += 1
                s2.rotation %= 64
           
    beacons = []
    for s in scanners:
        s.beacons = s.data[s.rotation][1]
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