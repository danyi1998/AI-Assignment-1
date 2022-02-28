import json 

def uniform_cost_search(goal, start):
    
        global graph,cost

        # ucs tree
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

                # get the top element of the
                queue = sorted(queue)
                p = queue[-1]

                # pop the element
                del queue[-1]

                # get the original value
                p[0] *= -1

                # check if the element is part of
                # the goal list
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
                                # update parent
                                tree[p[1]] = p[2]
                                
                                # return [answer, visited]
                                return [answer, tree]

                # check for the non visited nodes
                # which are adjacent to present node
                if (p[1] not in visited):
                        for i in range(len(graph[str(p[1])])):

                                # value is multiplied by -1 so that
                                # least priority is at the top
                                queue.append( [(p[0] + cost[str(p[1]) + "," + graph[str(p[1])][i]])* -1, int(graph[str(p[1])][i]), p[1]])

                                # put the child:parent into tree
                                tree[p[1]] = p[2] 

                                

                # mark as visited
                visited[p[1]] = 1

        # return [answer, visited]
        return [answer, tree]


# create the graph

# add edge 
# graph = {"1": ["2", "4"], "2": ["7"], "3": ["2"], "4": ["2", "7", "5"], "5": ["3", "6"], "6": ["3", "7"], "7": ["5"]}
f = open("G.json")
graph = json.load(f)
f.close()

# add the distance  
# cost = {"1,2": 2, "1,4": 5, "2,7": 1, "4,2": 5, "4,7": 6, "4,5": 2, "3,2": 4, "5,3": 4, "5,6": 3, "6,3": 6, "6,7": 3, "7,5": 7}
f = open("Dist.json")
cost = json.load(f)
f.close()

# start state
start_node = 1

# goal state
goal = [50]

# get the answer
returned_data = uniform_cost_search(goal, start_node)
answer = returned_data[0]

# visited_path = returned_data[1]
tree = returned_data[1] 

# print the answer
print("Minimum cost from 1 to 50 is = ",answer[0])

# solution path
solution = goal

while solution[-1] != start_node:
        # to solution append the parent node
        solution.append(tree[solution[-1]])
        

solution.reverse()
print(solution) 

'''
# solution path
solution = goal

while solution[-1] != start_node:
        for key in visited_path:
                if str(key) in graph[str(solution[-1])]:
                        solution.append(key)
                        break 
solution.reverse()          
print(solution)
'''

