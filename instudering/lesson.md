## Instuderingsuppgifter inför provet december 2017

Ni kommer att ha tre frågor om programmering på provet. De kommer att handla om sådant vi gått igenom på lektionerna. Här kommer tre uppgifter som ni kan göra, klarar du dem kommer du fixa frågorna på provet också.

### 1. Indentering
För att Python-kod ska fungera behöver den vara indenterad på rätt sätt. Det betyder att kod som ska köras inuti till exempel en funktion eller loop måste flyttas in från kanten, antingen med `TAB`-tangenten (som ser ut som en pil med ett streck efter sig) eller med fyra mellanslag (`SPACE`). Till exempel:

```python
def hej():
	print('Hej!')
```

eller

```python
while i < 5:
	i += 1
```

#### Uppgift
Gör en funktion som heter `goddag()` och som ger tillbaka (`return`) textsträngen `'Goddag'`. Tänk på indenteringen!

### 2. Textsträngar
De olika tecknen i en textsträng får ett *index* beroende på var i strängen det står. Det första tecknet har index 0 och det sista har index -1. Om din variabel heter `s` kommer du åt tecknet genom att skriva `s[index]`. Vill du veta hur många tecken en textsträng har kan du använda den inbyggda funktionen `len(s)` som i *length*.

#### Uppgift
Skapa en variabel som heter `s` och som innehåller textsträngen `'decembernatt'`. Skapa sedan 3 variabler till: `a`, `b` och `c`. `a` ska innehålla den första bokstaven i strängen `s`, `b` ska innehålla den sista bokstaven och `c` ska innehålla antalet bokstäver i textsträngen.

### 3. Funktioner och förenkling
Vi har tittat en del på funktioner i Python. De är bra för att man ska slippa skriva samma kod flera gånger. I spelet 'Gissa talet' definierar vi funktioner som vi sedan kan köra om och om igen tills spelaren gissar rätt.

En funktion skapas genom att man skriver `def funktionens_namn():` och sedan hoppar ner en rad. Sedan måste man *indentera* (hoppa in från kanten) och fortsätta koden under.

Tänk dig att du har en robot som du kan programmera så att den kan ta sig igenom en labyrint. Tyvärr har den gått lite sönder och kan bara svänga åt höger. Men eftersom du är en smart person har du kommit på att du kan få den att svänga till vänster genom att svänga höger tre gånger! Dit program för att roboten ska komma ur labyrinten skulle kunna se ut såhär:

```python
gå_framåt(2)
sväng_höger()
gå_framåt(3)
sväng_höger() 
sväng_höger() 
sväng_höger()
gå_framåt(2)
sväng_höger() 
sväng_höger() 
sväng_höger()
gå_framåt(4) 
sväng_höger()
gå_framåt(2)
```

Onödigt mycket `sväng_höger()`, speciellt om det är en lång labyrint. Du måste dessutom vara säker på att du svänger exakt tre gånger varje gång du ska svänga vänster. Istället kan du definiera en funktion `sväng_vänster()` och använda en loop för att svänga höger tre gånger.

```python
def sväng_vänster():
	for _ in range(3):
		sväng_höger()

gå_framåt(2)
sväng_höger()
gå_framåt(3)
sväng_vänster()
gå_framåt(2)
sväng_vänster()
gå_framåt(4) 
sväng_höger()
gå_framåt(2)
```

Koden blir lättare att läsa och du riskerar inte att råka svänga för mycket eller lite. 

`for _ in range(3):` betyder att koden i loopen upprepas 3 gånger. Eftersom du inte behöver en variabel i loopen kan du använda understreck (`_`). Tänk på att koden som hör till loopen (`sväng_höger()`) också är *indenterad*!

#### Uppgift
Gör en funktion som kan hurra för dig på din födelsedag. Den ska heta `hurra` och ska skriva ut 

```python
Hipp hipp 
hurra!
hurra!
hurra!
``` 

på skärmen. Använd en loop för att slippa skriva samma sak flera gånger. Du har fått en början, kolla till vänster på skärmen.