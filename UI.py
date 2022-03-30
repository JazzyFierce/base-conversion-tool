import math
from based import ConversionFunctions


class UI:
    def __init__(self):
        self.options = ['Convert from decimal base', 'Convert from non-decimal base', 'Convert common constants',
                        'Exit']
        self.conversion_options = ['Convert to common bases (binary, octal, hex)', 'Convert to custom base',
                                   'Back']
        self._common_bases = {'Binary': 2, 'Octal': 8, 'Hex': 16}
        self._common_constants = {'Pi': math.pi, 'Tau': math.tau, "Euler's Constant": math.e,
                                  "Golden Ratio": (1 + 5 ** 0.5) / 2}
        self.converter = ConversionFunctions()

    def selection(self, option):
        match option:
            case '1':
                while True:
                    print('\nWhich base(s) would you like to convert to?')
                    for num, choice in enumerate(self.conversion_options):
                        print(f'{num + 1}){choice}')
                    base_choice = input('Enter choice: ')

                    match int(base_choice):
                        case 1:
                            while True:
                                try:
                                    num_to_convert = float(input('Enter the decimal number to convert: '))
                                    print(f'Decimal number: {num_to_convert}')
                                    for base_name, base in self._common_bases.items():
                                        print(f'{base_name}: {self.converter.dec_to_any(num_to_convert, base)}')
                                    break
                                except ValueError:
                                    continue
                            break
                        case 2:
                            while True:
                                try:
                                    num_to_convert = float(input('Enter the decimal number to convert: '))
                                    custom = int(input('Enter your base (decimal format): '))
                                    print(f'Decimal number: {num_to_convert}')
                                    print(f'Base {custom} number: {self.converter.dec_to_any(num_to_convert, custom)}')
                                    break
                                except ValueError:
                                    continue
                            break
                        case 3:
                            return
                        case _:
                            print('Please enter a valid choice')
                            continue
            case '2':
                while True:
                    base = int(input('\nWhat base would you like to convert from?: '))
                    print('How is your non-decimal number notated?\n1) With alpha-numerics\n2) With spaces\n3) Back')
                    notation = input('Your choice: ')
                    match notation:
                        case '1':
                            num_to_convert = input('Enter number to convert: ')
                            print(f'Base {base} number: {num_to_convert}')
                            print(f'Decimal: {self.converter.any_to_dec_v1(base, num_to_convert)}')
                            break
                        case '2':
                            num_to_convert = input('Enter number to convert: ')
                            print(f'Base {base} number: {num_to_convert}')
                            print(f'Decimal: {self.converter.any_to_dec_v2(base, num_to_convert)}')
                            break
                        case '3':
                            return
                        case _:
                            print('Please enter a valid option.')

            case '3':
                base_choice = int(input('What base would you like to convert to?: '))
                for name, constant in self._common_constants.items():
                    print(f'{name} {self.converter.dec_to_any(constant, base_choice)}')
                return

            case '4':
                exit()
            case _:
                return 'Please select a valid option'

    def run(self):
        print("Base Conversion Tool v1 by Isabel Loney")
        while True:
            print('\nWhat would you like to do?')
            for num, choice in enumerate(self.options):
                print(f'{num + 1}) {choice}')
            option = input("\nYour Choice: ")
            self.selection(option)
