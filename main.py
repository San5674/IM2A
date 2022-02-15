"""
onsketLan = 150000
Kontobeholdning = int(input("skriv inn ett tall:"))
paKonto = Kontobeholdning
print(paKonto)
minEgenkapital = 10000


if paKonto <= minEgenkapital:
    print("du har desverre ikke nok egenkapital for å motta dette lånet, saken avsluttes, kom tilbake senere")
elif paKonto >= minEgenkapital:
    print("du har fått innvilget dettte lånet fordi at du har nok egenkapital, nedbetalingen av lånet blir fulgt opp videre")
"""
def dager_til_minutter():
    Dager = int(input("Skriv inn antall dager:"))
    minutter = Dager * 24 * 60
    print(minutter)
dager_til_minutter()
