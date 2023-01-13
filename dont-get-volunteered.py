def solution(src, dest):
    return BFS(src // 8, src % 8, dest // 8, dest % 8)

class Square:
    def __init__(self, x, y, dist=0):
        self.dist = dist
        self.x = x
        self.y = y

def BFS(src_x, src_y, dest_x, dest_y):
    offsets = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    visited_squares = set()

    q = list()
    # root node
    q.append(Square(src_x, src_y))

    dest = Square(dest_x, dest_y)

    while len(q) != 0:
        square = q.pop(0)

        dist = square.dist

        if square.x == dest.x and square.y == dest.y:
            return dist

        if square not in visited_squares:
            # mark as visited
            visited_squares.add(square)
            for offset in offsets:
                potential = (square.x + offset[0], square.y + offset[1])
                # if in valid bounds
                if (potential[0] >= 0 and potential[0] < 8 and potential[1] >= 0 and potential[1] < 8):
                    q.append(Square(potential[0], potential[1], dist + 1))
    # according to "knight's tour" problem, 64 is unachievable for shortest path
    return 64