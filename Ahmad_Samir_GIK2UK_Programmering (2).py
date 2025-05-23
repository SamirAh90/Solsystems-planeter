# ***************************************************************** #
#                                                                   #
#   PROGRAMMERING:  INTRODUKTION TILL PYTHON                        #
#                                                                   #
#   Mitt program, av Samir Ahmad                                    #
#                                                                   #
# ***************************************************************** #

# Skriv ett program enligt instruktionerna!

# Kort intorduktion om programmet
""" Detta program ger en interaktiv introduktion till vårt solsystems planeter. Användaren välkomnas och får information om de åtta planeterna: Merkurius, Venus, Jorden, Mars, Jupiter, Saturnus, Uranus och Neptunus. Genom att skriva namnet på en planet får användaren fakta, färg, storlek och en visuell representation av den valda planeten.
Målet är att utbilda och inspirera användare om solsystemet på ett enkelt och engagerande sätt."""

# Programmet startas från här:
print("***** Hej och välkommen till programmet! *****")
print("\nVisste du att det finns åtta planeter i vårt solsystem?")
print("\nDe är:")
print("- Merkurius")
print("- Venus")
print("- Jorden")
print("- Mars")
print("- Jupiter")
print("- Saturnus")
print("- Uranus")
print("- Neptunus\n")


# En array med namnen på himlakroppar.
celestialBodies = ["Merkurius", "Venus", "Jorden", "Mars", "Jupiter", "Saturnus", "Uranus", "Neptunus"]

# Dictionary som innehåller fakta om varje himlakropp
celestialBodyFacts = {
    "Merkurius": "Den närmaste planeten till solen och har inga månar.",
    "Venus": "Kallas ofta Jorden's tvilling men har en extremt het atmosfär.",
    "Jorden": "Den enda planeten med liv och har en atmosfär som stödjer vatten i flytande form.",
    "Mars": "Kallas den röda planeten på grund av järnoxid på ytan.",
    "Jupiter": "Den största planeten i solsystemet med en stor röd fläck som är en storm.",
    "Saturnus": "Känd för sina spektakulära ringar som består av is och sten.",
    "Uranus": "En gasjätte som roterar på sin sida och har ett svagt ringsystem.",
    "Neptunus": "Den mest avlägsna planeten med starka vindar och ett mörkt blått utseende.",
}
# Dictionary innehållande information om färger för varje himlakropp
celestialBodyColors = {
    "Merkurius": "Gråaktig med kraterliknande yta.",
    "Venus": "Gulaktig på grund av svavelsyra i atmosfären.",
    "Jorden": "Blå och grön, dominerad av vatten och vegetation.",
    "Mars": "Röd på grund av järnoxid.",
    "Jupiter": "Brun och orange med vita molnband.",
    "Saturnus": "Ljusgul på grund av dess gaser och ringar.",
    "Uranus": "Blågrön på grund av metan i atmosfären.",
    "Neptunus": "Djup blå, också på grund av metan i atmosfären.",
}
# Dictionary innehållande information om storlekar för varje himlakropp
celestialBodySizes = {
    "Merkurius": "Den minsta planeten i solsystemet.",
    "Venus": "Näst största planeten efter Jorden.",
    "Jorden": "Mellan storleken bland planeterna.",
    "Mars": "Lite mindre än Jorden.",
    "Jupiter": "Den största planeten i solsystemet.",
    "Saturnus": "Den näst största planeten.",
    "Uranus": "Tredje största planeten.",
    "Neptunus": "Lite mindre än Uranus.",
}

# Dictionary för visuella representationer för varje planet med hjälp av text
planetVisuals = {
    "Merkurius": "      \n   ___   \n  /   \\  \n |  O  | \n  \\___/  ", 
    "Venus": "      \n   _____  \n  /     \\ \n |   O   |\n  \\_____/ ", 
    "Jorden": "      \n   ___   \n  / O \\  \n |     | \n  \\___/  ",  
    "Mars": "       \n   _/\\_  \n  | O |  \n  |   |  \n   \\_/   ",  
    "Jupiter": "      \n  .-=-.  \n /     \\ \n|   O   |\n \\     / ",  
    "Saturnus": "      \n   ___   \n  /~~~\\  \n |  O  | \n  \\___/  ", 
    "Uranus": "      \n   ___   \n  | O |  \n  |   |  \n  \\___/  ", 
    "Neptunus": "      \n    O   \n  / | \\  \n /     \\ \n|_______| ",
}

# Programmet ber användaren att ange namnet på en himlakropp för att hämta information om den.
print("Vilken himlakropp vill du lära dig mer om? Skriv namnet, till exempel (Uranus), så dyker vi in i dess värld!🌟🌌")
selectedPlanetName = input()

# Initierar en variabel för att kontrollera om planeten hittades.
found = False

# Koden letar (Loopar) igenom en lista av himlakroppar för att hitta en specifik planet. När den hittar planeten, sätts en flagga till True, och den hämtar fakta, färg, storlek och visuell information om den planeten och sparar i respektiv variabl.
for planetName in celestialBodies:
    if selectedPlanetName == planetName:
        found = True  # Planeten har hittats
        planetFact = celestialBodyFacts[planetName]  # Hämtar fakta om planeten
        planetColor = celestialBodyColors[planetName]  # Hämtar färginformation
        planetSize = celestialBodySizes[planetName]  # Hämtar storleksinformation
        planetVisual = planetVisuals[planetName]  # Hämtar visuell information
        
        # Skriver ut informationen om planeten.
        print()
        print("Himlakropp: " + "\033[32m\"" + planetName.upper() + "\"\033[0m")
        print("Fakta:", planetFact)
        print("Färg:", planetColor)
        print("Storlek:", planetSize)
        print("Visual:  \n " + "\033[33m" + planetVisual + "\033[0m") 
        print("------------------------------")
        
# Skriver ut ett meddelande om planeten inte hittades.
if not found:
    print("Ursäkta, jag har ingen information om: " + "\033[31m\"" + selectedPlanetName.upper() + "\"\033[0m" + ". Det verkar som att denna planet fanns inte i min tid!")

# Avslutande utskrift.
print()
print("Hej då, tack att du anvönder vårt program och glöm inte att simmma lungt!")
