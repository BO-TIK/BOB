def calculate(f_number, znak, t_number):
    try:
        f_number = float(f_number)
        t_number = float(t_number)
    except:
        print("Ti eblan?")
        return
    match (znak):
            case "+":
                print(f_number + t_number)
                return
            case "*":
                print(f_number * t_number)
                return
            case "/":
                print(f_number / t_number)
                return
            case "-":
                print(f_number - t_number)
            case _:
                print('ti eblan?')
                return
calculate(1, 1, 2)
calculate('в', '0', '3')
calculate('1', '/', '4')