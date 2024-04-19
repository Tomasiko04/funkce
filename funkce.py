
#
#01
"""
def nejvetsi(x,y,z):
    maximální=max(x,y,z)
    return maximální

print(nejvetsi(10,2,15))
"""
#02
"""
import random
pc_body=0
ja_body=0
seznam_voleb=["kámen","nůžky","papír"]
kola=int(input("Kolik chcete hrát: "))
def body():
    print(f"\nPC počet bodů {pc_body}")
    print(f"Váš počet bodů {ja_body}\n")

for i in range (kola):
    body()
    
    ja_volba=input("Zadejte vaši volbu kámen/nůžky/papír: ")
    pc_volba=random.choice(seznam_voleb)
    
    if ja_volba in seznam_voleb:
        if (ja_volba == "kámen" and pc_volba == "nůžky") or \
        (ja_volba == "nůžky" and pc_volba == "papír") or \
        (ja_volba == "papír" and pc_volba == "kámen"):
            print("Vyhráli jste!")
            ja_body+=1

        elif pc_volba==ja_volba:
            print("REMÍZA. Volba se shoduje s pc. Hraj znovu")
            #kola+=1
            #print(f"pocet kol {kola}")
        else:
            print("Vyhrál počítač!")
            pc_body+=1

    
    else:
        print("Zadali jste špatnou hodnotu zadej znovu.")
if ja_body > pc_body:
        print("\nGratulujeme, vyhrál jste hru!")
        body()
elif ja_body < pc_body:
        print("\nPočítač vyhrál hru. Zkus to znovu!")
        body()
else:
    print("\nRemíza")
    body() 
"""
#03
"""
Vzorce pro výpočet:
Krychle S = 6a2 V = a3
Kvádr S = 2 ( ab + bc + ac ) V = abc
Koule S = 4πr2 V = 4/3 πr3
Válec S = 2πr2 + 2πrv V = πr2
"""
"""
import math
def s_krychle(a):
     s_kr=6*(a**2)
     print(s_kr)
def v_krychle(a):
     v_kr=a**3
     print(v_kr)

def s_kvadr(a,b,c):
     s_kv=2*( a*b + b*c + a*c )
     print(s_kv)
def v_kvadr(a,b,c):
     v_kv=a*b*c
     print(v_kv)

def s_koule(r):
     s_ko=4*(math.pi)*r*2
     print(s_ko)
def v_koule(r):
     v_ko=4/(3 *(math.pi)*(r**3))
     print(v_ko)

def s_válec(r,v):
     s_va= 2*(math.pi)*(r**2) + 2*(math.pi)*r*v
     print(s_va)

def v_válec(r):
     v_va=(math.pi)*(r**2)
     print(v_va)

x=0
while (x==0):
    teleso=input("Jaké těleso chcete počítat(krychle, kvádr, koule, válec): ")
    print(f"Vybral/a jste si {teleso}. Chcete počítat objem nebo povrch")
    vyber=input("Chcete počítat objem nebo povrch: ")
    if teleso=="krychle":
        vstup=int(input("Zadej stranu a: "))
        if vyber=="objem":
            
            v_krychle(vstup)
        else:
            
            s_krychle(vstup)
        
    elif teleso=="kvádr":
        vstup_a=int(input("Zadej stranu a: "))
        vstup_b=int(input("Zadej stranu b: "))
        vstup_c=int(input("Zadej stranu c: "))
        if vyber=="objem":
            v_kvadr(vstup_a,vstup_b,vstup_c)
        else:
            
            s_kvadr(vstup_a,vstup_b,vstup_c)

    elif teleso=="koule":
        vstup_r=int(input("Zadej stranu r: "))
        if vyber=="objem":
            v_koule(vstup_r)
        else:
            s_koule(vstup_r)

    elif teleso=="válec":
        vstup_r=int(input("Zadej stranu r: "))
        if vyber=="objem":
            v_válec(vstup_r)
        else:
            vstup_v=int(input("Zadej stranu v: "))
            s_válec(vstup_r,vstup_v)

    next=input("Chcete pokračovat?(ano/ne): ")
    if next=="ano":
        continue
    else:
        break
"""
#04
"""
def  favorite_book(title):
    print(f"Moje nejvíce oblíbená kniha je {title}.")

favorite_book(input("Zadejte vaši nejvíce oblíbenou knihu: "))

"""


