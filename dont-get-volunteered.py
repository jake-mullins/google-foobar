final = 0

# #def move(src_x, src_y, dest_x, dest_y, count):
#     # print((src_x, src_y), (dest_x, dest_y), count)
# 
#     if count > 20:
#         return
# 
#     # base case
#     if src_x == dest_x and src_y == dest_y:
#         final = count
#         print("YALLAH ", final)
# 
#     offsets = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, 1), (2, -1)]
# 
#     for offset in offsets:
#         # if within range
#         if src_x + offset[0] > 0 and src_x + offset[0] < 63 and src_y + offset[1] > 0 and src_y + offset[1] < 63:
#             move(src_x + offset[0], src_y + offset[1], dest_x, dest_y, count + 1)
#             
print(solution(27, 21))