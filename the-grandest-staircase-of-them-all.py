def solution(n):        # https://web.archive.org/web/20090220004749/http:/www.site.uottawa.ca/~ivan/F49-int-part.pdf
    solutions = []
    solutions.append([n])
    x = [1] * n 
    solutions.append(x[0:len(x)])   # weird pass by reference behavior
    x[0] = n
    m = 1   # number of parts
    h = 1   # index of last part > 1
    while x[0] != 1:
        print(1, x)
        if x[h] == 2:
            m = m + 1
            x[h] = 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
            h = h - 1
        else:
            r = x[h] - 1
            t = m - h + 1
            x[h] = r
            while t >= r:
                h = h + 1
                print(x, h)
                x[h] = r
                t = t - r
            if t == 0:
                m = h
            else:
                m = h + 1
                if t > 1:
                    h = h + 1
                    x[h] = t
            solutions.append(x[0:len(x)])
        print(2, x)
    return solutions

# pretty close, look at the x[-1] and x[0], wtf is that notation? # https://web.archive.org/web/20090220004749/http:/www.site.uottawa.ca/~ivan/F49-int-part.pdf
def solution2(n):
    solutions = []
    x = [1] * n
    solutions.append(x[0:n])
    x[-1] = -1
    x[0] = 2
    h = 1
    m = n - 1
    solutions.append(x[0:m])

    ctr = 0

    while x[0] != n:
        if (m - h) > 1:
            h = h + 1
            x[h] = 2
            m = m - 1
        else:
            j = m - 2
            while x[j] == x[m - 1]:
                x[j] = 1
                j -= 1
            h = j + 1
            x[h] = x[m - 1] + 1
            r = x[m] + x[m - 1] * (m - h - 1)
            x[m] = 1
            if m - h > 1:
                x[m - 1] = 1
            m = h + r - 1
            
        solutions.append(x[0:m])
        ctr += 1
    return solutions

def all_unique_partitions(n):
    solutions = []

    p = [0] * n
    k = 0
    p[k] = n

    solutions.append(p[0:n])

    while True:

        # find rightmost value != 1
        rem_val = 0
        while k >= 0 and p[k] == 1:
            rem_val += p[k]
            k -= 1

        if k < 0:
            return solutions

        p[k] -= 1
        rem_val += 1

        while p[k] < rem_val:
            p[k + 1] = p[k]
            rem_val -= p[k]
            k += 1

        p[k + 1] = rem_val
        k += 1

        solutions.append(p[0:k + 1])
        print(p[0:k + 1])

print(solution3(5))