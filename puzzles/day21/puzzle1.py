def read_input():
    with open("input.txt", "r") as file:
        return [int(p[28:]) for p in file.read().splitlines()]

mod = lambda i,j: ((i-1) % j) + 1
def main():
    pos = read_input()

    s = [0,0]
    for i in range(1,1000,3):
        pos[(i-1)%2] += sum([mod(j,100) for j in range(i,i+3)])
        pos[(i-1)%2] = mod(pos[(i-1)%2],10)
        s[(i-1)%2] += pos[(i-1)%2]
        if s[(i-1)%2] >= 1000: break
    
    print(f"Part 1 {min(s)*(i+2)}")
 
if __name__ == "__main__":
    main()