# ***************************************************************** #
#                                                                   #
#   PROGRAMMERING:  INTRODUKTION TILL PYTHON                        #
#                                                                   #
#   Steg 2.  Strängar och input från användaren                     #
#                                                                   #
#   OBS: DETTA PROGRAM KOMMER ATT GE ETT FEL NÄR DU EXEKVERAR!      #
#                                                                   #
#   Vi har tänkt oss att göra en beräkning med ett tal som vi       #
#   läser in från användaren, men detta program visar felet som     #
#   uppstår då vi missar att konvertera strängen från användaren    #
#   till ett flyttal!                                               #
#                                                                   #
# ***************************************************************** #

# Vi ber användaren om ett tal.
# UPPGIFT:  Exekvera programmet och mata in ett tal i konsol-fliken,
#           till exempel 2 eller 17 eller 918.54.
print()
print("Ange ett tal, så ska jag göra en intressant beräkning")
aNumber = input()

# UPPGIFT:  Notera felet som uppstår. Undersök variabeln aNumber i
#           "Variables"-fliken till vänster.
#           Förklaring: Tal plus tal skulle gå att räkna ut som en 
#           addition, men variabeln aNumber innehåller ju en sträng.
result = 2 + aNumber

# UPPGIFT:  Exekvera programmet igen, men mata in några tecken som 
#           INTE är ett tal i konsol-fliken, till exempel Hej eller
#           namnet på ditt husdjur. Förklaringen är naturligtvis
#           densamma: variabeln aNumber innehåller ju en sträng,
#           och man kan inte addera tal och strängar.


# UPPGIFT:  Ingenting. Den stackars programmeraren hade tänkt sig 
#           att skriva ut något intressant här nedan, men exekveringen
#           når ju aldrig hit. Du skulle bara få uppleva felet här 
#           ovan! Gå vidare till nästa program.  :-)
print()
print("Jag har adderat två till talet du matade in:")
print(result)
print()