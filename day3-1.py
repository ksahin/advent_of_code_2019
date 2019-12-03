

grid = []
for a in range(5000):
    new = []
    for b in range(5000):
        new.append(['.', '.'])
    grid.append(new)


input_string1= "R75,D30,R83,U83,L12,D49,R71,U7,L72"
input_string2 = "U62,R66,U55,R34,D71,R55,D58,R83"

input1 = input_string1.split(',')
input2 = input_string2.split(',')

print(f'Grid x : {len(grid)} grid y: {len(grid[0])}')
def draw_path(grid, path, char_to_draw):
    starting_x = 2500
    starting_y = 2500

    current_x = starting_x
    current_y = starting_y
    index = 0 if char_to_draw == 'a' else 1

    for path_instruction in path:
        direction = path_instruction[0]
        number = int(path_instruction[1:])
        #print(f'Exeuting path instruction: {path_instruction}')
        if direction == 'R':
            for n in range(number):
                #print(f' current_x: {current_x} n: {n}')
                grid[current_x+1][current_y][index] = char_to_draw
                current_x += 1
        elif direction == 'L':
            for n in range(number):
                grid[current_x-1][current_y][index] = char_to_draw
                current_x -= 1
        elif direction == 'U':
            for n in range(number):
                grid[current_x][current_y+1][index] = char_to_draw
                current_y += 1
        elif direction == 'D':
            for n in range(number):
                grid[current_x][current_y-1][index] = char_to_draw
                current_y -= 1
        print(f'Current x: {current_x} Current_y: {current_y}')
    
    return grid
    
grid = draw_path(grid, input1, 'a')
grid = draw_path(grid, input2, 'b')

def manhatan_distance(i, j):
    return (i - 2500) + (j-2500)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j][0] =='a' and grid[i][j][1] == 'b':
            print(f'The two path cross at: x:{i} y:{j}')
            print('Manhattan distance: ' + str(manhatan_distance(i,j)))
