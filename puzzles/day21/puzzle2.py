from functools import cache

outcomes = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

def read_input():
    with open("input.txt", "r") as file:
        return [int(p[28:]) for p in file.read().splitlines()]

@cache
def mod(i,j):
    return ((i-1) % j) + 1

@cache
def play(state, turn):
    if state[1] > 20 or state[3] > 20:
        return (state[4],0) if state[1] > 20 else (0,state[4])

    wins = (0,0)
    for r,f in outcomes.items():
        pos = mod(state[turn*2]+r, 10)
        score = state[turn*2+1] + pos
        if turn:
            new_state = (state[0], state[1], pos, score, state[4]*f)
        else:
            new_state = (pos, score, state[2], state[3], state[4]*f)
        wins = tuple(map(sum, zip(wins, play(new_state, 1-turn))))

    return wins

def main():
    data = read_input()
    state = (data[0],0,data[1],0,1) #p1 pos, p1 score, p2 pos, p2 score, num games
    print(f"Part 2 {max(play(state, 0))}")

if __name__ == "__main__":
    main()