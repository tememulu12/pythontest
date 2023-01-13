from name_function import get_formatted_name

print("Wpisz 'q' aby zakończyć")
while True:
    first = input("Podaj imię:")
    if first == 'q':
        break
    last = input("Podaj nazwisko:")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f'Imię sformatowanie: {formatted_name}')
