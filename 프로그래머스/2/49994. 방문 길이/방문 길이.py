def solution(dirs):
    l = 0
    x, y = 5, 5
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    dirs = list(dirs)
    ways = set()
    
    for dir in dirs:
        dx, dy = d[dir]
        nx, ny = x+dx, y+dy
        if 0 <= nx < 11 and 0 <= ny < 11:
            if (x,y, nx, ny) not in ways:
                l += 1
            ways.add((x,y, nx, ny))
            ways.add((nx, ny, x, y))
            x, y = nx, ny
    return l