# print("Tohle je můj první program ")

# print(1,2,3)

""""
komentář

-+-+-+


Multiline string
"""

"""
prvni_promena = 43
druha_promena = "43"


print(type(prvni_promena))
print(type(druha_promena))


print(prvni_promena+prvni_promena)
print(druha_promena+druha_promena)

"""

zvire = "pes"
jidlo = "steak"

# moje zvire má najraději jídlo

# print("pes"+"steak")

# print("Moje" + " " + zvire + " " + "má nejraději" + " "+ jidlo)

# print("Moje", zvire,"má nejraději", jidlo)

# # format
# print(f"Moje {zvire} má nejraději {jidlo}")


mini_zoo = ["pes", "kočka", "slepice", "ondatra"]
# print(type(mini_zoo))
print(mini_zoo)

mini_zoo.append("gepard")
mini_zoo.append("slon")
mini_zoo.remove("slepice")

print(mini_zoo)

for zvire in mini_zoo:
    print(f"V naší zoo potkáte: {zvire}")