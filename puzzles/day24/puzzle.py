def read_input():
    chks = []
    adds = []
    with open("input.txt", "r") as file:
        l = file.read().splitlines()
        for i in range(0, len(l), 18):
            chks.append(int(l[i+5][6:]))
            adds.append(int(l[i+15][6:]))
    return chks, adds

def dfs(state, chks, adds, i, p1):
    if i == 14:
        return state
    
    states = []
    for j in range(9 if p1 else 1, 0 if p1 else 10, -1 if p1 else 1):
        if chks[i] > 0:
            states.append([state[0]*26 + j + adds[i], state[1]+str(j)])
        elif j == (chks[i] + (state[0] % 26)):
            states.append([state[0] // 26, state[1]+str(j)])

    for state in states:
        r = dfs(state, chks, adds, i+1, p1)
        if r: return r

def main():
    chks, adds = read_input()

    """
    The input is a full set of 14 subsets of matching operations
    There are three operations that differ
    (div) op 5  - 1 or 26 (negative chk val or positive chk val)
    (chk) op 6  - check value (<0 or >9)
    (add) op 16 - add value

    Three things to notice
    1. If check is negative, z is always divided by 26
    2. If check is negative, there is a change "eql x w" is true
    3. If check is positive, it's always larger than 9
    
    If check is negative then x might become 0. This can only happen if
    check + x % 26 is equal to input. Since y is always multiplied by
    x before ops with z, then y is always 0, and z is not changed.
    Therefor we can skip all other ops in current set of ops

    If check is positive x always ends up at 1, because "eql x w" cannot be true
    Then y is not changed to a 0 before any ops with z, and z is changed. This can
    also happen if notice 2 does not hold since x first becomes 0 before it's 
    comparison with 0 (turning x to 1)

    Since we want z to equal 0 at the final step there needs to be an equal
    number of additions and subtractions. To find the all model numbers we can
    then for each subset of operations create a state of all possible outcomes.
    Then as we hit a subset with a negative check we prune away the ones that
    are not possible. 
    """

    print("Part 1 {}".format(dfs((0, ""), chks, adds, 0, 1)[1]))
    print("Part 2 {}".format(dfs((0, ""), chks, adds, 0, 0)[1]))

if __name__ == "__main__":
    main()