# ***************************************************************** #
#                                                                   #
#   PROGRAMMERING: INTRODUKTION TILL PYTHON                         #
#                                                                   #
#   Steg 1.  Variabler, exekvering, och output till användaren      #
#                                                                   #
#   Vi ska beräkna omkretsen och arean av en cirkel. Cirkeln        #
#   ska kunna ha olika radie, och finessen är att vi ska ändra      #
#   programmet värde på EN variabel, på EN plats i programmet!      #
#                                                                   #
# ***************************************************************** #


# Vi skapar variabeln radius för radien, och tilldelar den ett värde.
# Detta är alltså radien på en cirkel.
radius = 5

# Vi skapar och tilldelar variabeln pi.
pi = 3.1415926

# Vi beräknar omkrets och area.
# (Not: "radien i kvadrat" beräknas enkelt som "radien gånger radien".)
# EXTRAUPPGIFT:
#           Träna på vad omkrets heter på engelska, om du inte 
#           redan hade kläm på det. Betoningen ska ligga på stavelsen 
#           med u:et!
circumference = 2 * radius * pi
area = (radius * radius) * pi

# Vi skriver ut omkrets och area, med funktionen print().
print()
print(circumference)
print(area)
print()

# ------------------------------------------------------
# Avslutande fråga
# ------------------------------------------------------

# FRÅGA:    Vad händer om du ändrar värdet på radien? 
#           (Not: Du ska alltså ändra värdet som tilldelas till 
#           variabeln radius på rad 16!)
