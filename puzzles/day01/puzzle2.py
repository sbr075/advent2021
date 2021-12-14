# answer 1618

def read_input():
    with open("input.txt", "r") as file:
        input = [int(line[:-1]) for line in file.readlines()]
    
    return input    
    
def main():
    input = read_input()

    increases = 0

    base = None
    for i in range(len(input)-2):
        sum = input[i] + input[i+1] + input[i+2]

        if base == None:
            base = sum
        
        if sum > base:
            increases += 1

        base = sum

    print(increases)

if __name__ == "__main__":
    main()