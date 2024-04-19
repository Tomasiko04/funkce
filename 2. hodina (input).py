
"""
cislo = 7
string = "ahoj"
desetine_cislo= 10.5

print(type(cislo))
print(type(string))
print(type(desetine_cislo))

"""

# osoba1_vek = input("Zadejte váš věk: ")
# print(f"Uživatel 1 zadal svůj věk: {osoba1_vek}")

# print(type(osoba1_vek))

# osoba2_vek = int(input("Zadejte svůj věk: ")) #přetypování na int


# print(type(osoba2_vek))

# print(f"Uživatel 2 zadal svůj věk: {osoba2_vek}")

# print(f"Uživatel 2 zadal svůj věk:" + str(osoba2_vek))  #přetypování na str

# print(f"Uživatel 2 má {70 - osoba2_vek} let do důchodu")


# Zjišťuje jméno a věk
#vyhodnocuje, jestli může vstoupit (nezletilý nemůže, dospělý může,
#  senior jde se slevou)

"""
Postup:

1. info-input

2. vyhodnotit, porovnat => booleovaké hodnoty, porovnávací operátory, kontext podmínky

3. výsledná zpráva => print
"""

name= str(input(" What is your name?: "))
age= int(input("How old are you?: "))

# print(f"{name}: {age}")
"""
print(f"Hello {name}, I see you are {age} years old")
print("přepočítáváááá.....")

if age < 18:
    print("Go home, kid!")

if age >= 18: #NEBO if age > 18 or == 18:
    
    print(f"Have fun,{name}")

    if age > 65:
        print(f"Welcome sir/madame {name}") 

if 18 < age > 65:
    print(f"Welcome sir/madame {name}") 

"""

if age < 18:
    print("Go home, kid!")

elif age >= 65:
    print(f"Welcome sir/madame {name}")

else:
    print(f"Welcome to our club")

