def read_input():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()
    
    return data

def count_bits(bits, idx):
    bit_count = [0, 0]

    for bit in bits:
        bit_count[int(bit[idx])] += 1
    
    return bit_count

def most_common_bit(bit_count):
    if bit_count[0] > bit_count[1]:
        return "0"
    return "1"

def least_common_bit(bit_count):
    if bit_count[0] > bit_count[1]:
        return "1"
    return "0"

def main():
    data = read_input()

    oxygen = data
    scrubber = data
    
    # Find oxygen generator rating
    idx = 0
    while len(oxygen) != 1:
        bit_count = count_bits(oxygen, idx)
        o_common = most_common_bit(bit_count)

        oxygen = [bits for bits in oxygen if bits[idx] == o_common]
        idx += 1

    # Find CO2 scrubber rating
    idx = 0
    while len(scrubber) != 1:
        bit_count = count_bits(scrubber, idx)
        c_common = least_common_bit(bit_count)

        scrubber = [bits for bits in scrubber if bits[idx] == c_common]
        idx += 1

    print(int(oxygen[0], 2) * int(scrubber[0], 2))

if __name__ == "__main__":
    main()