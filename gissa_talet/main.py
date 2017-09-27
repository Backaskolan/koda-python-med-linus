import random

rekord = 0

def setup():
  talet = random.randint(1, 100)
  antal_gissningar = 1
  q(talet, antal_gissningar)

def q(talet, antal_gissningar):
    gissning = input('Jag tänker på ett tal mellan 1 och 100, gissa vilket!\n:')
    loop(talet, antal_gissningar, gissning)

def loop(talet, antal_gissningar, gissning):
  global rekord
  while int(gissning) != talet:
    if talet < int(gissning):
      print('Nej, det är lägre')
      antal_gissningar += 1
      q(talet, antal_gissningar)
    elif talet > int(gissning):
      print('Nej det är högre')
      antal_gissningar += 1
      q(talet, antal_gissningar)
  print('Det var rätt, du behövde {0} gissningar'.format(antal_gissningar))
  if rekord == 0 or antal_gissningar < rekord:
    rekord = antal_gissningar
  spela_igen = input("Vill du spela igen (J/n)? ")
  if spela_igen != 'n':
    setup()
  else:
    print('Tack för att du spelade! Ditt rekord var {0} gissningar.'.format(rekord))
    exit()

setup()