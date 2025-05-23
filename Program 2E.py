# ***************************************************************** #
#                                                                   #
#   PROGRAMMERING:  INTRODUKTION TILL PYTHON                        #
#                                                                   #
#   Steg 2.  Strängar och input från användaren                     #
#                                                                   #
#   Vi utforskar nu hur vi kan hantera texter som strängar, och     #
#   tal som tal - och konvertera mellan dessa!                      #
#                                                                   #
#   Detta program gör inget vettigt, utan du ska exekvera det och   #
#   observera variablerna i minnet - alltså i "Variables"-fliken    #
#   till vänster.                                                   #
#                                                                   #
# ***************************************************************** #

# --------------------------------------------------------------
# Första halvan av programmet: Konvertering av tal till strängar
# --------------------------------------------------------------

# Vi skapar ett par variabler som innehåller tal.
number1 = 2
number2 = 17.45

# Vi skapar ett par variabler ytterligare, där vi vill lägga
# samma tal, men som strängar.
# FRÅGA:    Titta i minnet, alltså i "Variables"-fliken - vad är det
#           för skillnad mellan number1 och stringFromNumber1? Och mellan
#           number2 och stringFromNumber2?
# FRÅGA:    Vad gör alltså funktionen str()?
stringFromNumber1 = str(number1)
stringFromNumber2 = str(number2)


# -------------------------------------------------------------
# Andra halvan av programmet: Konvertering av strängar till tal
# -------------------------------------------------------------

# Vi skapar ett par strängvariabler.
string1 = "3"
string2 = "019"
string3 = "3.8"

# Vi konverterar dessa strängar till tal, och tilldelar dem till 
# ytterligare ett par variabler.
# FRÅGA:    Titta i minnet, alltså i "Variables"-fliken - vad är det
#           för skillnad mellan string1 och numberFromString1, och mellan
#           string2 och numberFromString2?
# FRÅGA:    Vad gör alltså funktionen float()?
numberFromString1AsFloat = float(string1)
numberFromString2AsFloat = float(string2)
numberFromString3AsFloat = float(string3)

# Vi gör nästan samma sak igen.
# FRÅGA:    Titta i minnet, alltså i "Variables"-fliken, och jämför
#           med de tidigare konverteringarna.
# FRÅGA:    Vad gör alltså funktionen int()?
# UPPGIFT:  Lägg på minnet att man vill ha förklarande namn på sina
#           variabler!
numberFromString1AsInt = int(string1)
numberFromString2AsInt = int(string2)


# UPPGIFT:  Stega igenom pass också.
pass


# ------------------------------------------------------
# Missa inte en till uppgift här längst ner!
# ------------------------------------------------------
# UPPGIFT:  Lägg till även en konvertering av string3 till tal
#           med funktionen int(), på samma sätt som vi gör 
#           med string1 och string2. 
# FRÅGA:    Detta kommer att ge upphov till ett fel när 
#           programmet exekverar - varför?
