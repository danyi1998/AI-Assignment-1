# this code allows for multiple goal states, but in our assignment we just have one 

import json

def uniform_cost_search(goal, start):
    
        global graph,cost

        # tree contains child node : parent node
        tree = {} 
        
        answer = []

        # create a priority queue
        queue = []

        # set the answer vector to max value
        for i in range(len(goal)):
                answer.append(10**8)

        # insert the starting index and parent 
        queue.append([0, start, 0])

        # map to store visited node
        visited = {}

        # count
        count = 0

        # while the queue is not empty
        while (len(queue) > 0):

                # get the smallest distance in the queue 
                queue = sorted(queue)
                p = queue[-1]

                # delete from queue 
                del queue[-1]

                # get the absolute value of the distance 
                p[0] *= -1

                # check if the element is in goal 
                if (p[1] in goal):

                        # get the position
                        index = goal.index(p[1])

                        # if a new goal is reached
                        if (answer[index] == 10**8):
                                count += 1

                        # if the cost is less
                        if (answer[index] > p[0]):
                                answer[index] = p[0]

                        # pop the element
                        del queue[-1]

                        queue = sorted(queue)
                        if (count == len(goal)):
                                # update tree with child node : parent node 
                                tree[p[1]] = p[2]

                                # return from function
                                return [answer, tree]

                # before expanding, check if the node has been visited/expanded before 
                if (p[1] not in visited):
                        # for each neighbour of the current node p[1] 
                        for i in range(len(graph[str(p[1])])):

                                # value is multiplied by -1 so that least priority is at the top
                                queue.append( [(p[0] + cost[str(p[1]) + "," + graph[str(p[1])][i]])* -1, int(graph[str(p[1])][i]), p[1]])

                                # put the child node : parent node into tree
                                tree[p[1]] = p[2] 

                # mark as visited
                visited[p[1]] = 1

        return [answer, tree]  


# load the graph
f = open("G.json")
graph = json.load(f)
f.close() 

# add the distance 
f = open("Dist.json")
cost = json.load(f)
f.close() 

# start node
start_node = 1 

# goal state
goal = [50]   

# call the ucs function 
returned_data = uniform_cost_search(goal, start_node)

# get the distance 
answer = returned_data[0]

# get the tree which contains the child node:parent node 
tree = returned_data[1] 

# print the answer
print("Minimum cost from " + str(start_node) + " to " + str(goal[0]) + " is = ", answer[0])

# solution path
solution = goal

# while the solution path does not yet contain the start node
while solution[-1] != start_node:
        # to solution we append the parent of the last item (node)
        solution.append(tree[solution[-1]])

# to go from the start node to the goal node 
solution.reverse()

# print solution path
print(solution)

