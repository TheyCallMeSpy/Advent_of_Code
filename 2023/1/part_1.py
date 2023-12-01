import re

def part2(line):
    LETTER_TO_NUMBER = [("one", "1"),("two", "2"),("three", "3"),("four", "4"),("five", "5"),("six", "6"),("seven", "7"),("eight", "8"),("nine", "9")]
    return line

def part1(line):
    line_digit_only = re.findall("\d", line)
    line_digit_only = "".join(line_digit_only)
    if len(line_digit_only) == 1:
        line_digit_only = line_digit_only + line_digit_only
    else:
        line_digit_only = line_digit_only[0] + line_digit_only[-1]
    return int(line_digit_only)

def main():
    sum = 0

    data = open("2023\\1\\input.txt", "r")
    for line in data:
        line = part2(line)
        sum += part1(line)
    print(sum)

if __name__ == "__main__":
    main()