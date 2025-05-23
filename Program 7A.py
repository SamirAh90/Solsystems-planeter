# ***************************************************************** #
#                                                                   #
#   PROGRAMMERING:  INTRODUKTION TILL PYTHON                        #
#                                                                   #
#   Steg 7.  Datastrukturen Dictionary                              #
#                                                                   #
#   Vi startar med ett superenkelt, fungerande program igen.        #
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

# UPPGIFT:  Utforska "Variables"-fliken tills du kan se hela 
#           Dictionary:ns innehåll.
# FRÅGA:    Vilka är nycklarna i Dictionary:n? Vilka är värdena?

# För att hämta fakta om ett visst djur (d.v.s. värdet), anger 
# vi djurets namn (d.v.s. nyckeln) inom hakparentes.
# FRÅGOR:   På nästa rad ser vi två variabler - titta på bägge i
#           "Variables"-fliken.
#           * Vilken variabel är själva Dictionary:n?
#           * Vad är nyckeln? D.v.s. vad används som key till Dictionary:n?
#           * Vad hämtar vi ut?
#           * Vad innehåller "seaHorseFact" då raden har exekverats?
seaHorseFact = cuteAnimalsFacts["Sjöhäst"]

# Och så gör vi en utskrift bara för att det är trevligt.
print()
print("Visste du att en sjöhäst " + seaHorseFact)
print()