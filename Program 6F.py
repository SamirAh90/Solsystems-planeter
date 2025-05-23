# ***************************************************************** #
#                                                                   #
#   PROGRAMMERING:  INTRODUKTION TILL PYTHON                        #
#                                                                   #
#   Steg 6.  Selektion med if                                       #
#                                                                   #
# ***************************************************************** #

# I det här programmet kombinerar vi en loop och en if/else-sats.

# UPPGIFT:  Skapa en array med (exempelvis) planeter.
#           (Hint: titta på programmen i steg 4.)
planetNames = ["Ahmad", "Mahmood", "Jan", "Kabul"]

# UPPGIFT:  Skriv ut en instruktion till användaren med print(), och 
#           läs sedan in en planet (eller något annat) i en variabel. 
#           Titta på Program 6C.
print("Tjäna skriva något namn på en klille")
selectedPlanet = input()

# UPPGIFT:  Följ vad som händer då programmet exekverar tills du 
#           förstår hur exekveringen styrs av for-loopen och if-
#           satsen.
#           Du behöver förmodligen stega igenom programmet flera 
#           gånger, och titta på flera olika ställen:
#           * I "Variables"-fliken: Inspektera hur variabler skapas 
#             och tilldelas/förändras
#           * I Konsol-fliken: Följ utskrifterna med print()
#           * I denna Python-fil: Följ hur loopen och if-satsen styr 
#             exekveringen genom att "hoppa över" rader, eller "hoppa tillbaka".
#           Lägg till förklarande kommentarer.
#           Snygga till utskrifterna medan du håller på!
for planetName in planetNames:
    print("Detta varv i loopen hanterar vi" + planetName)
    if planetName == "Ahmad":
        print("Tur att du valde" + planetName + "för det är en himlakropp som jag vet massor om")
    else:
        print("Du valde inte" + planetName + "men jag vet också en massa om " + planetName)
pass

