import math
from queue import PriorityQueue

def get_h(childNode: str, desNode: str ,Coord: dict):
#     get heuristic
    dx = Coord[childNode][0] - Coord[desNode][0]
    dy = Coord[childNode][1] - Coord[desNode][1]
    return math.sqrt(dx**2 +dy**2)

def get_energyUsed(path: list, cost: dict):
#     get energyUsed in the path
    if len(path) <= 1:
        energyUsed = 0
    else:
        energyUsed = 0
        for i in range(len(path) - 1):
            energyUsed += cost[f"{path[i]},{path[i+1]}"]
    return energyUsed

def get_totalDist(path: list, dist: dict):
#     get totalDistance in the path
    if len(path) <= 1:
        totalDist = 0
    else:
        totalDist = 0
        for i in range(len(path) - 1):
            totalDist += dist[f"{path[i]},{path[i+1]}"]
    return totalDist

def printPath(path: list):
    path = "->".join(path)
    path = "Shortest path: " + path 
    print(path)


def get_task3_path(curNode: str , desNode: str, energyBudget: int, Coord: dict, Cost: dict, Dist: dict, G: dict):
#    initialising Priority Queue, current path as curPath, visited list, score as fn, and energyUsed = 0.
    pQue = PriorityQueue()
    curPath = [curNode]
    newPath = curPath
    visited = []
    fn = 0
    energyUsed = 0
    accumulated_dist = 0 
    pQue.put((fn,(energyUsed, curPath, accumulated_dist)))
#    put the source node in the queue

    while not pQue.empty():
#         get the entry with the least score, and assign variables energyUsed and current path respectively, curNode (current node) is assigned as the last node in the path
        pathInfo = pQue.get() 
        energyUsed, curPath, accumulated_dist = pathInfo[1]
        curNode = curPath[-1]
            
        # if current node  = destination node, prrint the requirements and call printPath() method to achieve required format
        if curNode == desNode:
            print('Task 3')
            printPath(curPath)
            print('Shortest Distance:',get_totalDist(curPath, Dist))
            print('Total energy cost:', get_energyUsed(curPath, Cost))
            break


        if (curNode not in visited):
            visited.append(curNode)
            
            for nbNode in G[curNode]:
                newEnergy = energyUsed + Cost[f"{curNode},{nbNode}"]
                if newEnergy <= energyBudget:
                    gn = accumulated_dist + Dist[f"{curNode},{nbNode}"]
                    new_accumulated_distance = gn 
                    hn = get_h(nbNode,desNode,Coord)
                    f = gn + hn

                    newPath = curPath.copy()
                    newPath.append(nbNode)
                    pQue.put((f, (newEnergy ,newPath, new_accumulated_distance)))
                    
    return curPath
