# ***************************************************************** #
#                                                                   #
#   PROGRAMMERING:  INTRODUKTION TILL PYTHON                        #
#                                                                   #
#   Steg 2.  Strängar och input från användaren                     #
#                                                                   #
#   OBS: DETTA PROGRAM KOMMER ATT GE ETT FEL NÄR DU EXEKVERAR!      #
#                                                                   #
#   Detta program illustrerar ytterligare ett fel som uppstår       #
#   då man missar att konvertera variabler till rätt datatyp.       #
#                                                                   #
# ***************************************************************** #

# Vi ber användaren om ett tal.
# UPPGIFT:  Exekvera programmet och mata in ett tal i konsol-fliken,
#           till exempel 2 eller 17 eller 918.54.
print()
print("Ange ett tal, så ska jag göra en intressant beräkning")
aNumberAsString = input()

# Vi konverterar först användarens input från en sträng till ett tal
# och vips! så går det bra att göra en beräkning:
# UPPGIFT:  Undersök variablerna i "Variables"-fliken.
aNumber = float(aNumberAsString)
result = 2 + aNumber

# UPPGIFT:  Notera felet som uppstår. Undersök variabeln aNumber i
#           "Variables"-fliken till vänster.
#           Förklaring: Tal plus tal skulle gå att räkna ut som en 
#           addition, men variabeln aNumber innehåller ju en sträng.
print()
print("Jag har adderat två till talet du matade in:")
print(result)
print()

# UPPGIFT:  Exekvera programmet igen, men mata in några tecken som 
#           INTE är ett tal i konsol-fliken, till exempel Hej eller
#           namnet på ditt husdjur. Vad händer? Varför?

