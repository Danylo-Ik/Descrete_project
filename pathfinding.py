from typing import List
import random
import heapq

def read_graph(pathname: str) -> List[List[int]]:
    """
    read graph from csv file and save it is a list of lists
    [[1,2,3,4,5], [6,7,8,9,10],[11,12,13,14,15]]
    """
    with open(pathname, 'r', encoding = 'utf-8') as file:
        return [[int(ind.strip()) for ind in line.split(',')] for line in file.readlines()]

def generate_graph(width: int, length: int, max_height: int) -> List[List[int]]:
    """
    generate a graph with given length and size and fill it with random heights
    width - number of int's in every list
    length - number of lists inside main list
    """
    graph_list = [[random.randrange(1, max_height) for k in range(width)] for i in range(length)]
    return graph_list

def find_shortest_path(graph: list, step: int, start: tuple, end: tuple) -> List[tuple]:
    """
    Find the shortest path between two points and return a list of pairs of indexes.
    """
    def heuristic(current: tuple, goal: tuple):
        """
        Find the approximate distance between start and end points.
        """
        dx = step * (goal[0] - current[0])
        dy = step * (goal[1] - current[1])
        dz = graph[goal[0]][goal[1]] - graph[current[0]][current[1]]
        return (dx ** 2 + dy ** 2 + dz ** 2) ** 0.5

    def cost(current: tuple, next_coords: tuple):
        """
        Find the cost of moving from the current point to the next point.
        """
        cath_1 = (graph[next_coords[0]][next_coords[1]] - graph[current[1]][current[2]]) ** 2
        cath_2 = step ** 2
        return (cath_1 + cath_2) ** 0.5

    length, width = len(graph), len(graph[0])
    visited = set()
    start_coords = (heuristic(start, end), start[0], start[1], [(start[0], start[1])])
    heap = [start_coords]

    while heap:
        curr_coords = heapq.heappop(heap)

        if (curr_coords[1], curr_coords[2]) == end:
            return curr_coords[3]

        if (curr_coords[1], curr_coords[2]) in visited:
            continue

        visited.add((curr_coords[1], curr_coords[2]))
        neighbors = [(curr_coords[1] + 1, curr_coords[2]),
                     (curr_coords[1] - 1, curr_coords[2]),
                     (curr_coords[1], curr_coords[2] + 1),
                     (curr_coords[1], curr_coords[2] - 1)]

        for i, j in neighbors:
            if 0 <= i < length and 0 <= j < width and (i, j) not in visited:
                cost_value = cost(curr_coords, (i, j))
                heuristic_value = heuristic((i, j), end)
                new_path = curr_coords[3] + [(i, j)]
                new_coords = (heuristic_value + cost_value, i, j, new_path)
                heapq.heappush(heap, new_coords)

    return []

def main():
    """
    main function
    """
    graph = generate_graph(3, 3, 10)
    if len(graph) <= 10:
        for line in graph:
            print(line)
    print(find_shortest_path(graph, 1, (0, 0), (2, 2)))

if __name__ == "__main__":
    main()