# ***************************************************************** #
#                                                                   #
#   PROGRAMMERING:  INTRODUKTION TILL PYTHON                        #
#                                                                   #
#   Steg 5.  Iteration med for-loop                                 #
#                                                                   #
#   Här behöver du själv fylla i saker vid "HÄR_SAKNAS_NÅGOT", men  #
#   det är i stort sett samma program som i Program 5A och 5B.      #
#                                                                   #
# ***************************************************************** #

# Vi skapar en array med gulliga djur.
cuteAnimals = ["Samir", "Ahamd", "Jan", "Kabul", "Jalal", "Nawid"]

# Vi skriver ut ett trevligt startmeddelande.
print("Wellcome till vår program")

# Vi loopar igenom arrayen och skriver ut varje havsdjur.
for cuteAnimal in cuteAnimals:
    print(cuteAnimal + " " +"är ett jättegulligt djur")

# FRÅGA:   Som du ser "slog vi ihop" två strängar - vad är det mer formella
#          ordet för "slå ihop"?
# UPPGIFT: Det var något som inte blev så snyggt i utskriften när strängarna
#          "slogs ihop"; justera detta.

# Vi skriver ut ett trevligt avslutningsmeddelande.
print("tack")
