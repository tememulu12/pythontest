def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

def get_formatted_name(first, last):
    full_name = f"{first}{last}"
    return full_name
while True:
    print("imie i nazwisko:")
    print("wpisz 'q' aby zakonczyc")
    f_name = input("imie: ")
    if f_name == 'q':
        break
    l_name = input("nazwisko:")
    if l_name == 'q':
        break
    formated_name = get_formatted_name(f_name, l_name)
    print(f"witaj {formated_name}")
print(build_person('pawel', 'michalik'))
print(build_person('pawel', 'michalik', 42))

designs = ['telefon', 'robot', 'sześcian']
models = []

while designs:
    current_designs = designs.pop()
    print(f"Wydruk modelu: {current_designs}")
    models.append(current_designs)

print("Wydrukowane zostały modele:")
for model in models:
    print(model)
