# ***************************************************************** #
#                                                                   #
#   PROGRAMMERING:  INTRODUKTION TILL PYTHON                        #
#                                                                   #
#   Steg 6.  Selektion med if                                       #
#                                                                   #
#   Det här programmet är i stort sett detsamma som nyss, med ett   #
#   litet tillägg. Försök att förstå vad som händer, och lös        #
#   "HÄR_SAKNAS_NÅGOT".                                             #
#                                                                   #
# ***************************************************************** #


# UPPGIFT:  Försök att förstå vad som kommer att hända då du exekverar
#           rad 27-30. Skriv ut något lämpligt på rad 30.
#           Exekvera sedan programmet några gånger, och mata in olika 
#           strängar.

# Vi skriver ut en fråga till användaren, och läser sedan in hens 
# svar i variabeln userChoice.
print()
print("Vill du läsa viktig information om räkor? (Välj J/N)")
userChoice = input()

# Utskrift
print()
if userChoice == "J":
    print("Räkor är både rosa och rödlistade")
else:
    print("Du träckte N så du får inet svar")

# Avslutande utskrift
print("Det var allt för denna gången!")
print()
