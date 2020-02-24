import sys

class Node:
    def __init__(self, parent, position):
        self.position = position
        self.parent = parent
        # Distance between start and finish
        self.g = 0
        # Heuristic
        self.h = 0
        # Sum
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __str__(self):
        return f'{self.position} --> '


def astar(maze, start, finish):
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    finish_node = Node(None, finish)
    finish_node.g = finish_node.h = finish_node.f = 0

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while open_list is not None:
        # Go to the finish
        current_node = open_list[0]
        current_index = 0
        for i, node in enumerate(open_list):
            if node.f < current_node.f:
                current_node = node
                current_index = i

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == finish_node:
            path = []
            current = current_node
            # Go in reverse with parent and then reverse the list
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:  # Adjacent squares

            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                    len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue

            # if it's one then it's a wall
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            new_node = Node(current_node, node_position)
            children.append(new_node)

        for child in children:
            for closed_child in closed_list:
                if child == closed_child:
                    continue
            child.g = current_node.g + 1
            child.h = ((child.position[0] - finish_node.position[0]) ** 2) + (
                        (child.position[1] - finish_node.position[1]) ** 2)
            child.f = child.g + child.h
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list.append(child)


def fix(position):
    # Converts to tuple and checks validity
    if len(position) is 2:
        position = [int(i) for i in position]
        for i in position:
            if -1 < i < 10:
                position = tuple(position)
                return position


def main():
    grid = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

    start = []
    finish = []

    start.append(input('Enter the row of the start point: '))
    start.append(input('Enter the column of the start point: '))

    finish.append(input('Enter the row of the finish point: '))
    finish.append(input('Enter the column of the finish point: '))

    start = fix(start)
    finish = fix(finish)

    road = astar(grid, start, finish)

    for node in road:
        if node == road[-1]:
            print(f'{node}')
        else:
            print(f'{node} --> ', end='')


if __name__ == '__main__':
    main()
