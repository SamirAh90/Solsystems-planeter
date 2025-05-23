# ***************************************************************** #
#                                                                   #
#   PROGRAMMERING:  INTRODUKTION TILL PYTHON                        #
#                                                                   #
#   Steg 4.  Datastrukturen Array                                   #
#                                                                   #
#   Vi övar lite till på att skriva arrayer.                        #
#                                                                   #
# ***************************************************************** #

# UPPGIFT:  Skapa en egen array och skriv ut den.
import array as arr

number = arr.array("i", [10, 20, 30])

print(number[2])


print(", " .join([str(number[0]), str(number[2]), str(number[1])]))

pass
