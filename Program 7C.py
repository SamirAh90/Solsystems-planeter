# ***************************************************************** #
#                                                                   #
#   PROGRAMMERING:  INTRODUKTION TILL PYTHON                        #
#                                                                   #
#   Steg 7.  Datastrukturen Dictionary                              #
#                                                                   #
#   Det här programmet gör samma sak som i Program 7B - _plus_ att  #
#   vi använder flera Dictionary:s, för olika syften.               #
#                                                                   #
#   Vi har en uppslagsbok för "Allmänna fakta", en för "Färg", och  #
#   #en som heter "Storlek". I uppslagsboken "Färg" kan jag slå     #
#   upp till exempel "Bläckfisk", och få reda på bläckfiskens       #
#   färg. Vill jag få reda på om "Bläckfisk" är stor eller liten,   #
#   använder jag i stället uppslagsboken "Storlek".                 #
#                                                                   #
# ***************************************************************** #


# Vi skapar en Dictionary som innehåller en kort faktatext om några
# söta havsdjur.
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

# Vi ställer en fråga till användaren, om vilket djur hen vill lära sig
# mer om, och läser in svaret.
print("Hej vilken djur vill dulära dig mer om?")
selectedAnimalName = input()

# För att hämta fakta om ett visst djur, använder vi nyckel inom hakparentes.
# UPPGIFT:  Följ mönstret för de två första raderna på den tredje raden.
selectedAnimalFact = cuteAnimalsFacts[selectedAnimalName]
selectedAnimalColor = cuteAnimalsColors[selectedAnimalName]
selectedAnimalSize = cuteAnimalsSizes[selectedAnimalName]

# Och så skriver vi ut alltsammans.
# UPPGIFT:  Sätt ihop trevliga strängar att skriva ut.
print("Här är begärde uppgifter " + "Facta: " + selectedAnimalFact + "Färg: " + selectedAnimalColor + "Name: " + selectedAnimalSize)
