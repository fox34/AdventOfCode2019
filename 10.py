#!/usr/bin/env python3

import math, operator

puzzle_input = """.#....#.###.........#..##.###.#.....##...
...........##.......#.#...#...#..#....#..
...#....##..##.......#..........###..#...
....#....####......#..#.#........#.......
...............##..#....#...##..#...#..#.
..#....#....#..#.....#.#......#..#...#...
.....#.#....#.#...##.........#...#.......
#...##.#.#...#.......#....#........#.....
....##........#....#..........#.......#..
..##..........##.....#....#.........#....
...#..##......#..#.#.#...#...............
..#.##.........#...#.#.....#........#....
#.#.#.#......#.#...##...#.........##....#
.#....#..#.....#.#......##.##...#.......#
..#..##.....#..#.........#...##.....#..#.
##.#...#.#.#.#.#.#.........#..#...#.##...
.#.....#......##..#.#..#....#....#####...
........#...##...#.....#.......#....#.#.#
#......#..#..#.#.#....##..#......###.....
............#..#.#.#....#.....##..#......
...#.#.....#..#.......#..#.#............#
.#.#.....#..##.....#..#..............#...
.#.#....##.....#......##..#...#......#...
.......#..........#.###....#.#...##.#....
.....##.#..#.....#.#.#......#...##..#.#..
.#....#...#.#.#.......##.#.........#.#...
##.........#............#.#......#....#..
.#......#.............#.#......#.........
.......#...##........#...##......#....#..
#..#.....#.#...##.#.#......##...#.#..#...
#....##...#.#........#..........##.......
..#.#.....#.....###.#..#.........#......#
......##.#...#.#..#..#.##..............#.
.......##.#..#.#.............#..#.#......
...#....##.##..#..#..#.....#...##.#......
#....#..#.#....#...###...#.#.......#.....
.#..#...#......##.#..#..#........#....#..
..#.##.#...#......###.....#.#........##..
#.##.###.........#...##.....#..#....#.#..
..........#...#..##..#..##....#.........#
..#..#....###..........##..#...#...#..#.."""


asteroid_coords = []
rows = puzzle_input.split("\n")

# Karte aller Asteroiden aufstellen
for row_index, row in enumerate(rows):
    for col_index, col in enumerate(list(row)):
        if col == "#":
            asteroid_coords.append((col_index, row_index))




# Teil 1

# Punkt zwischen zwei anderen, zweidimensional
def is_between_2d(x1, x2, between):
    return x1 <= between <= x2 or x2 <= between <= x1

# Drei Punkte auf einer Linie, 3d
def collinear(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) == (p3[0] - p1[0]) * (p2[1] - p1[1])

# Definierter Punkt innerhalb der Linie von p1 nach p2
def point_is_inbetween(p1, p2, candidate):
    if not collinear(p1, p2, candidate):
        return False
    
    if p1[0] != p2[0]:
        return is_between_2d(p1[0], candidate[0], p2[0])
    else:
        return is_between_2d(p1[1], candidate[1], p2[1])
    


# Für jeden Asteroiden sichtbare andere prüfen
def get_point_with_max_visibility():
    num_visible_max = 0
    best_asteroid = False
    for asteroid in asteroid_coords:
        num_visible = 0
        for other_asteroid in asteroid_coords:
            if other_asteroid == asteroid:
                continue
        
            has_asteroid_inbetween = False
            for asteroid_inbetween in asteroid_coords:
                if asteroid_inbetween == asteroid or asteroid_inbetween == other_asteroid:
                    continue
            
                if point_is_inbetween(asteroid, other_asteroid, asteroid_inbetween):
                    has_asteroid_inbetween = True
                    break
            
            if not has_asteroid_inbetween:
                num_visible += 1
        
        #print(asteroid, num_visible)
    
        # Dieser hat bislang beste Sicht
        if num_visible > num_visible_max:
            best_asteroid = asteroid
            num_visible_max = num_visible
    
    return best_asteroid, num_visible_max

# (28,29) mit 340 sichtbaren
#best_asteroid, num_visible_max = get_point_with_max_visibility()
#print("Bester Asteroid ist", best_asteroid, "mit", num_visible_max, "sichtbaren Asteroiden")




# Teil 2
best_asteroid = (28,29)
num_visible_max = 340

# Bei welchem Winkel wird p2 von p1 getroffen, ausgehend von vertikalem Start nach oben
def get_angle(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    d_x = x2 - x1
    d_y = y2 - y1
    rads = math.atan2(d_x, -d_y)
    degs = math.degrees(rads)
    if degs < 0:
        degs = 360 + degs
    return degs

# Radius und Winkel von base zu point
def get_relative_polar(base, point):
    r = ((point[0] - base[0])**2 + (point[1] - base[1])**2)**0.5
    angle = get_angle(base, point)
    return (r, angle, point)


def vaporize(base, surrounding):
    # Umrechnung zu Radius+Winkel
    polar_points = []
    for point in surrounding:
        polar_points.append(get_relative_polar(base, point))
    
    # Sortiere nach Winkel, dann Entfernung
    polar_points.sort(key=operator.itemgetter(1, 0), reverse = True)
    
    # Entferne Punkte, einen Punkt pro Winkel pro Durchgang
    removed_counter = 0
    i = len(polar_points) - 1
    laser_angle = -1
    while removed_counter < 200:
        current_r, current_angle, _ = polar_points[i]
        
        # Entferne
        if current_angle != laser_angle or len(polar_points) <= 1:
            last_removed_point = polar_points.pop(i)
            removed_counter += 1
        
        laser_angle = current_angle
        i -= 1
        
        # Nächster Durchlauf von hinten
        if i < 0:
            i = len(polar_points) - 1
        
    print(removed_counter)
    return last_removed_point[2][0]*100 + last_removed_point[2][1]
    

surrounding = asteroid_coords[:]
surrounding.remove(best_asteroid)
# 2628
print(vaporize(best_asteroid, surrounding))
