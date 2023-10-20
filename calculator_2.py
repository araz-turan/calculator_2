import math
def input_control_x():
    while True:
        input_1 = input('Enter a number: ')
        if input_1.isdigit():
            return int(input_1)
        elif input_1 == '-{}'.format(input_1):
            return '-{}'.format(input_1)
        else:
            try:
                input_1 = float(input_1)
                return input_1
            except:
                print('Enter a valid number')
x = input_control_x()
def oper_1_input_control():
    oper_elements = ['+', '-', '*', '/', '**', 'sqrt', 'factorial', 'floor', 'ceil', 'ln', 'log.e', 'log(x,y)', '1/x', '|x|', 'C', 'Exit']
    oper = input('Enter one of these operations {+,-,*,/,**,sqrt,factorial,floor,ceil,ln,log.e,log(x,y),1/x,|x|,C,Exit}: ')
    while oper not in oper_elements:
        print('You must enter an operation!')
        oper = input('Enter one of these operations {+,-,*,/,**,sqrt,factorial,floor,ceil,ln,log.e,log(x,y),1/x,|x|,C,Exit}: ')
    else:
        return oper
oper = oper_1_input_control()
if oper == 'Exit':
    None
degerler = []
while x != 'This operation cannot be performed':
    def input_control_y():
        oper_list = ['=', 'C', 'Exit','sqrt', 'factorial', 'floor', 'ceil', 'ln', 'log.e','1/x','|x|']
        if oper not in oper_list:
            while True:
                input_2 = input('Enter a number: ')
                if input_2.isdigit():
                    return int(input_2)
                elif input_2 == '-{}'.format(input_2):
                    return '-{}'.format(input_2)
                else:
                    try:
                        input_2 = float(input_2)
                        return input_2
                    except:
                        print('Enter a valid number')
        else:
            return None
    y = input_control_y() 
    if oper == '+':
        x = x + y
        degerler.append(x)
    elif oper == '-':
        x = x - y
        degerler.append(x)
    elif oper == '*':
        x = x * y
        degerler.append(x)
    elif oper == '/':
        if y == 0:
            x = 'This operation cannot be performed'
            degerler.append(x)
        else:
            x = x / y
            degerler.append(x)
    elif oper == '**':
        x = x ** y
        degerler.append(x)
    elif oper == 'sqrt':
        if x >= 0:
            x = math.sqrt(x)
            degerler.append(x)
        else:
            x = 'This operation cannot be performed'
            degerler.append(x)
    elif oper == 'factorial':
        if x >= 0:
            x = math.factorial(x)
            degerler.append(x)
        else:
            x = 'This operation cannot be performed'
            degerler.append(x)
    elif oper == 'floor':
        x = math.floor(x)
        degerler.append(x)
    elif oper == 'ceil':
        x = math.ceil(x)
        degerler.append(x)
    elif oper == 'ln':
        if x >= 0:
            x = math.log10(x)
            #x = math.log(x, 10)
            degerler.append(x)
        else:
            x = 'This operation cannot be performed'
            degerler.append(x)
    elif oper == 'log.e':
        if x >= 0:
            x = math.log(x)
            degerler.append(x)
        else:
            x = 'This operation cannot be performed'
            degerler.append(x)
    elif oper == 'log(x,y)':
        if x >= 0 and y >= 0:
            x = math.log(x, y)
            degerler.append(x)
        else:
            x = 'This operation cannot be performed'
            degerler.append(x)
    elif oper == '1/x':
        if x == 0:
            x = 'This operation cannot be performed'
            degerler.append(x)
        else:
            x = 1 / x
            degerler.append(x)
    elif oper == '|x|':
        x = abs(x)
        degerler.append(x)
    elif oper == '=':
        x = degerler[-1]
        print(x)
    elif oper == 'C':
        x = input_control_x()
        degerler.clear()
    elif oper == 'Exit':
        break
    def oper_2_input_control():
        oper_elements = ['+', '-', '*', '/', '**', '=','sqrt', 'factorial', 'floor', 'ceil', 'ln', 'log.e', 'log(x,y)', '1/x', 'C', 'Exit']
        oper = input('Enter one of these operations {+,-,*,/,**,sqrt,factorial,floor,ceil,ln,log.e,log(x,y),1/x,C,=,Exit}: ')
        while oper not in oper_elements:
            print('You must enter an operation!')
            oper = input('Enter one of these operations {+,-,*,/,**,sqrt,factorial,floor,ceil,ln,log.e,log(x,y),1/x,C,=,Exit)}: ')
        else:
            return oper
    oper = oper_2_input_control()
else:
    print(degerler[-1])