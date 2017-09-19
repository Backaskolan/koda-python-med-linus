# Textsträngar

En textsträng är alltså ett särskilt slags *objekt* i Python. Det finns särskilda funktioner inbyggda i Python som är till för att använda på strängar.

Vill du veta hur många tecken som finns i din sträng `s` använder du `len(s)`. `len` är en förkortning av *length*, alltså längd.

`print(len(s))`

Om du vill komma åt ett visst tecken i din sträng kan du använda `[index]`. `Index` börjar räkna på 0 och fortsätter öka med ett för varje tecken i strängen.

`print(s[0])`
ger första tecknet i strängen, alltså `P`.
`print(s[3])`
ger fjärde tecknet i strängen, alltså `h`.

*Hur kan du komma åt sista tecknet i en sträng som du inte vet hur lång den är?*

Vill du komma åt fler än ett tecken kan du använda *slicing*:

`print(s[2:5])`
ger tredje till fjärde tecknet i strängen, alltså `tho`. **Den sista siffran räknas inte.**

## Uppgifter
Gör en variabel som heter s och innehåller strängen "Python".
Gör sedan fem variabler till: a, b, c, d och e.
De ska innehålla:

  a. Första tecknet i strängen `s`, alltså `P`
  
  b. Tredje tecknet i strängen `s`, alltså `t`
  
  c. Sista tecknet i strängen `s`, alltså `n`
  
  d. Andra till och med fjärde tecknet i strängen `s`, alltså `yth`
  
  e. Längden på strängen `s`, alltså `6`
  
Skriv ut dina variabler på skärmen så du kan se att det har blivit rätt. (Använd `print()`)