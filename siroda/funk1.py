def powitanie(imie: str):
    print(f"witam, {imie.title()}!")

def powitanie2(imie: str, wiek=18, *liczba):
    return f"{imie.title()} lat {wiek} {liczba}"

powitanie("tomek")
powitanie(str(300))
print(powitanie("jarek"))
imie = powitanie2("jarek", 2,3,4,7,8)

imiona = []
imiona.append(imie)
print(imiona)