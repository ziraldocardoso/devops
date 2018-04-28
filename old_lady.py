m = 0
n = 0
numero_total = 7
animal = list()
quantidade = list()

print ("Indique 7 (sete) animais: ")
for j in range(int(numero_total)):
    m = input("%s" %animal + ":")
    animal.append(m)

print ("Indique a quantidade desejada de cada animal: ")
for i in range(int(numero_total)):
    n = int(input("%s" %animal[i] + ":"))
    if 0 < n < 21:
      quantidade.append(int(n))
    else:
      print ("Escolha um número entre 1 e 20")
      break

musica = (" "+"There was an old lady who swallowed %d %s" %(quantidade[0], animal[0]) + ".\n "
+ "I don't know why she swallowed %d %s" %(quantidade[0], animal[0]) + " - perhaps she'll die!\n "
"#----------------------------------#\n "
+ "There was an old lady who swallowed %d %s" %(quantidade[1], animal[1]) + ";\n "
+ "That wriggled and wiggled and tickled inside her.\n "
+ "She swallowed %d %s" %(quantidade[1], animal[1]) + " to catch %d %s" %(quantidade[0], animal[0]) + ";\n "
+ "I don't know why she swallowed a fly - perhaps she'll die!\n "
"#----------------------------------#\n "
+ "There was an old lady who swallowed %d %s" %(quantidade[2], animal[2]) + ";\n "
+ "How absurd to swallow %d %s" %(quantidade[2], animal[2]) + ".\n "
+ "She swallowed %d %s" %(quantidade[2], animal[2]) + " to catch %d %s" %(quantidade[1], animal[1]) + ";\n "
+ "She swallowed %d %s" %(quantidade[1], animal[1]) + " to catch %d %s" %(quantidade[0], animal[0]) + ";\n "
+ "I don't know why she swallowed %d %s" %(quantidade[0], animal[0]) + " - perhaps she'll die!\n "
"#----------------------------------#\n "
+ "There was an old lady who swallowed %d %s" %(quantidade[3], animal[3]) + ";\n "
+ "Fancy that to swallow %d %s" %(quantidade[3], animal[3]) + "!\n "
+ "She swallowed %d %s" %(quantidade[3], animal[3]) + " to catch %d %s" %(quantidade[2], animal[2]) + ";\n "
+ "She swallowed %d %s" %(quantidade[2], animal[2]) + " to catch %d %s" %(quantidade[1], animal[1]) + ";\n "
+ "She swallowed %d %s" %(quantidade[1], animal[1]) + " to catch %d %s" %(quantidade[0], animal[0]) + ";\n "
+ "I don't know why she swallowed %d %s" %(quantidade[0], animal[0]) + " - perhaps she'll die!\n "
"#----------------------------------#\n "
+ "There was an old lady who swallowed %d %s" %(quantidade[4], animal[4]) + ";\n "
+ "What a hog, to swallow %d %s" %(quantidade[4], animal[4]) + "!\n "
+ "She swallowed %d %s" %(quantidade[4], animal[4]) + " to catch %d %s" %(quantidade[3], animal[3]) + ";\n "
+ "She swallowed %d %s" %(quantidade[3], animal[3]) + " to catch %d %s" %(quantidade[2], animal[2]) + ";\n "
+ "She swallowed %d %s" %(quantidade[2], animal[2]) + " to catch %d %s" %(quantidade[1], animal[1]) + ";\n "
+ "She swallowed %d %s" %(quantidade[1], animal[1]) + " to catch %d %s" %(quantidade[0], animal[0]) + ";\n "
+ "I don't know why she swallowed %d %s" %(quantidade[0], animal[0]) + " - perhaps she'll die!\n "
"#----------------------------------#\n "
+ "There was an old lady who swallowed %d %s" %(quantidade[5], animal[5]) + ";\n "
+ "She swallowed %d %s" %(quantidade[5], animal[5]) + " to catch %d %s" %(quantidade[4], animal[4]) + ";\n "
+ "She swallowed %d %s" %(quantidade[4], animal[4]) + " to catch %d %s" %(quantidade[3], animal[3]) + ";\n "
+ "She swallowed %d %s" %(quantidade[3], animal[3]) + " to catch %d %s" %(quantidade[2], animal[2]) + ";\n "
+ "She swallowed %d %s" %(quantidade[2], animal[2]) + " to catch %d %s" %(quantidade[1], animal[1]) + ";\n "
+ "She swallowed %d %s" %(quantidade[1], animal[1]) + " to catch %d %s" %(quantidade[0], animal[0]) + ";\n "
+ "I don't know why she swallowed %d %s" %(quantidade[0], animal[0]) + " - perhaps she'll die!\n "
"#----------------------------------#\n "
+ "There was an old lady who swallowed %d %s" %(quantidade[6], animal[6]) + ";\n "
+ "...She's dead, of course!")

print (musica)
