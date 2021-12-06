def read_input():
    with open("input.txt", "r") as file:
        return [int(a) for a in file.readline().split(",")]

def main(days):
    data = read_input()

    # Keep track of how many fishes are in each age category
    l = [0 for i in range(9)]
    for i in data:
        l[i] += 1
    
    for i in range(days):
        tmp = l.pop(0) # Remove first element of list
        l[6] += tmp
        l.append(tmp)

    print(sum(l))

if __name__ == "__main__":
    main(80)
    main(256)