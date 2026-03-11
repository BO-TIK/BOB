def calculate(f_number, znak, t_number):
    type_number = type(f_number)
    typet_number = type(t_number)
    if type_number or typet_number != int or float:
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

calculate(1, '+ ',3)

print(type(2))
