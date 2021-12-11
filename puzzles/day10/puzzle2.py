import numpy as np

def read_input():
    with open("input.txt", "r") as file:
        return file.read().splitlines()

icp = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}

e = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

def main():
    data = read_input()

    o = []
    for l in data:
        r = []
        for c in l:
            if c in e:
                r += [c]
            elif c != e[r[-1]]:
                r = []
                break
            else:
                r.pop()
        
        if r:
            o += [r]
    
    for l in o:
        t = 0
        for c in l[::-1]:
            t*=5
            t+=icp[c]
        s+=[t]
    print(sorted(s)[int(len(s)/2)])
    

if __name__ == "__main__":
    main()