import math
from based import dec_to_any
from based import any_to_dec_v1
from based import any_to_dec_v2

options = ['Convert from decimal base', 'Convert from non-decimal base', 'Convert common constants', 'Exit']
conversion_options = ['Convert to common bases (binary, octal, hex)', 'Convert to custom base',
                      'Back']
common_bases = {'Binary': 2, 'Octal': 8, 'Hex': 16}
common_constants = {'Pi': math.pi, 'Tau': math.tau, "Euler's Constant": math.e, "Golden Ratio": (1 + 5 ** 0.5) / 2}


def selection(asdf):
    match int(asdf):
        case 1:
            while True:
                print('\nWhich base(s) would you like to convert to?')
                for num, choice in enumerate(conversion_options):
                    print(f'{num + 1}){choice}')
                base_choice = input('Enter choice: ')

                match int(base_choice):
                    case 1:
                        num_to_convert = float(input('Enter the decimal number to convert: '))
                        print(f'Decimal number: {num_to_convert}')
                        for base_name, base in common_bases.items():
                            print(f'{base_name}: {dec_to_any(num_to_convert, base)}')
                        break
                    case 2:
                        num_to_convert = float(input('Enter the decimal number to convert: '))
                        custom = int(input('Enter your base (decimal format): '))
                        print(f'Decimal number: {num_to_convert}')
                        print(f'Base {custom} number: {dec_to_any(num_to_convert, custom)}')
                        break
                    case 3:
                        return
                    case _:
                        print('Please enter a valid choice')
                        continue
        case 2:
            while True:
                base = int(input('\nWhat base would you like to convert from?: '))
                print('How is your non-decimal number notated?\n1) With alpha-numerics\n2) With spaces\n3) Back')
                notation = input('Your choice: ')
                match notation:
                    case '1':
                        num_to_convert = input('Enter number to convert: ')
                        print(f'Base {base} number: {num_to_convert}')
                        print(f'Decimal: {any_to_dec_v1(base, num_to_convert)}')
                        break
                    case '2':
                        num_to_convert = input('Enter number to convert: ')
                        print(f'Base {base} number: {num_to_convert}')
                        print(f'Decimal: {any_to_dec_v2(base, num_to_convert)}')
                        break
                    case '3':
                        return
                    case _:
                        print('Please enter a valid option.')

        case 3:
            base_choice = int(input('What base would you like to convert to?: '))
            for name, constant in common_constants.items():
                print(f'{name} {constant} {dec_to_any(constant, base_choice)}')
            return

        case 4:
            exit()
        case _:
            return 'Please select a valid option'


def run():
    print("Base Conversion Tool v1 by Isabel Loney")
    while True:
        print('\nWhat would you like to do?')
        for num, choice in enumerate(options):
            print(f'{num + 1}) {choice}')
        option = input("\nYour Choice: ")
        selection(option)
