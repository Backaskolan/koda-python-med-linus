## Interaktivitet med input() - frivilligt!

Testa att använda funktionen `input()`. Den väntar på att användaren ska skriva något som du sedan kan göra något med.

Om du kör programmet ser du att `input()` ger tillbaka en textsträng och `add(1, 2)` ger tillbaka `12`.

Du behöver göra om textsträngen till ett tal. Det gör du genom att skriva `return int(num1)+int(num2)` i din funktion istället för bara `return num1+num2`. 

`int()` gör alltså om en variabel till ett tal - men vad händer om man skriver en bokstav som `input`?

### Viktigt!
repl.it gillar inte att rätta uppgifter med `input()` i sig. Kommentera bort raderna med `input()` genom att sätta en `#` framför dem innan du klickar på submit. Såhär ska det se ut på alla rader med input:
`# x = input("Skriv första talet: ")`
