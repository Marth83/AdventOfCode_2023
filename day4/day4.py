def sol1():
    result = 0
    with open('day4/day4.txt') as f:
        for line in f.readlines():
            winning_numbers, our_ticket = [item.strip().split() for item in line.split(':')[1].split('|')]
            current = 0
            for item in our_ticket:
                if item in winning_numbers:
                    current = 1 if current == 0 else current * 2
            result += current
    return result

print(sol1())

def sol2():
    with open('day4/day4.txt') as f:
        lines = f.readlines()
        result = [1] * len(lines)
        for index, line in enumerate(lines):
            winning_numbers, our_ticket = [item.strip().split() for item in line.split(':')[1].split('|')]
            matches = sum(item in winning_numbers for item in our_ticket)
            for j in range(1, matches + 1):
                result[index + j] += result[index]
    return sum(result)

print(sol2())