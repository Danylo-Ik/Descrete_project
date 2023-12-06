def read_graph(pathname: str) -> List(List(int))):
	"""
	read graph from csv file and save it is a list of lists
	[[1,2,3,4,5], [6,7,8,9,10],[11,12,13,14,15]]
	"""
	with open(pathname, 'r', encoding = 'utf-8') as file:
		return [[int(ind.strip()) for ind in line.split(',')] for line in file.readlines()]

def generate_graph(width: int, length: int) -> List(List(int))):
	"""
 	generate a graph with given length and size and fill it with random heights
  	width - number of int's in every list
   	length - number of lists inside main list
  	"""
	pass
	

def find_shortest_path(graph: List(List(int)), step: int, start: tuple(int, int), end: tuple(int, int) -> List(tuple(int, int):
	"""
 	find the shortest path between two points and return list of pairs of indexes
  	"""
	pass
	
