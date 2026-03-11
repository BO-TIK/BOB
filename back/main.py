def calculate(f_number, znak, t_number):
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
if isinstance(f_number, (int, float) and isinstance(t_number, (int, float))):
    calculate()
else:
    print("ZOV")
