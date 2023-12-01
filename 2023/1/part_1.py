sum = 0

f = open("2023\\1\input.txt", "r")
for x in f:
    digit_only = filter(str.isdigit,x)
    digit_only = "".join(digit_only)
    if len(digit_only) == 1:
        digit_only = digit_only + digit_only
    else:
        digit_only = digit_only[0] + digit_only[len(digit_only)-1]
    sum += int(digit_only)
print(sum)
f.close()