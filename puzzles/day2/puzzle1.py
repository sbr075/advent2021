def read_input():
    with open("input.txt", "r") as file:
        input = [line[:-1].split(" ") for line in file.readlines()]
    
    return input

def main():
    input = read_input()

    horizontal = 0
    depth = 0

    for line in input:
        action = line[0]
        value = int(line[1])

        if action == "forward":
            horizontal += value
        elif action == "down":
            depth += value
        else:
            depth -= value

    print(depth * horizontal)

if __name__ == "__main__":
    main()