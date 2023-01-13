def solution(src, dest):
    return solution2(src // 8, src % 8, dest // 8, dest % 8, 0)

def solution2(src_x, src_y, dest_x, dest_y, count):
    offsets = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    Q = list()

    explored = dict()
    explored[(src_x, src_y)] = 0

    count = 1

    v = (src_x, src_y)
    Q.append(v)

    while len(Q) != 0:
        u = Q.pop(0)
        print(u)

        if u[0] == dest_x and u[1] == dest_y:
            print("final:", Q, count)
            return count
        
        for offset in offsets:
            potential_coord = (src_x + offset[0], src_y + offset[1])
            if potential_coord[0] > 0 and potential_coord[0] < 63 and potential_coord[1] > 0 and potential_coord[1] < 63:
                if potential_coord not in explored:
                    v = potential_coord
                    Q.append(v)
                    explored[potential_coord] = count

        count += 1
# class Node:
#     def __init__(self, x, y, dist=0):
#         self.x = x
#         self.y = y
#         self.dist = dist
#         explored = False

offset = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

solution(28, 13)