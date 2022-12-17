import re


#Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
class Valve:
    def __init__(self, name, neighbours, flow):
        self.name = name
        self.neighbours = neighbours
        self.flow = flow

    def __str__(self):
        return f'Valve {self.name} has a flow rate={self.flow}; tunnels lead to valves {self.neighbours}'


def bfs(valves, current):
    steps = 0
    q = [(current, steps)]
    visited = {}
    while q:
        current, steps = q.pop(0)
        current = valves[current]
        for neighbour in current.neighbours:
            if steps > 30:
                return visited
            if neighbour not in visited:
                q.append((neighbour, steps + 1))
                visited[neighbour] = steps + 1

    return visited


def paths(valves, current, flows, time=30, exclude=set()):
    steps = 0
    q = [(current, list(), steps, 0)]
    _paths = []
    highest = 0
    best_path = []
    while q:
        q.sort(key=lambda tup: tup[-2])
        current, path, steps, total_flow = q.pop(0)
        if steps >= time:
            print(highest, best_path)
            return highest, best_path
        total_flow += ((time-steps)*flows[current].flow)
        path.append((current, steps, total_flow))
        if total_flow > highest:
            highest = total_flow
            best_path = path
            print(total_flow, path)
        for neighbour in valves[current]:
            if neighbour not in [p[0] for p in path] and neighbour not in exclude:
                q.append((neighbour, path[:], steps+valves[current][neighbour]+1, total_flow))
    return highest, best_path


def calculate_flow(p, distmap, valves):
    flow = 0
    seconds_left = 30
    current = "AA"
    while seconds_left > 0 and p:
        next = p.pop(0)
        cost = distmap[current][next]
        if cost < seconds_left:
            seconds_left -= (cost+1)
            flow += valves[next].flow * seconds_left
            current = next
        else:
            break
    return flow


def main():
    with open("day16.txt", 'r') as f:
        data = f.read().split('\n')

    valves = {}
    for d in data:
        _valves = re.findall('[A-Z]{2}', d)
        flow = int(re.findall('-?\d+', d)[0])
        valves[_valves[0]] = Valve(_valves[0], _valves[1:], flow)

    # create map with distances from - to all nodes within 30s reach
    distmap = {}
    for v in valves:
        distmap[v] = bfs(valves, v)
    for d in distmap:
        print (d, distmap[d])

    # delete all 0 flow nodes
    for v in valves:
        if valves[v].flow == 0:
            for d in distmap:
                #del d[v]
                del distmap[d][v]
            if v != "AA":
                del distmap[v]
    print()

    for d in distmap:
        print (d, distmap[d])
    print()

    highest1, path1 = paths(distmap, 'AA', valves, 26)
    print(f"{highest1}")

    open_valves = set([t[0] for t in path1[1:]])
    print(open_valves)
    highest2, path2 = paths(distmap, 'AA', valves, 26, open_valves)

    print(highest1 + highest2)





if __name__ == "__main__":
    main()
