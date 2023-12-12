import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.animation import FuncAnimation

# Приклад файлу, який зчитується
# 5,4,3,6,7,5,2
# 3,6,7,5,3,2,1
# 2,5,6,4,2,1,0
# 3,4,5,3,6,7,5
# 6,5,2,4,7,5,3
# 4,5,7,8,4,3,1
# 1,4,6,4,3,2,0
# 0,1,2,3,4,5,6

def transform_tuples_to_lists(tuples):
    lists = [list(t) for t in tuples]
    return lists

def vizualize(path: str, output: list):
    """
    Приклад вводу
    >>> [[0,2],[1,3],[2,4],[3,3],[4,2],[5,1],[6,1]]
    """
    graf = read_graph(path)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    len_x = len(graf[0]) #довжина графа
    len_y = len(graf) #висота графа
    # дані, щоб побудувати граф
    l = [int(graf[j][i]) for j in range(len_y) for i in range(len_x)] #ліст всіх значень висто справа наліво, зверху вниз
    f = [i+1 for i in range(len_y*len_x)] #ліст з номерацією, щоб створити дікшенарі з носерами
    d = dict(zip(f, l)) #дікшенарі, де кожна висота прономерована, нумерація з 1 починається

    # наступні рядочки(до X, Y, Z = нам будують нам нашу матирцю)
    # встановлюємо координати
    x_coord_range = [i for i in range(len(graf[0]))] #х в ренджі довжини графа
    y_coord_range = [i for i in range(len(graf))] #y в ренджі висоти графа
    z_coord = graf

    X, Y = np.meshgrid(x_coord_range, y_coord_range) # оскільки x та y "обмежені", тобто не є на всю площу,
    # то ця функція умовно їх перемножує, і створює наче декартові координати
    Z = np.array(z_coord) #оскільки z має на кожну координату "відповідь", то її задаємо цією функцією
    ax.plot_surface(X, Y, Z, cmap="plasma", alpha=0.7) # нарешті будуємо
    ax.plot_wireframe(X, Y, Z, color='black', linewidth=0.5)

    # будуємо пряму
    # output = [[0,2],[1,3],[2,4],[3,3],[4,2],[5,1],[6,1]] #наш гіпотетичний вивід з функції A*
    z = [d[(el[1])*len_x + (el[0]+1)] for el in output] #ліст значень вершин для нашого аутпуту(математика тупа)
    line_coords = [(output[i][0], output[i][1], z[i]) for i in range(len(z))]
    # тут у нас ліст координат, крізь які має проходити наша лінія
    line_x, line_y, line_z = zip(*line_coords)
    ax.plot(line_x, line_y, line_z, color='green', marker='o', \
label='Line through specific coordinates', linewidth=3.0, alpha=1.0)
    # наша пряма(ламана)
    plt.show()

if __name__ == "__main__":
    from pathfinding import find_shortest_path, read_graph
    path = transform_tuples_to_lists(find_shortest_path(read_graph('graph.csv'), 1, (0, 0), (9, 9)))
    vizualize('graph.csv', path)
