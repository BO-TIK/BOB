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
    elif znak != '+' or znak != "-" or znak != "*" or znak != "/":
        result = 'Данный калькулятор не поддерживает такие операции'
        print(result)
    elif f_number or t_number != int or float:
        print("Ты чо далбаёб?")
calculate('1', '+', '2')
