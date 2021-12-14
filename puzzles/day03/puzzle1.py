def read_input():
    with open("input.txt", "r") as file:
        input = [line[:-1] for line in file.readlines()]
    
    return input

def main():
    input = read_input()

    bit_count = {}

    for line in input:
        for i in range(len(line)):
            bit = int(line[i])

            if i not in bit_count:
                bit_count[i] = [0, 0]
            
            bit_count[i][bit] += 1
    
    gamma = ""
    epsilon = ""

    for _, value in bit_count.items():
        if value[0] > value[1]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    
    print(int(gamma, 2) * int(epsilon, 2))
    

if __name__ == "__main__":
    main()