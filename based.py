import math
import string
import copy


class ConversionFunctions:
    def __init__(self):
        self.alpha_num = list(string.digits) + list(string.ascii_uppercase)

    def dec_to_any(self, dec_num, base):
        int_part = int(dec_num)
        float_part = dec_num % 1
        converted_int = []
        converted_float = []
        alpha_num = copy.deepcopy(self.alpha_num)

        while int_part > 0:
            converted_int.insert(0, int_part % base)
            int_part //= base

        while float_part > 0 and len(converted_float) < 17:
            conversion_step = float_part * base
            converted_float.append(int(conversion_step))
            float_part = conversion_step - (int(conversion_step))

        # converted numbers will be precise to 15 decimal points, rounded based on the 16th one
        # this isn't ideal but the program will go into a death loop otherwise
        # can you call them DECIMAL points if it's not in decimal base? Hmm...

        try:
            temp = str(converted_float[15])

            if alpha_num.index(temp) >= math.ceil(base / 2):  # 0 1 2 3 4 5 6 7 8 9
                converted_float[14] = int(alpha_num[alpha_num.index(str(converted_float[14])) + 1])
            converted_float.pop(15)
        except IndexError:
            pass

        if base <= 37:
            for num in range(0, len(converted_int)):
                if converted_int[num] > 9:
                    converted_int[num] = alpha_num[converted_int[num]]

            for num in range(0, len(converted_float)):
                if converted_float[num] > 9:
                    converted_float[num] = alpha_num[converted_float[num]]

            if len(converted_float):
                converted_int.append('.')
            return "".join([str(x) for x in converted_int + converted_float])
        else:
            return " ".join([str(x) for x in converted_int + converted_float])

    def any_to_dec_v1(self, base, num):  # converts to decimal with digits past 9 notated with letters
        digits = list(num)
        alpha_num = copy.deepcopy(self.alpha_num)
        available_chars = alpha_num[:base]

        for digit in digits:
            if digit.upper() not in available_chars:
                return 'Error: Number uses a character not available in given base. Please try again.'

        for index in range(0, len(digits)):
            if digits[index] in string.ascii_letters:
                digits[index] = alpha_num.index(digits[index].upper())
            else:
                digits[index] = alpha_num.index(digits[index])
        digits.reverse()
        dec_num = 0
        for num in range(0, len(digits)):
            dec_num += digits[num] * (base ** num)
        return dec_num

    @staticmethod  # this isn't really necessary, but IDEs are annoying sometimes
    def any_to_dec_v2(base, num):  # user input consists of decimal numbers separated by spaces
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
