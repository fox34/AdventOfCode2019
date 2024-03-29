#!/usr/bin/env python3

input1 = "R1009,U286,L371,U985,R372,D887,R311,U609,L180,D986,L901,D592,R298,U955,R681,D68,R453,U654,L898,U498,R365,D863,L974,U333,L267,D230,R706,D67,L814,D280,R931,D539,R217,U384,L314,D162,L280,U484,L915,D512,L974,D220,R292,U465,L976,U837,R28,U68,L98,D177,L780,U732,R696,D412,L715,U993,L617,U999,R304,D277,R889,D604,R199,U498,R302,U958,R443,U957,R453,U362,R704,U301,R813,U404,L150,D673,L407,D233,L901,D965,R602,U615,R496,U467,R849,U530,L205,D43,R709,U127,L35,U801,L565,D890,R90,D763,R95,D542,R84,D421,L298,D58,R794,U722,R205,U830,L149,D759,L950,D708,L727,U401,L187,D598,L390,D469,R375,U985,L723,U63,L983,D39,L160,U276,R822,D504,L298,D484,L425,U228,L984,D623,L936,U624,L851,D748,L266,D576,L898,U783,L374,D276,R757,U89,L649,U73,L447,D11,L539,U291,L507,U208,R167,D874,L596,D235,R334,U328,R41,D212,L544,D72,L972,D790,L282,U662,R452,U892,L830,D86,L252,U701,L215,U179,L480,U963,L897,U489,R223,U757,R804,U373,R844,D518,R145,U304,L24,D988,R605,D644,R415,U34,L889,D827,R854,U836,R837,D334,L664,D883,L900,U448,R152,U473,R243,D147,L711,U642,R757,U272,R192,U741,L522,U785,L872,D128,L161,D347,L967,D295,R831,U535,R329,D752,R720,D806,R897,D320,R391,D737,L719,U652,L54,D271,L855,D112,R382,U959,R909,D687,L699,U892,L96,D537,L365,D182,R886,U566,R929,U532,L255,U823,R833,U542,R234,D339,R409,U100,L466,U572,L162,U843,L635,D153,L704,D317,L534,U205,R611,D672,L462,D506,L243,U509,L819,D787,R448,D353,R162,U108,R850,D919,R259,U877,R50,D733,L875,U106,L890,D275,L904,U849,L855,U314,L291,U170,L627,U608,R783,U404,R294"
input2 = "L1010,D347,R554,U465,L30,D816,R891,D778,R184,U253,R694,U346,L743,D298,L956,U703,R528,D16,L404,D818,L640,D50,R534,D99,L555,U974,L779,D774,L690,U19,R973,D588,L631,U35,L410,D332,L74,D858,R213,U889,R977,U803,L624,U627,R601,U499,L213,U692,L234,U401,L894,U733,R414,D431,R712,D284,R965,D624,R848,D17,R86,D285,R502,U516,L709,U343,L558,D615,L150,D590,R113,D887,R469,U584,L434,D9,L994,D704,R740,D541,R95,U219,L634,D184,R714,U81,L426,D437,R927,U232,L361,D756,R685,D206,R116,U844,R807,U811,L382,D338,L660,D997,L551,D294,L895,D208,R37,D90,R44,D131,R77,U883,R449,D24,R441,U659,R826,U259,R98,D548,R118,D470,L259,U170,R518,U731,L287,U191,L45,D672,L691,U117,R156,U308,R230,U112,L938,U644,R911,U110,L1,U162,R943,U433,R98,U610,R428,U231,R35,U590,R554,U612,R191,U261,R793,U3,R507,U632,L571,D535,R30,U281,L613,U199,R168,D948,R486,U913,R534,U131,R974,U399,L525,D174,L595,D567,L394,D969,L779,U346,L969,D943,L845,D727,R128,U241,L616,U117,R791,D419,L913,D949,R628,D738,R776,D294,L175,D708,R568,U484,R589,D930,L416,D114,L823,U16,R260,U450,R534,D94,R695,D982,R186,D422,L789,D886,L761,U30,R182,U930,L483,U863,L318,U343,L380,U650,R542,U92,L339,D390,L55,U343,L641,D556,R616,U936,R118,D997,R936,D979,L594,U326,L975,U52,L89,U679,L91,D969,R878,D798,R193,D858,R95,D989,R389,U960,R106,D564,R48,D151,L121,D241,L369,D476,L24,D229,R601,U849,L632,U894,R27,U200,L698,U788,L330,D73,R405,D526,L154,U942,L504,D579,L815,D643,L81,U172,R879,U28,R715,U367,L366,D964,R16,D415,L501,D176,R641,U523,L979,D556,R831"

