import copy
from os import stat

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

    for s in range(len(spots)):
        if s in [2, 4, 6, 8]:
            try:
                print(f"{rooms[s][0]} ", end="")
            except:
                print("  ", end="")
        else:
            print("  ", end="")
    print()

    for s in range(len(spots)):
        if s in [2, 4, 6, 8]:
            try:
                print(f"{rooms[s][1]} ", end="")
            except:
                print("  ", end="")
        else:
            print("  ", end="")
    print()

def room_available(rooms, a_p, l):
    d = ltn[l]
    if d in a_p:
        if not rooms[d]: return True
        if all(c == l for c in rooms[d]): return True
    
    return False

def room_complete(nr, room):
    if len(room) < 2:      return False
    if room[0] != ntl[nr]: return False
    if len(set(room)) > 1: return False
    return True

def all_complete(rooms):
    for nr,room in rooms.items():
        if not room_complete(nr, room):
            return False

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
    return a_p

def calc_cost(p, d, l, in_r, to_r):
    cost = abs(p-d) * nrg[l]
    cost += nrg[l] * (in_r + to_r)
    return cost

def find_best(rooms, spots, cost, least_cost):
    b_s = [None, None, least_cost]
    
    status(rooms, spots, cost)

    change = True
    while change:
        change = False

        # Iterate over all spots in hallway and see if any can be moved to their rooms
        for p in range(len(spots)):
            l = spots[p]
            if l:
                a_p = get_pos(spots, p, l)
                if room_available(rooms, a_p, l):
                    e_c = calc_cost(p, ltn[l], l, 0, 2-len(rooms[ltn[l]]))
                    print(f"(H) Moving {l} to {ltn[l]} from {p} {e_c}")
                    cost += e_c
                    spots[p] = None
                    rooms[ltn[l]].append(l)
                    change = True

        # Go through all rooms and check if amphipod can move directly to another room
        for nr, room in rooms.items():
            if not room:
                continue
            
            l = rooms[nr][0]
            
            # If letter is in right room, but not room is not complete it needs to move
            if ltn[l] == nr:
                continue
            
            a_p = get_pos(spots, nr, l)
            if room_available(rooms, a_p, l):
                e_c = calc_cost(nr, ltn[l], l, 1, 2-len(rooms[ltn[l]]))
                print(f"(R) Moving {l} to {ltn[l]} from {nr} {e_c}")
                cost += e_c
                rooms[nr].remove(l)
                rooms[ltn[l]].insert(0, l)
                change = True

    status(rooms, spots, cost)
    #input("Click enter to continue...")
    print()

    if cost > least_cost: 
        return b_s

    if all_complete(rooms):
        return [rooms, spots, cost]

    # Get all remaining states
    for nr, room in rooms.items():
        if not room or room_complete(nr, room):
            continue
        
        l = rooms[nr][0]
        if ltn[l] == nr and len(rooms[nr]) == 1: # If letter is in right room, and only one there it can be ignored
            continue
        
        states = []
        a_p = get_pos(spots, nr, l)
        a_p = [s for s in a_p if s not in [2,4,6,8]]
        for p in a_p:
            tmp_cost = calc_cost(nr, p, l, 1, 0) + cost
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
                print(f"New least cost {r_s[2]}")
                status(r_s[0], r_s[1], r_s[2])
                least_cost = r_s[2]
                b_s = copy.deepcopy(r_s)
    
    return b_s

def main():
    rooms, spots = read_input()
    b_s = find_best(rooms, spots, 0, 1E100)

    print("Final solution")
    status(b_s[0], b_s[1], b_s[2])
    print(f"Cost {b_s[2]}")

if __name__ == "__main__":
    main()