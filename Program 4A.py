# ***************************************************************** #
#                                                                   #
#   PROGRAMMERING:  INTRODUKTION TILL PYTHON                        #
#                                                                   #
#   Steg 4.  Datastrukturen Array                                   #
#                                                                   #
#   Ett färdigt fungerande program nu igen! Du ska bara stega       #
#   igenom det, och utforska vad du ser i "Variables"-fliken.       #
#                                                                   #
# ***************************************************************** #

# Vi skapar en array med namnen på söta havsdjur:
cuteAnimals = ["Fisk", "Sjöstjärna", "Sjöhäst", "Bläckfisk", "Krabba"]

# UPPGIFT:  Titta på innehållet i cuteAnimals i "Variables"-fliken. 
#           Alltså, hitta elementen "Fisk", "Sjöstjärna", o.s.v.
#           Klicka även på den lilla pilen för att expandera ("veckla 
#           ut") cuteAnimals.

print(cuteAnimals[1], cuteAnimals[0], cuteAnimals[4])
print(", ".join([cuteAnimals[0], cuteAnimals[1], cuteAnimals[3], cuteAnimals[4]]))


# Följande rad "pass" gör ingenting. Den ligger här endast för att vi vill
# hinna inspektera arrayen cuteAnimals innan programmet avslutas. Kom ihåg
# att exekvera även denna rad så att programmet exekverar färdigt.
pass
