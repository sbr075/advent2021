lut = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"
    }

def read_input():
    with open("input.txt", "r") as file:
        return "".join([lut[c] for c in file.read()])

def get_packets(data, p):
    version = data[p:p+3]; p+=3
    type_id = data[p:p+3]; p+=3
    packet_info = [version, type_id]
    if type_id == "100":
        b = ""
        while True:
            b += data[p+1:p+5]
            if not int(data[p]):
                break
            p+=5
        p+=5
        packet_info.append(int(b,2))

    else:
        type_id_l = data[p:p+1]; p+=1
        packet_l = 15 if type_id_l == "0" else 11
        spi = int(data[p:p+packet_l], 2)
        p+=packet_l

        sub_packets = []
        if packet_l == 15:
            tmp = p + spi
            while p < tmp:
                sub_packet, p = get_packets(data, p)
                sub_packets += [sub_packet]
        else:
            for i in range(spi):
                sub_packet, p = get_packets(data, p)
                sub_packets += [sub_packet]

        packet_info.append(sub_packets)
    return packet_info, p

def sum_versions(packets):
    v = int(packets[0], 2)
    t = int(packets[1], 2)
    if t == 4: return v

    s = v
    for sp in packets[2]:
        s += sum_versions(sp)
    return s

def calc_packets(packets):
    t = int(packets[1], 2)
    if t == 4:
        return packets[2]

    values = []
    for sp in packets[2]:
        values.append(calc_packets(sp))
    
    if t == 0:
        values = sum(values)
    elif t == 1:
        s = 1
        for v in values:
            s*=v
        values = s
    elif t == 2:
        values = min(values)
    elif t == 3:
        values = max(values)
    elif t == 5:
        values = 1 if values[0] > values[1] else 0
    elif t == 6:
        values = 1 if values[0] < values[1] else 0
    elif t == 7:
        values = 1 if values[0] == values[1] else 0
    
    return values

def main():
    data = read_input()
    packets, _ = get_packets(data, 0)
    print(sum_versions(packets))
    print(calc_packets(packets))

if __name__ == "__main__":
    main()