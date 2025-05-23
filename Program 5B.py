# ***************************************************************** #
#                                                                   #
#   PROGRAMMERING:  INTRODUKTION TILL PYTHON                        #
#                                                                   #
#   Steg 5.  Iteration med for-loop                                 #
#                                                                   #
#   Ett fungerande program, att hänga med på och ändra lite         #
#   grann i.                                                        #
#                                                                   #
# ***************************************************************** #

# UPPGIFT:  Exekvera programmet flera gånger, tills du hänger med på
#           vad som händer. Titta både på "Variables"-fliken och i
#           konsol-fliken.
# UPPGIFT:  Lägg sedan till några element (djur) i arrayen. Exekvera
#           igen några gånger tills du hänger med på vad som händer.

# Vi skapar samma array som i Program 4A.
cuteAnimals = ["Fisk", "Sjöstjärna", "Sjöhäst", "Bläckfisk", "Krabba"]

# Vi skriver ut ett trevligt startmeddelande.
print()
print("Här kommer en massa gulliga havsdjur:")

# Vi loopar igenom arrayen och skriver ut varje havsdjur:
for cuteAnimal in cuteAnimals:
    print(cuteAnimal)

# Vi skriver ut ett trevligt avslutningsmeddelande:
print("Det var allihopa!")
print()


# ------------------------------------------------------
# Extra uppgift (frivillig)
# ------------------------------------------------------
# UPPGIFT:  Skriv även ut HUR MÅNGA djur du har i arrayen! Till
#           exempel med följande sats på rad 20:
#           print("Här kommer" + numberOfAnimals + " gulliga havsdjur:")
#           Du får reda på längden av en array med funktionen len().
