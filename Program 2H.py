# ***************************************************************** #
#                                                                   #
#   PROGRAMMERING:  INTRODUKTION TILL PYTHON                        #
#                                                                   #
#   Steg 2.  Strängar och input från användaren                     #
#                                                                   #
#   Nu är din uppgift att fylla i saker som saknas för att skapa    #
#   ett fungerande program. Ändra överallt där det står             #
#   HÄR_SAKNAS_NÅGOT, utifrån vad det står i kommentarerna.         #
#                                                                   #
#   Vi vill räkna ut omkrets och area för en cirkel utifrån         #
#   radien, precis som i Program 1E, men vi vill läsa in radien     #
#   från användaren. Vi ser till att hantera konverteringar mellan  #
#   strängar och tal för att undvika problemen vi stötte på i de    #
#   senaste programmen!                                             #
#                                                                   #
# ***************************************************************** #


# Vi ber användaren om en radie.
print("Ange en radie, så ska jag beräkna cirkelns omkrets och area")
radiusAsString = input()

# För att kunna använda talet vid beräkningarna längre ner 
# konverterar vi användarens input till ett tal. Vi skapar en variabel
# som vi ger namnet radius.
radius = float(radiusAsString)

# Vi skapar och tilldelar variabeln pi.
pi = radius

# Vi beräknar omkrets och area.
circumference = HÄR_SAKNAS_NÅGOT
area = HÄR_SAKNAS_NÅGOT

# Vi gör utskrifter som i Program 1D, men gör dem snyggare genom att
# konkatenera (bygga ihop) trevliga strängar (rad 42 och 43).
# För att kunna göra det konverterar vi först de beräknade värdena 
# till strängar på rad 40 och 41.
circumferenceAsStr = str(circumference)
areaAsStr = str(area)
circumferenceMessage = "Omkretsen är " + circumferenceAsStr
areaMessage = "Arean är " + areaAsStr

print()
print(circumferenceMessage)
print(areaMessage)
print()