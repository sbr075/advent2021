import copy

ltn = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

ntl = {
    2: "A",
    4: "B",
    6: "C",
    8: "D"
}

nrg = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000
}

room_len = 4

def read_input():
    with open("input.txt", "r") as file:
        rooms = {}
        for l in file.read().splitlines():
            if "." in l:
                spots = [None for _ in range(l.count("."))]
            for i,c in enumerate(l):
                if c.isalpha():
                    rooms[i-1] = [c] if i-1 not in rooms else rooms[i-1] + [c]

        return rooms, spots

def status(rooms, spots, cost):
    print(f"cost {cost}")
    for s in spots:
        print("_ " if not s else f"{s} ", end="")
    print()

    for i in range(room_len):
        for s in range(len(spots)):
            if s in [2, 4, 6, 8]:
                try:
                    print(f"{rooms[s][i]} ", end="")
                except:
                    print("  ", end="")
            else:
                print("  ", end="")
        print()

def room_complete(nr, room):
    if len(room) < room_len: return False
    for l in room:
        if ltn[l] != nr:
            return False
    return True

def all_complete(rooms):
    for nr,room in rooms.items():
        if not room_complete(nr, room):
            return False

    return True

def room_available(rooms, l):
    room_nr = ltn[l]
    room = rooms[room_nr]
    if not room: return True
    for l in room:
        if ltn[l] != room_nr:
            return False
    return True

def path_clear(spots, p, d, in_h):
    s = 1 if p < d else -1
    for i in range(p+(s*in_h), d+s, s):
        if spots[i]: return False
    return True

def get_pos(spots, p, l):
    a_p=[]
    for i in range(p+1, len(spots)):
        if spots[i]: break
        a_p.append(i)
    
    for i in range(p-1, -1, -1):
        if spots[i]: break
        a_p.append(i)
    
    d = ltn[l]
    a_p = sorted(a_p, key=lambda x: abs(d-x))
    a_p = [s for s in a_p if s not in [2,4,6,8]]
    return a_p

def calc_cost(p, d, c, in_r, to_r):
    return abs(p-d) * c + c * (in_r + to_r)

def find_best(rooms, spots, cost, least_cost):
    b_s = [None, None, 1E100]
    change = True
    while change:
        change = False

        for p in range(len(spots)):
            if spots[p]:
                l = spots[p]
                d = ltn[l]
                if room_available(rooms, l) and path_clear(spots, p, d, 1):
                    cost += calc_cost(p, d, nrg[l], 0, room_len-len(rooms[d]))
                    spots[p] = None
                    rooms[d].insert(0,l)
                    change = True
        
        for nr, room in rooms.items():
            if not room:
                continue

            l = rooms[nr][0]
            d = ltn[l]
            if d == nr:
                continue

            if room_available(rooms, l) and path_clear(spots, nr, d, 0):
                cost += calc_cost(nr, d, nrg[l], (room_len+1)-len(rooms[nr]), room_len-len(rooms[d]))
                rooms[nr].remove(l)
                rooms[d].insert(0,l)
                change = True

    if cost > least_cost:
        return b_s
    
    if all_complete(rooms):
        return [rooms, spots, cost]
    
    for nr, room in rooms.items():
        if not room or room_complete(nr, room):
            continue
        
        l = rooms[nr][0]
        cont = True
        for i in range(len(room)-1,-1,-1):
            if ltn[room[i]] != nr:
                cont = False
                break
        
        if cont: continue

        states = []
        a_s = get_pos(spots, nr, l)
        for p in a_s:
            tmp_cost = calc_cost(nr, p, nrg[l], (room_len+1)-len(rooms[nr]), 0) + cost
            if tmp_cost > least_cost:
                continue

            c_r = copy.deepcopy(rooms)
            c_r[nr].pop(0)

            c_s = spots[:]
            c_s[p] = l
            states.append([c_r, c_s, tmp_cost])
        
        for state in states:
            if state[2] > least_cost:
                continue

            r_s = find_best(state[0], state[1], state[2], least_cost)
            if r_s[2] < least_cost and all_complete(r_s[0]):
                least_cost = r_s[2]
                b_s = copy.deepcopy(r_s)
        
    return b_s



def main():
    rooms, spots = read_input()
    b_s = find_best(rooms, spots, 0, 1E100)

    print("Final solution")
    status(b_s[0], b_s[1], b_s[2])

if __name__ == "__main__":
    main()