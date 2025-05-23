# ***************************************************************** #
#                                                                   #
#   PROGRAMMERING:  INTRODUKTION TILL PYTHON                        #
#                                                                   #
#   Steg 7.  Datastrukturen Dictionary                              #
#                                                                   #
#   Det här programmet gör samma sak som det förra, men läser in    #
#   ett havsdjur från användaren.                                   #
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

# Vi ställer en fråga till användaren, om vilket djur hen vill lära sig
# mer om, och läser in svaret.
# UPPGIFT:  Exekvera programmet flera gånger, och mata in både strängar
#           (alltså djur) som finns, och som inte finns, i Dictionary:n.
#           Vad händer? Varför?
# Hint: om programmet inte hämtar ut det fakta du tänkt dig, kom ihåg att 
# versaler och gemener är olika tecken! "A" och "a" är olika tecken. 
# Med andra ord: strängar hanteras "case-sensitive".
print()
print("Skriv in ett havsdjur som du vill lära dig mer om:")
selectedAnimalName = input()

# För att hämta fakta om ett visst djur (d.v.s. värdet), anger 
# vi djurets namn (d.v.s. nyckeln) inom hakparentes.
# FRÅGOR:   På nästa rad ser vi nu TRE variabler. Titta på dem i
#           "Variables"-fliken.
#           * Vilken variabel är själva Dictionary:n?
#           * Vad är nyckeln? D.v.s. vad används som key till Dictionary:n?
#           * Vad hämtar vi ut?
#           * Vad innehåller "cuteAnimalFact" då raden har exekverats?
cuteAnimalFact = cuteAnimalsFacts[selectedAnimalName]

# Och så gör vi en utskrift.
# UPPGIFT:          Snygga till utskriften med mellanslag på lämpliga ställen.
# EXTRA UPPGIFT:    Vill du snygga till meningen, så att inte själva fakta 
#                   börjar med stor bokstav? Lägg till .lower() efter variabeln 
#                   cuteAnimalFact, så anropas en funktion som returnerar
#                   strängen konverterad till gemener (lowercase, alltså "små
#                   bokstäver").
print("Visste du att en " + selectedAnimalName + cuteAnimalFact.lower())

