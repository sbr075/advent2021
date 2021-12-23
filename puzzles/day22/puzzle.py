class Cube():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def read_input():
    with open("input.txt", "r") as file:
        d=[]
        for l in file.read().splitlines():
            c = []
            l = l.split(" ")
            c.append(1 if l[0] == "on" else 0)
            l = l[1].split(",")
            for p in l:
                c.append([int(i) for i in p[2:].split("..")])
            d.append(c)
        return d

def not_intersecting(c1, c2):
    return not (c2.x[0] <= c1.x[1] and c2.x[1] >= c1.x[0] and \
                c2.y[0] <= c1.y[1] and c2.y[1] >= c1.y[0] and \
                c2.z[0] <= c1.z[1] and c2.z[1] >= c1.z[0])

def slice_cube(c1, c2):
    cubes = []

    # slice right side of c2
    if c1.x[1] < c2.x[1]:
        cubes.append(Cube([c1.x[1]+1, c2.x[1]], c2.y[:], c2.z[:]))
        c2.x[1] = c1.x[1]

    # slice left side of c2 
    if c1.x[0] > c2.x[0]:
        cubes.append(Cube([c2.x[0], c1.x[0]-1], c2.y[:], c2.z[:]))
        c2.x[0] = c1.x[0]
    
    # slice top side of c2
    if c1.y[1] < c2.y[1]:
        cubes.append(Cube(c2.x[:], [c1.y[1]+1, c2.y[1]], c2.z[:]))
        c2.y[1] = c1.y[1]

    # slice bottom side of c2 
    if c1.y[0] > c2.y[0]:
        cubes.append(Cube(c2.x[:], [c2.y[0], c1.y[0]-1], c2.z[:]))
        c2.y[0] = c1.y[0]
    
    # slice front side of c2
    if c1.z[1] < c2.z[1]:
        cubes.append(Cube(c2.x[:], c2.y[:], [c1.z[1]+1, c2.z[1]]))
        c2.z[1] = c1.z[1]

    # slice back side of c2 
    if c1.z[0] > c2.z[0]:
        cubes.append(Cube(c2.x[:], c2.y[:], [c2.z[0], c1.z[0]-1]))
    
    return cubes

def oob(c):
    for p in [c.x, c.y, c.z]:
        if any(v < -50 for v in p) or any(v > 50 for v in p): return True

def main(part1=False):
    data = read_input()

    cubes = []
    for d in data:
        c1 = Cube(d[1], d[2], d[3])
        new_cubes = []
        for c2 in cubes:
            if part1 and oob(c2): continue
            if not_intersecting(c1, c2):
                new_cubes += [c2]
            else:
                new_cubes += slice_cube(c1, c2)
        
        if d[0]:
            new_cubes.append(c1)

        cubes = new_cubes
    
    area = 0
    for cube in cubes:
        x_len = cube.x[1] - cube.x[0] + 1
        y_len = cube.y[1] - cube.y[0] + 1
        z_len = cube.z[1] - cube.z[0] + 1
        area += (x_len * y_len * z_len)
    
    return area

if __name__ == "__main__":
    print(f"Part 1: {main(True)}")
    print(f"Part 2: {main()}")