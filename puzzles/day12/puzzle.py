def read_input():
    with open("input.txt", "r") as file:
        data = [f.split("-") for f in file.read().splitlines()]
    return data

def update_graph(graph, p1, p2):
    if p2 != "start":
        if p1 not in graph:
            graph[p1] = set([p2])
        else:
            graph[p1].add(p2)

def dfs(graph, l, v, twice):
    if l == "end": return 1
    tot = 0
    for p in graph[l]:
        if p.isupper():
            tot += dfs(graph, p, v, twice)
        else:
            if p not in v:
                tot += dfs(graph, p, v | {p}, twice)
            elif twice:
                tot += dfs(graph, p, v, False)
    return tot


def main():
    data = read_input()

    graph = {}
    for d in data:
        update_graph(graph, d[0], d[1])
        update_graph(graph, d[1], d[0])
    
    print(dfs(graph, "start", set(), False))
    print(dfs(graph, "start", set(), True))
    
if __name__ == "__main__":
    main()