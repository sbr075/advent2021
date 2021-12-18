def read_input():
    with open("input.txt", "r") as file:
        d = [c[2:].split("..") for c in file.read()[13:].split(", ")]
        return [int(i) for s in d for i in s]

def bruteforce(y_v, x_v, b):
    x,y = 0,0
    while True:
        x+=x_v
        y+=y_v
        if b[0] <= x <= b[1] and b[2] <= y <= b[3]:
            return 1
        elif x > b[1] or y < b[2]:
            return 0
        x_v -= 1 if x_v > 0 else 0
        y_v -= 1

def main():
    data = read_input()

    print(f"Part 1 {sum([y for y in range(-data[2])])}")

    p = 0
    for y_v in range(data[2], -data[2]+1):
        for x_v in range(data[1]+1):
            p+=bruteforce(y_v, x_v, data)
    print(f"Part 2 {p}")

if __name__ == "__main__":
    main()