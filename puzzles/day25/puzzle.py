import numpy as np

def read_input():
    with open("input.txt", "r") as file:
        arr = np.array([[c for c in l] for l in file.read().splitlines()])
        return arr

def main():
    data = read_input()
    h,w = data.shape

    steps = 0
    move = True
    while move:
        move = False
        t_data = data.copy()
        for y in range(h):
            for x in range(w):
                if data[y,x] == ">" and data[y,(x+1)%w] == ".":
                    t_data[y,(x+1)%w] = ">"
                    t_data[y,x] = "."
                    move = True
        
        data = t_data
        t_data = data.copy()
        for y in range(h):
            for x in range(w):
                if data[y,x] == "v" and data[(y+1)%h,x] == ".":
                    t_data[(y+1)%h,x] = "v"
                    t_data[y,x] = "."
                    move = True
        
        data = t_data
        steps += 1
        
    print(f"Part 1 {steps}")

if __name__ == "__main__":
    main()