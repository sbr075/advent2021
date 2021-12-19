def read_input():
    with open("input.txt", "r") as file:
        data = [list(l) for l in file.read().splitlines()]
        for d in data:
            for i in range(len(d)-1):
                if d[i].isnumeric() and d[i+1].isnumeric():
                    d[i]+=d[i+1]
                    del d[i+1]
        return data

def explode(l):
    n=0
    for i in range(len(l)):
        n += 1 if l[i] == "[" else -1 if l[i] == "]" else 0 
        if n>4 and l[i].isnumeric() and l[i+2].isnumeric():
            for j in range(i-3, 0, -1):
                if l[j].isnumeric():
                    l[j] = str(int(l[j]) + int(l[i]))
                    break
            
            for j in range(i+5, len(l)):
                if l[j].isnumeric():
                    l[j] = str(int(l[i+2]) + int(l[j]))
                    break

            l[i-1] = "0"
            del l[i:i+4]
            return 1
    return 0

def split(l):
    for i in range(len(l)):
        if l[i].isnumeric():
            int_l = int(l[i])
            if int_l > 9:
                lv = str(int_l // 2)
                rv = str(-(-int_l // 2))
                l[i] = ["[", lv, ",", rv, "]"]
                l[i-1:i+1] = [i for s in l[i-1:i+1] for i in s]
                return 1
    return 0

def add(r, l):
    return list("[" + "".join(r) + "," + "".join(l) + "]")

def calc_magnitude(l):
    while len(l) > 0 and not l[0].isnumeric():
        for i in range(len(l)-2):
            if l[i].isnumeric() and l[i+2].isnumeric():
                l[i-1] = str(3*int(l[i]) + 2*int(l[i+2]))
                del l[i:i+4]
                break
    return int(l[0])

def do_actions(data):
    r = None
    for d in data:
        if r:
            d = add(r, d)
        while 1:
            if explode(d):
                continue
            if split(d):
                continue
            break
        r = d

    return calc_magnitude(r)

def main():
    data = read_input()

    print(f"Part 1 {do_actions(data)}")    

    m = 0
    for d1 in data:
        for d2 in data:
            if d1 == d2:
                continue
            
            ws = [[d1, d2], [d2, d1]]
            for w in ws:
                r = do_actions(w)
                if r > m:
                    m = r

    print(f"Part 2 {m}")

if __name__ == "__main__":
    main()