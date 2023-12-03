def sol1() -> int:
    calibrationTotal = 0
    with open("day1.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            calibration = ''
            for start in line:
                if start.isdigit():
                    calibration += start
                    break
            line = line[::-1]
            for end in line:
                if end.isdigit():
                    calibration += end
                    break
            print(calibration)
            calibrationTotal += int(calibration)
    return calibrationTotal

# print(sol1())


def sol2() -> int:
    validStringNumber = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    calibrationTotal = 0
    with open("day1.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            print('--- ', line)
            calibration = ''
            for start in range(len(line)):

                if line[start].isdigit():
                    print(line[start])
                    calibration += line[start]
                    break
                
                if line[start:start+3] in validStringNumber:
                    print(line[start:start+3])
                    calibration += validStringNumber[line[start:start+3]]
                    break
                if line[start:start+4] in validStringNumber:
                    print(line[start:start+4])
                    calibration += validStringNumber[line[start:start+4]]
                    break
                if line[start:start+5] in validStringNumber:
                    print(line[start:start+5])
                    calibration += validStringNumber[line[start:start+5]]
                    break


            for start in range(len(line)-1, -1, -1):

                if line[start].isdigit():
                    print(line[start])
                    calibration += line[start]
                    break
        
                if line[start-3:start] in validStringNumber:
                    print(line[start-3:start])
                    calibration += validStringNumber[line[start-3:start]]
                    break
                if line[start-4:start] in validStringNumber:
                    print(line[start-4:start])
                    calibration += validStringNumber[line[start-4:start]]
                    break
                if line[start-5:start] in validStringNumber:
                    print(line[start-5:start])
                    calibration += validStringNumber[line[start-5:start]]
                    break

            print(calibration)
            calibrationTotal += int(calibration)
    return calibrationTotal

print(sol2())