import re
from copy import deepcopy
from tqdm import tqdm


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


def paths(valves, current, flows, time=30):
    steps = 0
    q = [[[[current, steps], [current, steps]], [current], 0]]
    _paths = []
    highest = 0
    best_path = []
    pbar = tqdm(total=10000000)
    while q:
        #q.sort(key=lambda tup: tup[-1], reverse=True)
        playerstats, path, total_flow = q.pop(0)
        if playerstats[0][1] >= time and playerstats[1][1] >= time:
            #print(highest, best_path)
            print(total_flow, "broke", q[-1])
            #return highest, best_path
        else:
            currentplayer = 1
            if playerstats[0][1] < playerstats[1][1]:
                currentplayer = 0
            for neighbour in valves[playerstats[currentplayer][0]]:
                if neighbour not in path:
                    new_steps = playerstats[currentplayer][1]+valves[playerstats[currentplayer][0]][neighbour]+1
                    if new_steps <= time:

                        ctotalflow = total_flow + ((time - new_steps) * flows[neighbour].flow)
                        cpath = deepcopy(path)
                        cpath.append(neighbour)
                        cplayerstats = deepcopy(playerstats)
                        cplayerstats[currentplayer][0] = neighbour
                        cplayerstats[currentplayer][1] = new_steps
                        if cplayerstats[0][1] < time-1 or cplayerstats[1][1] < time-1:
                            pbar.update(1)
                            q.append([cplayerstats, cpath, ctotalflow])
                        if ctotalflow > highest:
                            highest = ctotalflow
                            best_path = cpath
                            print(ctotalflow, cpath)
    pbar.close()

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


if __name__ == "__main__":
    main()
