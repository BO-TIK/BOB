first_start = True

def its_first():
    global first_start
    first_start = False

while True:
    first_tr = True
    temp_tr = True


    first_num = ''
    znak = ''
    temp_num = ''

    if first_start:
        print('Здраствуй ты в калькуляторе')
        its_first()

    print('введи число')
    while first_tr:
        try:
            first_num = int(input())
            first_tr = False
        except:
            print('число долбаеб')

    print('теперь знак')
    znak = input()

    print('теперь на что ну ты понял второе число')
    while temp_tr:
        try:
            temp_num = int(input())
            temp_tr = False
        except:
            print('число долбаеб')

    print(first_num, temp_num, znak)



