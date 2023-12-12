from typing import List

def read_graph(pathname: str) -> List[List[int]]:
	"""
	read graph from csv file and save it is a list of lists
	[[1,2,3,4,5], [6,7,8,9,10],[11,12,13,14,15]]
	"""
	with open(pathname, 'r', encoding = 'utf-8') as file:
		return [[int(ind.strip()) for ind in line.split(',')] for line in file.readlines()]

def generate_graph(width: int, length: int) -> List[List[int]]:
	"""
 	generate a graph with given length and size and fill it with random heights
  	width - number of int's in every list
   	length - number of lists inside main list
  	"""
	if __name__ == "__main__":
		import random

	graph_list = [[random.randrange(1, 10000) for k in range(width)] for i in range(length)]
	return graph_list

def find_shortest_path(graph: list, step: int, start: tuple, end: tuple) -> List[tuple]:
	"""
 	find the shortest path between two points and return list of pairs of indexes
  	"""
	def heuristic(current: tuple, goal: tuple, step: int):
		"""
		find approximate distance between start and end points
		"""
		return (((current[0] - goal[0]) ** 2 + \
		(current[1] - goal[1]) ** 2) ** 2 + \
		(graph[current[0]][current[1]] - graph[goal[0]][goal[1]]) ** 2) ** 0.5

	def cost(current: tuple, next_coords: tuple):
		"""
		find the cost of moving from current point to next point
		"""
		return (step ** 2 + (graph[current[0]][current[1]] - graph[next_coords[0]][next_coords[1]]) ** 2) ** 0.5

	length, width = len(graph), len(graph[0])
	visited = [[False for k in range(width)] for i in range(length)]
	start_coords = (start[0], start[1], 0, heuristic(start, end, step), [(start[0], start[1])])
	heap = [start_coords]

	while heap:
		curr_coords = min(heap, key = lambda x: x[2] + x[3])
		heap.remove(curr_coords)

		if (curr_coords[0], curr_coords[1]) == end:
			return curr_coords[4]

		visited[curr_coords[0]][curr_coords[1]] = True
		neighbors = [(curr_coords[0] + 1, curr_coords[1]), \
(curr_coords[0] - 1, curr_coords[1]), \
(curr_coords[0], curr_coords[1] + 1), \
(curr_coords[0], curr_coords[1] - 1)]

		for i, j in neighbors:
			if 0 <= i < length and 0 <= j < width and not visited[i][j]:
				cost_value = cost(curr_coords, (i, j))
				heuristic_value = heuristic((i, j), end, step)
				new_path = curr_coords[4] + [(i, j)]
				new_coords = (i, j, cost_value, heuristic_value, new_path)
				heap.append(new_coords)

	return []

def main():
	"""
	main function
	"""
	graph = read_graph('graph.csv')
	print(find_shortest_path(graph, 1, (0, 0), (9, 9)))

if __name__ == "__main__":
	main()