import math
import string


class ConversionFunctions:
    def __init__(self):
        # a set of available characters
        self.alpha_num = list(string.digits) + list(string.ascii_uppercase)

    def dec_to_any(self, dec_num, base):
        # the process for converting integers and fractional components is different, so we immediately separate them
        int_part = int(dec_num)
        float_part = dec_num % 1
        converted_int = []
        converted_float = []

        while int_part > 0:
            converted_int.insert(0, int_part % base)
            int_part //= base

        while float_part > 0 and len(converted_float) < 17:
            conversion_step = float_part * base
            converted_float.append(int(conversion_step))
            float_part = conversion_step - (int(conversion_step))

        # converted numbers will be precise to 15 digits for the fractional component
        # rounding will be based on the ceiling of base/2
        # i.e. anything larger than a half will be rounded up, which is pretty intuitive
        try:
            temp = converted_float[15]

            if temp >= math.ceil(base / 2):
                converted_float[14] += 1
            converted_float.pop(15)
        except IndexError:
            # this basically means 15 digits of precision isn't necessary; in that case, the exact number is printed
            pass

        if base <= 36:
            for num in range(0, len(converted_int)):
                if converted_int[num] > 9:
                    converted_int[num] = self.alpha_num[converted_int[num]]

            for num in range(0, len(converted_float)):
                if converted_float[num] > 9:
                    converted_float[num] = self.alpha_num[converted_float[num]]

            if len(converted_float):
                converted_int.append('.')
            return "".join([str(x) for x in converted_int + converted_float])
        else:
            if len(converted_float):
                converted_int.append(" . ")
            return " ".join([str(x) for x in converted_int + converted_float])

    def any_to_dec_v1(self, base, num):  # converts to decimal with digits past 9 notated with letters
        digits = list(num)
        available_chars = self.alpha_num[:base]

        for digit in digits:
            if digit.upper() not in available_chars:
                return 'Error: Number uses a character not available in given base. Please try again.'

        for index in range(0, len(digits)):
            if digits[index] in string.ascii_letters:
                digits[index] = self.alpha_num.index(digits[index].upper())
            else:
                digits[index] = self.alpha_num.index(digits[index])
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
