# Gissa talet

Börja med att gå igenom koden och försöka räkna ut vad den gör.

Det är ganska mycket vi inte har gått igenom redan: if-satser, while-loopar och str.format()-funktionen. Vi börjar med den sista.

## str.format()
Ibland vill du lägga till någonting i en sträng som du inte vet vad det är när du skriver koden, till exempel användarens namn, eller i det här fallet, hur många gissningar spelaren behöver för att hitta rätt tal. Då kan du använda str.format().
Säg att ditt spel börjar med att fråga spelaren om hens namn.

`namn = input('Vad heter du? ')`

Sen vill du skriva ut en hälsningsfras med namnet. Då kan du lägga in innehållet i variabeln `namn` så här:

`print('Välkommen, {0}!'.format(namn))`

`{0}` ersätts av innehållet i `namn`.
På samma sätt talar vi om för spelaren hur många gissningar hen behövde genom att skriva

`print('Det var rätt, du behövde {0} gissningar'.format(antal_gissningar))`

där `antal_gissningar` är en variabel som håller koll på hur många gissningar spelaren har använt.

## while-loopar
I vår funktion `loop()` finns det en `while`-loop.

`while int(gissning) != talet:`

Den jämför variabeln `gissning` med `talet` och loopen börjar om från början så länge de *inte* är samma. Jämförelsen `!=` betyder *är inte lika med*. `while`-loopen säger alltså

`så länge gissning inte är lika med talet`

När `gissning` faktiskt är lika med `talet`, hoppar programmet ur loopen och fortsätter köra koden under.

## if-satser
TODO