input1 = input1.split(",")
input2 = input2.split(",")

def calculate_coordinates(route):
    x = 0
    y = 0
    steps = 0 # Teil 2
    
    coordinates = [(x,y,steps)]
    
    for instruction in route:
        dir = instruction[0]
        len = int(instruction[1:])
        steps += len
        
        if dir == "U":
            y += len
        elif dir == "D":
            y -= len
        elif (dir == "L"):
            x -= len
        elif (dir == "R"):
            x+= len
        else:
            raise Exception("Invalid direction!")
        
        coordinates.append((x,y,steps))
    
    return coordinates


def calculate_lines(coordinates):
    
    # [(x1,y1,steps1),(x2,y2,steps2)],...
    lines = []
    
    for coordinate in range(1, len(coordinates)):
        pos1 = coordinates[coordinate-1]
        pos2 = coordinates[coordinate]
        lines.append([pos1, pos2])
    
    return lines


# Finde Schnittpunkt zweier abgeschlossenen Linien
def find_intersection(line1, line2):
    
    # 1. Geradenschnittpunkt
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    xintersect = det(d, xdiff) / div
    yintersect = det(d, ydiff) / div
    
    # 2. Abgeschlossene Linien
    # Alles in positiven Raum verschieben für einfacheres Rechnen
    xintersect_pos = xintersect + 100000
    yintersect_pos = yintersect + 100000
    x11 = line1[0][0] + 100000
    y11 = line1[0][1] + 100000
    x12 = line1[1][0] + 100000
    y12 = line1[1][1] + 100000
    
    x21 = line2[0][0] + 100000
    y21 = line2[0][1] + 100000
    x22 = line2[1][0] + 100000
    y22 = line2[1][1] + 100000
    
    # Erste Position ist immer die kleinere
    if x11 > x12:
        x11, x12 = x12, x11
    if y11 > y12:
        y11, y12 = y12, y11
    if x21 > x22:
        x21, x22 = x22, x21
    if y21 > y22:
        y21, y22 = y22, y21
    
    # Überschneidung liegt außerhalb des fest abgeschlossenen Linienbereichs
    if not x11 <= xintersect_pos <= x12 or not y11 <= yintersect_pos <= y12 or not x21 <= xintersect_pos <= x22 or not y21 <= yintersect_pos <= y22:
        raise Exception('intersection out of bounds')
    
    # Anzahl nötiger Schritte beider Teilstücke (Teil 2)
    steps1 = line1[0][2] + abs(line1[0][0] - xintersect) + abs(line1[0][1] - yintersect)
    steps2 = line2[0][2] + abs(line2[0][0] - xintersect) + abs(line2[0][1] - yintersect)
    
    return xintersect, yintersect, steps1+steps2

# Alle Überschneidungen für zwei Linienpaare suchen
def calculate_intersections(lines1, lines2):
    intersections = []
    for line1 in lines1:
        for line2 in lines2:
            try:
                intersection = find_intersection(line1, line2)
                intersections.append(intersection)
            except Exception:
                pass
    
    return intersections

# Abstand zur Mitte
def calculate_distance(pos):
    return abs(pos[0]) + abs(pos[1])


coord1 = calculate_coordinates(input1)
lines1 = calculate_lines(coord1)
#print(lines1)

coord2 = calculate_coordinates(input2)
lines2 = calculate_lines(coord2)
#print(lines2)


intersections = calculate_intersections(lines1, lines2)
min_distance = 999999
min_steps = 999999
for intersect in intersections:
    # Mittelpunkt ignorieren
    if intersect[0] == 0 and intersect[1] == 0:
        continue
    
    distance = calculate_distance(intersect)
    print(intersect, "Distance", distance)
    if distance < min_distance:
        min_distance = distance
    
    if (intersect[2] < min_steps):
        min_steps = intersect[2]

print()
print("Kleinste Distanz", min_distance) # Teil 1
print("Kleinste Anzahl Schritte", min_steps) # Teil 2


