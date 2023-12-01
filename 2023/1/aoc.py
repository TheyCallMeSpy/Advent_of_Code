def first_last_digit_and_word_to_digit(line):
    WORD = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    number_list = []
    for line_i in range(len(line)):
        if line[line_i].isdigit():
            number_list.append(line[line_i])
        else:
            for word_i in WORD:
                x = 0
                count = 0
                for letter in word_i:
                    try:
                        if letter == line[line_i+count]:
                            x += 1
                        count += 1
                    except:
                        pass
                if len(word_i) == x:
                    number_list.append(str(WORD.index(word_i)+1))
                    
    return int(number_list[0]+number_list[-1])

def main():
    sum = 0

    data = open("2023\\1\\input.txt", "r")
    for line in data:
        sum += first_last_digit_and_word_to_digit(line)
    print(sum)

if __name__ == "__main__":
    main()