#1
"""
def absolutni_hodnota(vysledek):
    if vysledek <0:
        return -vysledek
    else:
        return vysledek
        

cislo=int(input(f"Zadej cislo:"))
print(f"Absolutni hodnota čísla {cislo} je {absolutni_hodnota(cislo)}")
"""


#2
def nejvetsi2(a,b):
    if a>b:
        return a
    else:
        return b
vysledek = nejvetsi2(10, 3)
print(vysledek)


#3

def nejvetsi3(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
vysledek = nejvetsi3(-3, 19, 4)
print(vysledek)

#4

def nejvetsi(seznam):
    max_cislo = seznam[0]  # Předpokládáme, že první číslo v seznamu je největší
    for cislo in seznam:
        if cislo > max_cislo:
            max_cislo = cislo
    return max_cislo

vysledek = nejvetsi([1, 9, 3, 4, 6, 50, 9, 8, 5, 6])
print(vysledek) 

#5

def nejdelsi_string(string_a,string_b):

    if len(string_a)>len(string_b):
        return string_a
    else:
        return string_b

vysledek = nejdelsi_string("pes", "veverka")
print ("nejdelsi slovo je: " + vysledek)

#6

def spoj_stringy(seznam_str, spojovac):
    
    stryngy=seznam_str[0]

    for i in range(1,len(seznam_str)):
        stryngy+=spojovac+seznam_str[i]
    return stryngy



texty = ["ahoj", "jak", "se", "vede"]
print( spoj_stringy(texty, " °-_-> ") )
#####

def spoj_stringy(seznam_str, spojovac):
    spojeny_string = ""  
    for index, string in enumerate(seznam_str):
        if index != 0:
            spojeny_string += spojovac  
        spojeny_string += string  
    return spojeny_string


texty = ["ahoj", "jak", "se", "vede"]
print(spoj_stringy(texty, " °-_-> "))
#####


#7.1

def udelej_slovnik_seznam(tokeny):
    typy = []
    for token in tokeny:
        if token not in typy:
            typy.append(token)
    return typy


tokeny = ["ne", "ne", "ne", "on", "ne", "já", "upéci", "dikobraz", "a", "dikobraz"]
typy = udelej_slovnik_seznam(tokeny)
print(typy)



#7.2
def udelej_slovnik_slovnik(tokeny):
    typy = {}
    for token in tokeny:
        typy[token] = True              # Klíčům přiřadím libovolnou hodnotu jde mi o klíče
    return list(typy.keys())


tokeny = ["ne", "ne", "ne", "on", "ne", "já", "upéci", "dikobraz", "a", "dikobraz"]
typy = udelej_slovnik_slovnik(tokeny)
print(typy)
#7.3
def udelej_slovnik_mnozina(tokeny):
    typy = set(tokeny)
    return list(typy)

tokeny = ["ne", "ne", "ne", "on", "ne", "já", "upéci", "dikobraz", "a", "dikobraz"]
typy = udelej_slovnik_mnozina(tokeny)
print(typy)

#8
def pocet_slabik(slovo):
    souhlasky = "bcčdďfghjklmnňpqrřsštťvwxzž"
    pocet_samohlasek = 0
    for pismeno in slovo:
        if pismeno.lower() not in souhlasky:
            pocet_samohlasek += 1
    # Počet slabik bude počet samohlásek mínus počet spojených dvojic souhlásek
    pocet_slabik = pocet_samohlasek - slovo.count("au") - slovo.count("ou") - slovo.count("eu") - slovo.count("ie") - slovo.count("y")
    return max(pocet_slabik, 1)  # Minimum jedna slabika i pro jednoslabičná slova

print(pocet_slabik("veverka"))


#9
def je_string_palindrom(string):
    return string==string[::-1]
print(je_string_palindrom("radar"))
print(je_string_palindrom("kvik"))
#10
def jen_suda(seznam):
    seznam_suda=[]
    for i in range(0,len(seznam)):
        if seznam[i]%2==0:
            seznam_suda.append(seznam[i])
    return seznam_suda
cisla = [1, 8, 5, 43, 22]
print(jen_suda(cisla))