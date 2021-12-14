# answer 1581

def read_input():
    with open("input.txt", "r") as file:
        input = [int(line[:-1]) for line in file.readlines()]
    
    return input    
    
def main():
    input = read_input()

    increases = 0

    base = input[0]
    last = base
    for value in input[1:]:
        if value > base and value > last:
            increases += 1
        else:
            base = value
        
        last = value
        
    print(increases)

if __name__ == "__main__":
    main()