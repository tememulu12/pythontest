from kalkulator import kalkulator_funk

while True:
    num1 = float(input("Enter_first_number= "))
    num2 = float(input("Enter_second_number= "))
    menu = input("Enter menu add/sub/div/mult= ")
    if menu in ['add', 'sub', 'div', 'mult']:
        if menu == 'add':
            print(kalkulator_funk.addition(num1=num1, num2=num2))
        elif menu == 'sub':
            print(kalkulator_funk.subtraction(num1=num1, num2=num2))
        elif menu == 'div':
            print(kalkulator_funk.division(num1=num1, num2=num2))
        elif menu == "mult":
            print(kalkulator_funk.multiplication(num1=num1, num2=num2))

        exit_kal = input("Jesli chcesz zakonczyc pracy wypisz 'q'= ")
        if exit_kal == 'q':
           break
    else:
        print("invalid input")