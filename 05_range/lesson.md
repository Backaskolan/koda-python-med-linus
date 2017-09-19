## Funktionen range()

`range()` är ett sätt att skapa en lista med en rad nummer som man sen kan *loopa* igenom. Det kan vara användbart i många fall.

Titta på exemplet till vänster. Jag har skapat en variabel som heter `r` och som innehåller en `range()` med talen 0-9. Precis som `index` i en textsträng börjar Python räkna på 0 och inte på 1.

Kör koden `(Ctrl+Enter)` och se om du kan räkna ut vad som händer!

Först skriver vi ut själva variabeln `r` till skärmen. `r` innehåller en `range()` från 0 till 9, och det är vad vi får.

Sen kommer nästa del och den består av ett slags *loop* - en `for`-loop. Den säger helt enkelt att

`För varje nummer i vår range r:
  skriv ut numret`
  
`for`-loopen går igenom vår `range()` och skriver ut varje nummer från 0 till 9 och sedan avslutar den.

*Hur gör vi om vi till skriva ut alla nummer från 0-25?*
Eftersom `range()` börjar på 0 hoppar den över det sista talet. Vill vi skriva ut alla ta från 0-25 behöver vi skriva `range(26)`.

*Men om jag inte vill börja på 0?*
Du kan också tala om för `range()` att börja på ett annat tal än 0. Vill du till exempel ha siffrorna 5-10 skriver du `range(5, 11)`.
(Eftersom den hoppar över sista talet måste du själv lägga till ett och skriva 11 istället för 10).

*Jaha, men jag kanske inte vill skriva ut precis **alla** tal?*
`range()` kan också ta ett tredje *argument*, som kallas `step`. Det talar om för `range()` hur många tal du vill hoppa över. Vad tror du `range(2, 10, 2)` ger för resultat?

**Vidare arbete**
Testa lite olika argument till `range()`-funktionen. Vad händer om du skriver `range(1000)`?