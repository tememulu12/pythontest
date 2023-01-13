def multi(a, b):
    try:
        return a * b
    except TypeError:
        return 0


multi("a", "b")
multi(3, 3)


def multi2(a, b):
    try:
        return int(a) * int(b)
    except (TypeError, ValueError):
        # logging.warning('błędna operacja')
        return "błędne dane"


multi2("a", "b")
multi2(3, 3)


def multi3(a, b):
    try:
        return int(a) * int(b)
    except Exception as e:
        return f"błędne dane - błąd {e.args}"


multi3("a", "b")
multi3(3, 3)


valid_data = [{'name': 'Jan', 'age': '10'}, {'name': 'Dawid', 'age': '25'}, {'name': 'Marcin', 'age': '23'}]
invalid_dict = [{}, {'name': 'Dawid', 'age': '25'}, {'name': 'Marcin', 'age': '23'}]
invalid_dict1 = [{'name': 'Jan', 'age': 'age'}, {'name': 'Dawid', 'age': '25'}, {'name': 'Marcin', 'age': '23'}]


def check_age(users, age):
    count = 0
    for i, user in enumerate(users):
        try:
            user_age = int(user['age'])
        except KeyError:
            print(f'Niepoprawne dane: {user}')
        except ValueError:
            print(f'Niepoprawny wiek: {user}')
        else:
            count += 1 if user_age < age else 0
        finally:
            print(f"{i}-{user}")
    return f"Ilość osób spełniających kryteria: {count}"


print(check_age(valid_data, 15))
print(check_age(invalid_dict, 45))
print(check_age(invalid_dict1, 45))

