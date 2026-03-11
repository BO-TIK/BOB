def calculate(f_number, znak, t_number):
    try:
        f_number = float(f_number)
        t_number = float(t_number)
    except:
        print("Ti eblan?")
        return
    if znak == "+":
        print(f_number + t_number)
        return
    elif znak == "-":
        print(f_number - t_number)
        return
    elif znak == "*":
        print(f_number * t_number)
        return
    elif znak == "/":
        print(f_number / t_number)
    else:
        print('такого знака нет')
calculate(1, 1, 2)
calculate('в', '0', '3')
calculate('1', '/', '4')
