def calculate(f_number, znak, t_number):
    try:
        f_number = float(f_number)
        t_number = float(t_number)
    except:
        print("Ti eblan?")
        return
    if znak != "+" or znak != "-" or znak != "*" or znak != "/":
        print("Ti eblan?")
        return
    if znak == "+":
        print(f_number + t_number)
        return
    if znak == "-":
        print(f_number - t_number)
        return
    if znak == "*":
        print(f_number * t_number)
        return
    if znak == "/":
        print(f_number / t_number)
calculate()
