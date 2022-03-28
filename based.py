import string

alpha_num = list(string.digits) + list(string.ascii_uppercase)


def dec_to_any(dec_num, base):  # need a if/catch case for bases above 37
    int_part = int(dec_num)
    float_part = dec_num % 1
    converted_int = []
    converted_float = []

    while int_part:
        converted_int.insert(0, int_part % base)
        int_part //= base

    while float_part > 0:
        conversion_step = float_part * base
        converted_float.append(int(conversion_step))
        float_part = conversion_step - (int(conversion_step))

    try:
        for num in range(0, len(converted_int)):
            if converted_int[num] > 9:
                converted_int[num] = alpha_num[converted_int[num]]

        for num in range(0, len(converted_float)):
            if converted_float[num] > 9:
                converted_float[num] = alpha_num[converted_float[num]]

        if len(converted_float):
            converted_int.append('.')
        return "".join([str(x) for x in converted_int + converted_float])
    except IndexError:
        return 'Sorry, this program currently does not support above base 37'


def any_to_dec_v1(base, num):  # converts to decimal with digits past 9 notated with letters
    digits = list(num)
    available_chars = alpha_num[0:base]

    for digit in digits:
        if digit.upper() not in available_chars:
            return 'Error: Number uses a character not available in given base. Please try again.'

    for index in range(0, len(digits)):
        if digit in string.ascii_letters:
            digits[index] = alpha_num.index(digits[index].upper())
        else:
            digits[index] = alpha_num.index(digits[index])
    digits.reverse()
    dec_num = 0
    for num in range(0, len(digits)):
        dec_num += digits[num] * (base ** num)
    return dec_num


def any_to_dec_v2(base, num):  # user input consists of decimal numbers separated by spaces
    # needs decimal pt option, but we are going to address that LATER
    digits = num.split()

    try:
        digits.reverse()
        digits = [int(x) for x in digits]

        dec_num = 0
        for num in range(0, len(digits)):
            dec_num += digits[num] * (base ** num)
        return dec_num
    except ValueError:
        return 'Error: invalid digit. Please note the program does not currently support fractional components for this option.'
