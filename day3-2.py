





input_string1= "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
input_string2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"

input1 = input_string1.split(',')
input2 = input_string2.split(',')

def draw_path(path, char_to_draw):
    grid = []
    current_x = 0
    current_y = 0

    for path_instruction in path:
        direction = path_instruction[0]
        number = int(path_instruction[1:])
        if direction == 'R':
            for n in range(number):
                grid.append((current_x+1,current_y ))
                current_x += 1
        elif direction == 'L':
            for n in range(number):
                grid.append((current_x-1, current_y))
                current_x -= 1
        elif direction == 'U':
            for n in range(number):
                grid.append((current_x, current_y+1))
                current_y += 1
        elif direction == 'D':
            for n in range(number):
                grid.append((current_x, current_y-1))
                current_y -= 1
    
    return grid
    
grid1 = draw_path(input1, 'a')
grid2 = draw_path(input2, 'b')

matches = list(set(grid1) & set(grid2))

def manhatan_distance(i, j):
    return abs(i) + abs(j)


distances = []
for coordinates in matches:
    distances.append(manhatan_distance(coordinates[0], coordinates[1]))
#
sum_path = []
step1=0
step2=0

for intersection in matches:
    
    for index1, coor1 in enumerate(grid1):
        if coor1 == intersection:
            #import pdb; pdb.set_trace()
            step1 = index1
            break
    for index2, coor2 in enumerate(grid2):
        if coor2 == intersection:
            step2 = index2
            break
    sum_path.append(step1+step2)

print(min(sum_path)+2)








