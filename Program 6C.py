# ***************************************************************** #
#                                                                   #
#   PROGRAMMERING:  INTRODUKTION TILL PYTHON                        #
#                                                                   #
#   Steg 6.  Selektion med if                                       #
#                                                                   #
#   Programmet fungerar. Det här programmet skriver ut en text      #
#   _endast_ om användarens favoritdjur är Räka.                    #
#                                                                   #
# ***************************************************************** #


# Vi skriver ut en instruktion till användaren med print(), och läser sedan
# in hens favoritdjur i variabeln theFavoriteAnimal.
print()
print("Skriv in ditt favoritdjur:")
theFavoriteAnimal = input()

# UPPGIFT: Exekvera programmet några gånger, och mata in följande varianter
#          av "Räka". Vad händer? Vad händer _inte_? Varför?
#          (Stega igenom programmet för att riktigt se vad som händer.)
#          a) "räka"
#          b) "Räka"
#          c) "RÄKA"
#          d) "Räkor"
#          Uppdatera sedan kommentaren på rad 32.

# Utskrift
print()
print("Nu ska jag (kanske) berätta något viktigt...")

# Utskrift men endast om... 
if theFavoriteAnimal == "Räka":
    print("Du älskar visst räkor allra mest")

# Avslutande utskrift
print("Nu har jag berättat färdigt!")
print()
