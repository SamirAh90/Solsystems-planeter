# ***************************************************************** #
#                                                                   #
#   PROGRAMMERING:  INTRODUKTION TILL PYTHON                        #
#                                                                   #
#   Steg 6.  Selektion med if                                       #
#                                                                   #
#   Det här programmet fungerar nästan, men du behöver fixa         #
#   ett "HÄR_SAKNAS_NÅGOT". Programmet gör samma sak som nyss,      #
#   plus en sak till: om favoritdjuret _inte_ är "Räka", skriver    #
#   programmet _också_ ut något.                                    #
#                                                                   #
# ***************************************************************** #


# UPPGIFT:  Exekvera programmet några gånger, och mata in olika strängar.
#           Vad händer? Varför?

# Vi skriver ut en instruktion till användaren med print(), och läser sedan
# in hens favoritdjur i variabeln theFavoriteAnimal.
print()
print("Skriv in ditt favoritdjur:")
theFavoriteAnimal = input()

# Utskrift
print()
print("Nu ska jag (kanske) berätta något viktigt...")

# Ange samma villkor som i Program 6A:
if theFavoriteAnimal == "räkor":
    print("Du älskar visst räkor allra mest!")
else:
    print("Du tycker visst inget vidare om räkor")

# Avslutande utskrift
print("Nu har jag berättat färdigt")
print()
