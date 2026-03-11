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
    if znak != '+' or znak != "-" or znak != "*" or znak != "/":
        result = 'Данный калькулятор не поддерживает такие операции'
        print(result)
    else:
        print("Ты долбаёб?")
calculate(1, "+", 1)
calculate(1, "-", 1)
calculate(1, "*", 1)
