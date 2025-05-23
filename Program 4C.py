# ***************************************************************** #
#                                                                   #
#   PROGRAMMERING:  INTRODUKTION TILL PYTHON                        #
#                                                                   #
#   Steg 4.  Datastrukturen Array                                   #
#                                                                   #
#   Vi övar på att skriva arrayer, och vi skriver även ut dem med   #
#   funktionen print().                                             #
#                                                                   #
# ***************************************************************** #

# Vi skapar ett par arrayer som innehåller namn på lander
# UPPGIFT:  Skriv ett par arraydefinitioner, ungefär som i Program 4A 
#           och 4B. Uppdatera även kommentaren på rad 12!

nameCountry = ["Afhanistan", "Pakistan", "Sweden","Norway","India","Germany"]
nameCountryCity = ["Kabul","Islamabad","Stockholm","Oslo", "Dehli", "Berlin"]


# Här skriver vi ut...
# UPPGIFT:  Skriv in arraynamn som parameter till print, och titta på 
#           output i konsol-fliken. Uppdatera även kommentaren på rad 19!
print()
print(nameCountry[0],nameCountry[1],nameCountry[2],nameCountry[3],nameCountry[4], nameCountry[5])
print(nameCountryCity[0],nameCountryCity[1],nameCountryCity[2],nameCountryCity[3],nameCountryCity[4], nameCountryCity[5])
print(", ".join([
    nameCountry[0], nameCountryCity[0],
    nameCountry[1], nameCountryCity[1],
    nameCountry[2], nameCountryCity[2],
    nameCountry[3], nameCountryCity[3],
    nameCountry[4], nameCountryCity[4],
    nameCountry[5], nameCountryCity[5]]))
      
      
print()


# ------------------------------------------------------
# Missa inte en till uppgift här längst ner!
# ------------------------------------------------------
# UPPGIFT:  Exekvera programmet genom att välja "Run Python File" uppe till
#           höger. Om du inte redan börjat göra detta, gör det som  vana 
#           från och med nu.
