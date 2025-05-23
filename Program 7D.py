# ***************************************************************** #
#                                                                   #
#   PROGRAMMERING:  INTRODUKTION TILL PYTHON                        #
#                                                                   #
#   Steg 7.  Datastrukturen Dictionary                              #
#                                                                   #
#   En uppgift av samma slag som nyss, som låter dig befästa        #
#   kunskaper och träna på alla små handgrepp i utvecklingsmiljön.  #
#                                                                   #
#   Skriv ett program som följer samma mönster som övriga program   #
#   i Steg 7.                                                       #
#                                                                   #
#   Börja gärna från ingenting och skriv - och kolla i föregående   #
#   filer för att friska upp hur man gör. Du kan naturligtvis       #
#   kopiera förra programmet och ändra variabelnamn o.s.v. Håll då  #
#   koden uppdaterad med avseende på variabelnamn och kommentarer!  #
#                                                                   #
# ***************************************************************** #


# UPPGIFT:  Skapa några Dictionary:s med fakta, färg, o.s.v. på något
#           intressant som du är intresserad av.# Dictionaries with correct syntax
nameFact = {
    "Ahmad": "is a nice boy",
    "Ahmal": "is a great man",
    "Zubair": "is the king",
    "Lemar": "is the sun"
}

nameAge = {
    "Ahmad": "24",
    "Ahmal": "20",
    "Zubair": "10",
    "Lemar": "0"
}

nameColor = {
    "Ahmad": "Red",
    "Ahmal": "White",
    "Zubair": "Blue",
    "Lemar": "Purple"
}

# Prompt for user input
print("Hello and welcome to the program! Please write the name of the person you want information about:")
userInput = input()
# Vi hämtar fakta om ett visst X.
userSelectedName = nameFact[userInput]
userSelectedAge = nameAge[userInput]
userSelectedColor= nameColor[userInput]

# Och så skriver vi ut alltsammans.
print("You have selected: " + userInput + "He is" + userSelectedName + "Age: " + userSelectedAge + "Color: " + userSelectedColor)

