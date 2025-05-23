# ***************************************************************** #
#                                                                   #
#   PROGRAMMERING:  INTRODUKTION TILL PYTHON                        #
#                                                                   #
#   Steg 6.  Selektion med if                                       #
#                                                                   #
#   Det här programmet fungerar, så exekvera det och se till att    #
#   du förstår det.                                                 #
#                                                                   #
# ***************************************************************** #


# UPPGIFT:  Exekvera programmet några gånger, och besvara frågan 
#           olika. Ange både stort 'J' och litet 'j'. Vad händer?
#           Varför?

# Vi skriver ut en fråga till användaren, och läser sedan in hens 
# svar i variabeln userChoice.
print()
print("Vill du läsa viktig information om räkor? (Välj J/N)")
userChoice = input()

# Utskrift
print()
if userChoice == "J":
    print("Räkor är både rosa och rödlistade")

# Avslutande utskrift
print("Det var allt för denna gången!")
print()
