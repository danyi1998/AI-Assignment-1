def uniform_cost_search(goal, start):
    
	global graph,cost
	answer = []

	# create a priority queue
	queue = []

	# set the answer vector to max value
	for i in range(len(goal)):
		answer.append(10**8)

	# insert the starting index
	queue.append([0, start])

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
				return answer

		# check for the non visited nodes
		# which are adjacent to present node
		if (p[1] not in visited):
			for i in range(len(graph[str(p[1])])):

				# value is multiplied by -1 so that
				# least priority is at the top
				queue.append( [(p[0] + cost[str(p[1]) + ", " + graph[str(p[1])][i]])* -1, int(graph[str(p[1])][i])])

		# mark as visited
		visited[p[1]] = 1

	return answer


# create the graph

# add edge 
graph = {"1": ["2", "4"], "2": ["7"], "3": ["2"], "4": ["2", "7", "5"], "5": ["3", "6"], "6": ["3", "7"], "7": ["5"]} 

# add the distance  
cost = {"1, 2": 2, "1, 4": 5, "2, 7": 1, "4, 2": 5, "4, 7": 6, "4, 5": 2, "3, 2": 4, "5, 3": 4, "5, 6": 3, "6, 3": 6, "6, 7": 3, "7, 5": 7}

# goal state
goal = [7]  

# get the answer
answer = uniform_cost_search(goal, 1)

# print the answer
print("Minimum cost from 1 to 7 is = ",answer[0])

print(graph)
print(cost)
