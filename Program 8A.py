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
#   Vi bygger ihop allt vi lärt oss i Steg 1-7. Vi skapar en array  #
#   med havsdjur, som vi loopar igenom med en for-loop.             #
#   För varje varv i loopen, d.v.s. för varje havsdjur i arrayen,   #
#   skriver vi ut fakta, färg och storlek.                          #
#                                                                   #
# ***************************************************************** #


# UPPGIFT:  Utifrån kommentarerna, lös alla "HÄR_SAKNAS_NÅGOT".

# Vi skapar en array med namnen på söta havsdjur (se programmen i Steg 4).
cuteAnimals = ["Fisk", "Sjöstjärna", "Sjöhäst", "Bläckfisk", "Krabba"]

# Vi definierar tre Dictionary:s (se programmen i Steg 7).

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

# Och här, för varje varv i loopen skriver vi ut fakta, färg och storlek.
# UPPGIFT:          Gör vad du kan för att snygga till utskriften.
# EXTRA UPPGIFT:    Gör utskrifter ännu snyggare genom att separera
#                   stegen då en sträng byggs ihop (inuti for-loopen) 
#                   respektive skrivs ut (efter loopen), ungefär som i
#                   Program 5E.
for cuteAnimal in cuteAnimals:
    # Vi hämtar ut fakta, färg, m.m. ur våra Dictionary:s:
    animalFact = cuteAnimalsFacts[cuteAnimal]
    animalColor = cuteAnimalsColors[cuteAnimal]
    animalSize = cuteAnimalsSizes[cuteAnimal]
    # Och så gör vi en utskrift av detta:
   
    print("Djur:", cuteAnimal)
    print("Fakta:", animalFact)
    print("Färg:", animalColor)
    print("Storlek:", animalSize)
    print("------------------------------")
  