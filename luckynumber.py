from random import randint

geheim = randint(1, 20)
tipp = 0
i = 0

print ("Ein kleines Zahlenratespiel")
print ("================")

while tipp != geheim:

    tipp = int(input("Schlage eine Zahl vor: "))

    if tipp < geheim:
        print ("Dein Vorschlag ist zu klein")

    if tipp > geheim:
        print ("Dein Vorschlag ist zu gross")
    i = i + 1

print ("Klasse, du hast es in ", i, "Versuchen gschaft, ein gutes Tier!")
