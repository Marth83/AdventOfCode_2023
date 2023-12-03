def is_symbol(char: str) -> bool:
    return not char.isalnum() and char != '.'

def check_if_number_is_valid(matrix, curr_index: tuple, total: int, curr: str, is_already_valid: bool) -> bool:
    # Check if having adjacent symbol
    rows, cols = len(matrix), len(matrix[0])
    if (
        curr_index[0]-1 >= 0 and curr_index[1]-1 >= 0 and is_symbol(matrix[curr_index[0]-1][curr_index[1]-1]) or
        curr_index[0]-1 >= 0 and is_symbol(matrix[curr_index[0]-1][curr_index[1]]) or
        curr_index[1]-1 >= 0 and is_symbol(matrix[curr_index[0]][curr_index[1]-1]) or
        curr_index[0]+1 < rows and is_symbol(matrix[curr_index[0]+1][curr_index[1]]) or
        curr_index[0]+1 < rows and curr_index[1]+1 < cols and is_symbol(matrix[curr_index[0]+1][curr_index[1]+1]) or
        curr_index[1]+1 < cols and is_symbol(matrix[curr_index[0]][curr_index[1]+1]) or
        curr_index[0]-1 >= 0 and curr_index[1]+1 < cols and is_symbol(matrix[curr_index[0]-1][curr_index[1]+1]) or
        curr_index[0]+1 < rows and curr_index[1]-1 >= 0 and is_symbol(matrix[curr_index[0]+1][curr_index[1]-1])
    ):
        is_already_valid = True
    if curr_index[1]+1 < cols and matrix[curr_index[0]][curr_index[1]+1].isdigit():
        curr += matrix[curr_index[0]][curr_index[1]]
        matrix[curr_index[0]][curr_index[1]] = '.'
        total = check_if_number_is_valid(matrix, (curr_index[0], curr_index[1]+1), total, curr, is_already_valid)
    elif is_already_valid:
        curr += matrix[curr_index[0]][curr_index[1]]
        total += int(curr)
        curr = ''
        matrix[curr_index[0]][curr_index[1]] = '.'
        is_already_valid = False
    return total

def sol1() -> int:
    """Solution to the 1st part of the challenge"""
    total = 0
    matrix = []
    with open("/Users/mcol/Documents/Code/AdventOfCode/day3/day3.txt", "r") as f:
        for line in f.readlines():
            matrix.append(list(line.strip()))
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j].isdigit():
                    total = check_if_number_is_valid(matrix, (i,j), total, '', False)

    return total

# print(sol1())

#############

def is_gear_symbol(char: str) -> bool:
    return char == '*'

def get_part_number(matrix, curr_index: tuple, curr: str) -> str:
        if curr_index[1]-1 >=0 and matrix[curr_index[0]][curr_index[1]-1].isdigit():
            return get_part_number(matrix, (curr_index[0], curr_index[1]-1), curr)

        curr += matrix[curr_index[0]][curr_index[1]]

        matrix[curr_index[0]][curr_index[1]] = '.'
        if curr_index[1]+1 < len(matrix[0]) and matrix[curr_index[0]][curr_index[1]+1].isdigit():
            curr = get_part_number(matrix, (curr_index[0], curr_index[1]+1), curr)
        return curr

def check_if_gear_is_valid(matrix, curr_index: tuple, total: int) -> bool:
    # Check for gear
    adjacent_part_number = []
    rows, cols = len(matrix), len(matrix[0])
    if curr_index[0]-1 >= 0 and curr_index[1]-1 >= 0 and matrix[curr_index[0]-1][curr_index[1]-1].isdigit():
        adjacent_part_number.append(int(get_part_number(matrix, (curr_index[0]-1, curr_index[1]-1), '')))                                                                   
    if curr_index[0]-1 >= 0 and matrix[curr_index[0]-1][curr_index[1]].isdigit():
        adjacent_part_number.append(int(get_part_number(matrix, (curr_index[0]-1, curr_index[1]), '')))
    if curr_index[1]-1 >= 0 and matrix[curr_index[0]][curr_index[1]-1].isdigit():
        adjacent_part_number.append(int(get_part_number(matrix, (curr_index[0], curr_index[1]-1), '')))
    if curr_index[0]+1 < rows and matrix[curr_index[0]+1][curr_index[1]].isdigit():
        adjacent_part_number.append(int(get_part_number(matrix, (curr_index[0]+1, curr_index[1]), '')))
    if curr_index[0]+1 < rows and curr_index[1]+1 < cols and matrix[curr_index[0]+1][curr_index[1]+1].isdigit():
        adjacent_part_number.append(int(get_part_number(matrix, (curr_index[0]+1, curr_index[1]+1), '')))
    if curr_index[1]+1 < cols and matrix[curr_index[0]][curr_index[1]+1].isdigit():
        adjacent_part_number.append(int(get_part_number(matrix, (curr_index[0], curr_index[1]+1), '')))
    if curr_index[0]-1 >= 0 and curr_index[1]+1 < cols and matrix[curr_index[0]-1][curr_index[1]+1].isdigit():
        adjacent_part_number.append(int(get_part_number(matrix, (curr_index[0]-1, curr_index[1]+1), '')))
    if curr_index[0]+1 < rows and curr_index[1]-1 >= 0 and matrix[curr_index[0]+1][curr_index[1]-1].isdigit():
        adjacent_part_number.append(int(get_part_number(matrix, (curr_index[0]+1, curr_index[1]-1), '')))
    
    if len(adjacent_part_number) == 2:
        print(adjacent_part_number)
        total += adjacent_part_number[0] * adjacent_part_number[1]
    return total

def sol2() -> int:
    """Solution to the 2nd part of the challenge"""
    total = 0
    matrix = []
    with open("/Users/mcol/Documents/Code/AdventOfCode/day3/day3.txt", "r") as f:
        for line in f.readlines():
            matrix.append(list(line.strip()))
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if is_gear_symbol(matrix[i][j]):
                    total = check_if_gear_is_valid(matrix, (i,j), total)

    return total

print(sol2())