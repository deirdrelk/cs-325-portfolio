from sys import maxsize


def solve_tsp(G):
    num_vertices = len(G)
    # starting here
    source = 0
    # returning this
    vertices = []
    # looping through the options at each node
    while num_vertices > 0:
        # making a minimum weight that would be impossible as a baseline
        min_weight = maxsize
        # pick the minimum value in the array and add it to the ver:
        for i in range(1, len(G)):
            if G[i][source] < min_weight and i != source and i not in vertices and G[i][source] != 0:
                node = i
                min_weight = G[i][source]
        vertices.append(source)
        source = node
        num_vertices -= 1
    vertices.append(0)
    return vertices


if __name__ == '__main__':
    Puzzle = [
        [0, 5, 3, 0, 1],
        [5, 0, 9, 8, 2],
        [3, 9, 0, 7, 0],
        [0, 8, 7, 0, 4],
        [1, 2, 0, 4, 0]
    ]

    print(solve_tsp(Puzzle))
