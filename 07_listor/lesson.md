## Listor - list()

Ibland vill du samla flera variabler i en och samma samlingsvariabel. Ett sätt att göra det i Python är genom att göra en `list()`.

I koden till vänster har jag gjort en lista som heter `djuren` och som innehåller tre djur: apa, björn och citronfjäril.

Om jag sedan skriver ut min lista med `print(djuren)` får jag tillbaka min lista.

Vill jag veta hur många saker jag har i min lista kan jag använda `len(djuren)`. `len()` känner du igen från lektionen om textsträngar - den funkar på listor också!

På tal om textsträngar: de har en funktion som heter `join()` som tar en `list()` som argument. `join()` tar alla saker i en lista och sätter ihop dem till en textsträng. Du kan själv välja hur du vill dela upp sakerna i listan.

Du kan komma åt en enskild sak i en lista på samma sätt som du kan komma åt en enskild bokstav i en textsträng: genom `[index]`. Den första saken i listan har index `[0]`, precis som i textsträngen.

Du kan *loopa* igenom en lista precis som du gjorde med `range()`. En `for`-loop kan ge tillbaka varje sak för sig. Du kan också göra nånting med varje sak i loopen - till exempel köra `len()` på varje sak för sig.

*Vad är det för skillnad på `len(djuren)` och `len(djur)` i en `for`-loop?*

Vill du lägga till saker i din lista använder du `append()`. Det lägger till det du skriver i `(parentes)` sist i listan.

Du byter ut ett djur i listan genom att sätta ett nytt innehåll på djurets `index`.

*Kan du komma på hur du ska göra för att någon som använder ditt program kan lägga till egna djur i listan?*