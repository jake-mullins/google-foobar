# Here are some dead ends because I've never heard the term "Dynamic programming".
# https://web.archive.org/web/20090220004749/http:/www.site.uottawa.ca/~ivan/F49-int-part.pdf
# https://jeromekelleher.net/generating-integer-partitions.html

# probably could do caching, haven't learned that yet + sys import is illegal
def solution(n):
    global lookup 
    lookup = [[-1 for j in range(n + 1)] for i in range(n + 2)]

    return evaluate_stair(1, n) - 1

def evaluate_stair(height, left):
    global lookup

    if lookup[height][left] != -1:
        return lookup[height][left]

    # All bricks will be consumed
    # save literally a single recursive call at the end of a search tree by evaluating if it would return true before the right hand search begins.
    # I tried to benchmark this using time command, but it ran so fast that any changes were up to CPU Scheduling. Good problems to have.
    if left == 0:
        return 1

    # Not enough bricks to complete a row, thus an invalid result.
    if left < height:
        return 0

    # Left case is increasing the height of that step.
    # Right case is "placing" that stair, subtracting that height from total amount, moving on to the next step.
    lookup_res = evaluate_stair(height + 1, left) + evaluate_stair(height + 1, left - height)
    
    # save data
    lookup[height][left] = lookup_res

    return lookup_res