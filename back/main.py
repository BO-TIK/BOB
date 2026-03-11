def calculate(f_number, znak, t_number):
    if znak == "+":
        result = f_number + t_number
        print(result)
    elif znak == "-":
        result = f_number - t_number
        print(result)
    elif znak == "*":
        result = f_number * t_number
        print(result)
    elif znak == "/":
        result = f_number / t_number
        print(result)
    elif znak != '+' or znak != "-" or znak != "*" or znak != "/" or f_number != int or float or t_number != int or float:
        result = 'Данный калькулятор не поддерживает такие операции'
        print(result)
calculate()
