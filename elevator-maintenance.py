def solution(manuals):
    # lambda expressions are really rad, but also hard to relearn every time
    manuals.sort(key=lambda m: [int(num) for num in m.split('.')])
    return manuals
