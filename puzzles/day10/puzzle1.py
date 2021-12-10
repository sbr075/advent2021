def read_input():
    with open("input.txt", "r") as file:
        return file.read().splitlines()

e = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

def main():
    data = read_input()

    cor = {
        ")": [0, 3],
        "]": [0, 57],
        "}": [0, 1197],
        ">": [0, 25137]
    }

    o = []
    for l in data:
        for c in l:
            if c in e:
                o+=[c]
            elif c == e[o[-1]]:
                o.pop()
            else:
                cor[c][0]+=1
                break

    print(sum([v[0]*v[1] for _,v in cor.items()]))

if __name__ == "__main__":
    main()