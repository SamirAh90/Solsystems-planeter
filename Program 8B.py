# ***************************************************************** #
#                                                                   #
#   PROGRAMMERING:  INTRODUKTION TILL PYTHON                        #
#                                                                   #
#   Steg 8.  Vi knyter ihop alltsammans:                            #
#            * Variabler, strängar, exekvering                      #
#            * Input och output från/till användaren,               #
#               funktionsanrop                                      #
#            * Datastrukturerna Array och Dictionary,               #
#            * Iteration med for-loop                               #
#            * Selektion med if                                     #
#                                                                   #
#   Nu närmar vi oss slutet! Jämfört med förra programmet lägger    #
#   vi in en if-sats. Lös några "HÄR_SAKNAS_NÅGOT" med hjälp av     #
#   tidigare filer.                                                 #
#                                                                   #
# ***************************************************************** #


# Vi skapar en array med namnen på söta havsdjur.
cuteAnimals = ["Fisk", "Sjöstjärna", "Sjöhäst", "Bläckfisk", "Krabba"]

# Vi definierar tre Dictionary:s.

cuteAnimalsFacts = {
    "Fisk": "Simmar och blubbar",
    "Sjöstjärna": "Kravlar sig fram på botten",
    "Sjöhäst": "Galopperar sig fram",
    "Bläckfisk": "Har en distribuerad hjärna",
    "Krabba": "Nyps!",
}

# Här definierar vi en Dictionary med färger på samma djur.
cuteAnimalsColors = {
    "Fisk": "Blå",
    "Sjöstjärna": "Orange",
    "Sjöhäst": "Blek",
    "Bläckfisk": "Anpassar sig efter omgivningen",
    "Krabba": "Blir röd när den kokas",
}

# Här definierar vi en Dictionary med storlekar på djuren.
cuteAnimalsSizes = {
    "Fisk": "Medelstor",
    "Sjöstjärna": "Ganska liten",
    "Sjöhäst": "Pytteliten",
    "Bläckfisk": "Kan vara både liten och jättejättestor",
    "Krabba": "Strax under medellängd",
}

# Vi ställer en ja-/nej-fråga till användaren, och läser in svaret:
print()
print("Vill du lära dig om havets djur? Svara J eller N.")
userResponse = input()
print()

# Med hjälp av en if-/else-sats väljer vi väg beroende på användarens svar:
if userResponse == "J":
    for cuteAnimal in cuteAnimals:
        # Vi hämtar ut fakta, färg, m.m. ur våra Dictionary:s, och skriver ut detta:
        animalFact = cuteAnimalsFacts[cuteAnimal]
        animalColor = cuteAnimalsColors[cuteAnimal]
        animalSize = cuteAnimalsSizes[cuteAnimal]
    # Och så gör vi en utskrift av detta:
        print("Djur:", cuteAnimal)
        print("Fakta:", animalFact)
        print("Färg:", animalColor)
        print("Storlek:", animalSize)
        print("------------------------------")
    
else:
    print("Då ska jag inte tråka ut dig med fakta!")

# Avslutande utskrift.
print()
print("Hej då, simma lugnt!")
print()
