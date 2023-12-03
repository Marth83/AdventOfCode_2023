def sol1() -> int:
    # with only 12 red cubes, 13 green cubes, and 14 blue cubes
    max_values = {
        'RED': 12,
        'GREEN': 13,
        'BLUE': 14,
    }
    idTotal = 0
    with open("/Users/mcol/Documents/Code/AdventOfCode/day2/day2.txt", "r") as f:
        for line in f.readlines():
            print('-------')
            gameMax = {
                'RED': 0,
                'GREEN': 0,
                'BLUE': 0,
            }
            gameId = line.split(' ')[1]

            sets = line.split(':')[1].split(';')
            for set in sets:
                set = set.strip()
                print(set)
                for item in set.split(','):
                    item = item.strip()
                    number, color_name = item.split()
                    if 'red' in color_name:
                        gameMax['RED'] = max(gameMax['RED'], int(number))
                    if 'green' in color_name:
                        gameMax['GREEN'] = max(gameMax['GREEN'], int(number))
                    if 'blue' in color_name:
                        gameMax['BLUE'] = max(gameMax['BLUE'], int(number))
        
            if gameMax['RED'] <= max_values['RED'] and gameMax['GREEN'] <= max_values['GREEN'] and gameMax['BLUE'] <= max_values['BLUE']:
                idTotal += int(gameId[:-1])

        return idTotal
            

print(sol1())

def sol2() -> int:
    powerTotal = 0
    with open("/Users/mcol/Documents/Code/AdventOfCode/day2/day2.txt", "r") as f:
        for line in f.readlines():
            print('-------')
            gameMax = {
                'RED': 0,
                'GREEN': 0,
                'BLUE': 0,
            }
            gameId = line.split(' ')[1]

            sets = line.split(':')[1].split(';')
            for set in sets:
                set = set.strip()
                print(set)
                for item in set.split(','):
                    item = item.strip()
                    number, color_name = item.split()
                    if 'red' in color_name:
                        gameMax['RED'] = max(gameMax['RED'], int(number))
                    if 'green' in color_name:
                        gameMax['GREEN'] = max(gameMax['GREEN'], int(number))
                    if 'blue' in color_name:
                        gameMax['BLUE'] = max(gameMax['BLUE'], int(number))
        
            powerTotal += gameMax['BLUE'] * gameMax['GREEN'] * gameMax['RED']

        return powerTotal
    
print(sol2())