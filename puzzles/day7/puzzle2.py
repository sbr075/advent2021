def read_input():
    with open("input.txt", "r") as file:
        return [int(a) for a in file.readline().split(",")]

def s(n):
    return (n*(n+1))//2

def main():
    data = read_input()

    lc = 10E100
    for i in range(min(data),max(data)):
        t = sum([s(abs(d-i)) for d in data])
        if t < lc:
            lc = t
    
    print(lc)

if __name__ == "__main__":
    main()