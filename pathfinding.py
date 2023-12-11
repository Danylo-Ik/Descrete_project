from typing import List
import math

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

	graph_list = [[random.randrange(1, 100) for k in range(width)] for i in range(length)]
	return graph_list

def find_shortest_path(graph: list, step: int, start: tuple, end: tuple) -> List[tuple]:
	"""
 	find the shortest path between two points and return list of pairs of indexes
  	"""
	def heuristic(current: tuple, goal: tuple, step: int):
		"""
		find approximate distance between start and end points
		"""
		dist = step * math.sqrt((goal[0] - current[0]) ** 2 + (goal[1] - current[1]) ** 2)
		rel_height = abs(graph[current[0]][current[1]] - graph[goal[0]][goal[1]])
		return math.sqrt(dist ** 2 + rel_height ** 2)

	def cost(current: tuple, next: tuple):
		"""
		find the cost of moving from current point to next point
		"""
		return math.sqrt(step ** 2 + (graph[current[0]][current[1]] - graph[next[0]][next[1]]) ** 2)

	length, width = len(graph), len(graph[0])
	visited = [[False for k in range(width)] for i in range(length)]
	start_coords = (start[0], start[1], 0, heuristic(start, end, step))
	heap = [start_coords]
	
	while heap:
		curr_coords = min(heap, key = lambda x: x[2] + x[3])


