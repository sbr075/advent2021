def read_input():
    with open("input.txt", "r") as file:
        return {v[0]:v[1] for v in [l.split(" -> ") for l in file.read().splitlines()]}

def updt(d, k, v):
    d[k] = v if k not in d else d[k] + v

def main(temp, steps):
    p_i = read_input()

    pairs = {}
    [updt(pairs, temp[i:i+2], 1) for i in range(len(temp))]
    for i in range(steps):
        n_p = {}
        for p,c in pairs.items():
            if p in p_i:
                updt(n_p, p[0]+p_i[p], c)
                updt(n_p, p_i[p]+p[1], c)
        pairs = n_p

    c = {temp[-1]:1}
    for p,v in pairs.items():
        updt(c, p[0], v)
    print(max(c.items(), key=lambda x: x[1])[1]-min(c.items(), key=lambda x: x[1])[1])

if __name__ == "__main__":
    main("SCVHKHVSHPVCNBKBPVHV", 10)
    main("SCVHKHVSHPVCNBKBPVHV", 40)