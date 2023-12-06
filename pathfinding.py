from typing import List
def read_graph(pathname: str) -> List[List[int]]:
	"""
	read graph from csv file and save it is a list of lists
	[[1,2,3,4,5],
	[6,7,8,9,10],
	[11,12,13,14,15]]
	"""
	pass

def generate_graph(width: int, length: int) -> List[List[int]]:
	"""
 	generate a graph with given length and size and fill it with random heights
  	width - number of int's in every list
   	length - number of lists inside main list
  	"""
	import random
	graph_list = [[random.randrange(1, 10) for k in range(width)] for i in range(length)]
	return graph_list
print(generate_graph(7, 5))
	

def find_shortest_path(graph, step, start, end):
	"""
 	find the shortest path between two points and return list of pairs of indexes
  	"""
	pass
	
