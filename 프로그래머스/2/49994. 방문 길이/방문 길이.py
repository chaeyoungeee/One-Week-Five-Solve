def move(dir, x, y):
    if dir == 'U': return x, y+1
    if dir == 'D': return x, y-1
    if dir == 'R': return x+1, y
    if dir == 'L': return x-1, y
    return x, y

def solution(dirs):
    l = 0
    x, y = 5, 5
    dirs = list(dirs)
    ways = set()
    
    for dir in dirs:
        dx, dy = move(dir, x, y)
        if 0 <= dx < 11 and 0 <= dy < 11:
            if ((x,y), (dx, dy)) not in ways:
                l += 1
            ways.add(((x,y), (dx, dy)))
            ways.add(((dx,dy), (x, y)))
            x, y = dx, dy
    return l