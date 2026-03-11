def calculate(f_number, znak, t_number):
    if f_number or t_number != int or float:
        print("Ты чо далбаёб?")
    elif znak != '+' or znak != "-" or znak != "*" or znak != "/":
        result = 'Данный калькулятор не поддерживает такие операции'
        print(result)
    elif znak == "+":
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

calculate()
