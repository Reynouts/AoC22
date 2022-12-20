import functools
import re
from copy import deepcopy


# Very messy late night slow code. But gets the answer after some sleep.
# Perfect!


current_bp = 0
max_needed = 0

@functools.cache
def cyclo(ro1, ro2, ro3, ro4, re1, re2, re3, re4, minutes):
    global max_needed
    global current_bp
    robots = {"ore": ro1, "clay": ro2, "obsidian": ro3, "geode": ro4}
    resources = {"ore": re1, "clay": re2, "obsidian": re3, "geode": re4}

    if minutes == 32:
        return resources["geode"], robots["geode"]
    new_robots = [""]
    for name in ["ore", "clay", "obsidian", "geode"]:
        need = current_bp[name]
        can_buy = True
        for n in need:
            if resources[n] < need[n]:
                can_buy = False
        if can_buy:
            if max_needed[name] > robots[name] or name == "geode":
                new_robots.append(name)
    # collect resources
    for r in robots:
        resources[r] += robots[r]
    if "geode" in new_robots:
        new_robots = ["geode",]
    results = []
    for r in new_robots:
        if r == "":
            res = cyclo(robots["ore"], robots["clay"], robots["obsidian"], robots["geode"], resources["ore"], resources["clay"], resources["obsidian"], resources["geode"], minutes+1)
            if res == None:
                results.append((0, 0))
            else:
                results.append(res)
        else:
            crobots = deepcopy(robots)
            cresources = deepcopy(resources)
            need = current_bp[r]
            for n in need:
                cresources[n] -= need[n]
            crobots[r] += 1
            res = cyclo(crobots["ore"], crobots["clay"], crobots["obsidian"], crobots["geode"], cresources["ore"], cresources["clay"], cresources["obsidian"], cresources["geode"], minutes+1)
            if res == None:
                results.append((0, 0))
            else:
                results.append(res)
    highest = 0
    robo = 0
    for i in results:
        if i[0] > highest:
            highest = i[0]
            robo = i[1]
    return highest, robo



def main():
    with open("day19.txt", 'r') as f:
        data = f.read().split('\n')

    blueprints = []

    robots = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}
    resources = {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0}
    robot_names = list(resources)
    for d in data:
        number = int(d.split("Blueprint ")[1][0])
        print(number)
        blueprint = {}
        for index, robot in enumerate(d.split(".")[:-1]):
            numbers = [(int(n[0]), n[1]) for n in list(re.findall("(\d+) ([a-z]+)", robot))]
            r = {}
            for n in numbers:
                r[n[1]] = n[0]
            blueprint[robot_names[index]] = r
        blueprints.append(blueprint)

    global current_bp
    global max_needed
    geodes = []
    quality_levels = []
    for index, cbp in enumerate(blueprints):
        current_bp = cbp
        max_needed = {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0}
        for name in current_bp:
            for need in max_needed:
                if need in current_bp[name] and current_bp[name][need] > max_needed[need]:
                    max_needed[need] = current_bp[name][need]
        g, robo = cyclo(1, 0, 0, 0, 0, 0, 0, 0, 0)
        geodes.append(g)
        quality_levels.append(g*(index+1))
        cyclo.cache_clear()
    print("ANSWER:", sum(quality_levels))
    print(geodes[0]*geodes[1]*geodes[2])




if __name__ == "__main__":
    main()