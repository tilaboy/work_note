def c_digits(new_digit, curr_digits):
    return curr_digits + new_digit

total_number = int(input())

for i in range(total_number):
    d1 = ''
    d2 = ''

    for digit in input():
        if digit == '4':
            d1 = c_digits('1', d1)
            d2 = c_digits('3', d2)
        elif digit == '0':
            d1 = c_digits('0', d1)
            d2 = c_digits('0', d2)
        elif digit == '5':
            d1 = c_digits('3', d1)
            d2 = c_digits('2', d2)
        else:
            orig_d = int(digit)
            d1 = c_digits('1', d1)
            d2 = c_digits(str(orig_d - 1), d2)

    if d1 == '':
        d1 = 0
    if d2 == '':
        d2 =0

    print("Case #{}: {} {}".format(i+1, int(d1), int(d2)))
