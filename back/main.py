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
    else:
        result = 'Данный калькулятор не поддерживает такие операции'
        print(result)

calculate('hello', '-', 4)

