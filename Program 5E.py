# ***************************************************************** #
#                                                                   #
#   PROGRAMMERING:  INTRODUKTION TILL PYTHON                        #
#                                                                   #
#   Steg 5.  Iteration med for-loop                                 #
#                                                                   #
#   EXTRA (FRIVILLIG) UPPGIFT.                                      #
#                                                                   #
#   Härifrån dyker det upp "extra uppgifter", både inuti filerna,   #
#   och hela filer (Program 5E). De är tänkta att ge lite           #
#   skojigare utmaningar till den som kanske gäspar sig igenom      #
#   labbserien. Om de känns mastiga kan du spara alla extra-        #
#   uppgifter till slutet, och känna efter då om du har tid och     #
#   energi att återvända till dem! De kommer att kännas enklare     #
#   då. Och du kommer klara inlämningen galant om du hoppar över    #
#   alla extrauppgifter. Därav att de är markerade som "extra".     #  
#                                                                   #
#   Programmet loopar igenom en array för att räkna antalet         #  
#   element, och göra en lite snyggare utskrift än i programmen     #
#   hittills.                                                       #
#                                                                   #
# ***************************************************************** #


# Vi skapar en array med husdjur.
petNames = ["Holger", "Ellie", "Hermann", "Tonje", "Lillis", "Mårran", "Rufsan"]

# Vi skriver ut ett trevligt startmeddelande.
print("Hej och välkommen")

# Vi loopar igenom arrayen för att göra två saker:
# 1.    Vi räknar elementen. För detta använder vi en variabel 
#       som fungerar som räknare, och räknar upp den med ett för
#       varje varv.
# 2.    Vi bygger ihop en sträng för att kunna skriva ut elementen
#       på samma rad.

# Vi initierar räknaren med värdet noll:
numOfElements = 0
stringOfAllElements = ""
# UPPGIFT:      Följ noga vad som händer medan du stegar, som vanligt 
#               genom att titta på "Variables"-fliken.
for petName in petNames:
    numOfElements = numOfElements + 1
    stringOfAllElements = petName + " " + stringOfAllElements


# Avslutande utskrift.
print("Arrayen innehåller " + str(numOfElements) + " element: " + stringOfAllElements + ".")
print()


# ------------------------------------------------------
# Missa inte fler uppgifter här längst ner!
# ------------------------------------------------------
# UPPGIFT:      Lägg till och ta bort element (husdjur) i arrayen, 
#               och följ programmet. 
# UPPGIFT:      Ändra innehållet från husdjur till något helt annat. 
#               Ändra då alltså även variabelnamn och uppdatera 
#               kommentarer! (Det ingår ALLTID då man editerar sin 
#               kod. Håll den alltid ren och snygg!)
