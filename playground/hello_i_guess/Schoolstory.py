#Importieren aller nötigen Dinge
from random import randint

#Definition der Klasse und Methoden
class narrator():
    def k(self, text):
        print("Kind:   " + text)

    def m(self, text):
        print("Mutter: " + text)

    def l(self,text):
        print("Lehrer: " + text)
    
    def n(self, text):
        print(text.center(2*3 + len(text), '-'))
    
    def i(self, text):
        text = "        " + text
        return text

    def o(self):
        print("")
    
    def tag(self, tag):
        narrator.o()
        narrator.n(("Tag " + str(tag)))
        tag += 1

#Objekt der Klasse erzeugen
narrator = narrator()

#Deklaration nötiger Variablen
tag = 1
erfolg = 0
Fehler = True
Fächer = ['Mathe', 'Deutsch', 'Englisch', 'Biologie', 'Geschichte', 'Informatik']
Fach = ""
i = 1

#-------------------------------------------------------------------------------------------------

#Einführung
narrator.n("Willkommem bei Logik-Schule - Der interaktive Programmier-Lehrnspaß für groß und klein!")
narrator.n("Wähle zunächst bitte einen Schwierigkeitsgrad und ein Fach.")

#Level
narrator.o()
while Fehler == True:
    lvl = input((narrator.i("Schwierigkeitsstufe (1 bis 5): ")))
    lvl = int(lvl)
    if 1 <= lvl <= 5:
        Fehler = False
    else:    
        print(narrator.i("Wähle eine ganze Zahl zwischen 1 und 5!"))
        Fehler = True
Fehler = True

#Fach
narrator.o()
narrator.n("Wähle nun das Fach. Es stehen folgende Fächer zur Auswahl:")
for Fach in Fächer:
    print(narrator.i(" - " + Fach + " (" + str(i) + ")"))
    i += 1
Fach = Fächer[int(input(narrator.i("Fach: "))) - 1]
print(narrator.i(Fach))
narrator.o()

narrator.n("Super! Jetzt kann es losgehen.")

#Lernen?
while Fehler == True:
    for tag in range(1, 7 - lvl):
        narrator.tag(tag)
        narrator.n(("Du schreibst in " + str(7 - lvl) + " Tagen eine Arbeit."))
        narrator.o()
        d = input(narrator.i("Möchtest du lernen (1) oder prokrastinieren (0)? "))
        if d == '0':
            narrator.k("Ich sollte langsam wirklich lernen, wir schreiben eine Arbeit.")
            narrator.o()
            Fehler = False
            tag += 1
        elif d == '1':
            narrator.k("Ich fühle mich gut, da ich für die Arbeit immer besser vorbereitet bin.")
            narrator.o()
            erfolg += 1
            narrator.n("Deine Erfolgswahrscheinlichkeit ist um 1 gestiegen, glückwunsch!")
            narrator.n("Sie beträgt jetzt " + str(erfolg) + ".")
            Fehler = False
            tag += 1
        else:
            Fehler = True
Fehler = True

#Arbeit geschrieben
narrator.tag(tag)
narrator.k("Mama, wir haben heute eine Arbeit geschrieben.")
narrator.m("In welchem Fach?")
narrator.k(str("In " + Fach + "."))
narrator.m("Und, was sagt dein Bauchgefühl?")
if erfolg <= 1:
    narrator.k("Naja, geht so.")
else:
    narrator.k("Joa, ganz gut.")

tag += 1
narrator.tag(tag)
#Notenvergabe
if 1 < erfolg < 4:
    note = randint(1,4)
elif 4 <= erfolg:
    note = randint(1,3)
elif erfolg <= 1:
    note = randint(3, 6)
narrator.k("Mama, ich habe heute eine " + str(note) + " bekommen.")

#Reaktion der Mutter
if note == 1:
    e = "Aha."
elif note == 2:
    e = "Schön!"
elif note == 3:
    e = "Immerhin."
elif note == 4:
    e = "Naja."
elif note == 5:
    e = "Was?!"
    e.upper()
elif note == 6:
    e = "Oh Gott!"
    e.upper()
narrator.m(e)

if note <= 3 and 0 <= erfolg < 3:
    narrator.m("Glück gehabt! :)")

#'Ausbesserung'
if note > 3 and erfolg > 1 or note > 4:
    narrator.m("Daran müssen wir was ändern!")
    
    narrator.o()
    geld = input(narrator.i("Wie viel Geld soll der Lehrer bekommen? "))

    try:
        geld = int(geld)
    except ValueError:
        geld = input(narrator.i("Wie viel Geld soll der Lehrer bekommen? "))
    geld = int(geld)     
    geld2 = geld
    note2 = note
    
    tag += 1
    narrator.tag(tag)
    narrator.k("Bitte ändern Sie meine Note. Hier haben Sie " + str(geld) + "€.")
    while geld >= 20 and note > 1:
        note -= 1
        geld -= 10
    
    if note == note2:
        narrator.l("Damit brauchst du mir nicht ankommen!")
    else:
        narrator.l("Sehr schön, " + str(geld2) + "€! Damit hast du dir die " + str(note) + " wirklich verdient!")

        narrator.m("Mama, der Lehrer hat die Note geändert!")
        narrator.m("Echt? Zeig mal.")
        if note == 1:
            e = "sehr schön!"
        elif note == 2:
            e = "das hört sich doch schonmal besser an!"
        elif note == note2:
            e = "das verstehe ich jetzt nicht. Was hat der denn gesagt?"
        else:
            e = "schön."
        narrator.m("Oh! Eine " + str(note) + ", " + e)
        if note == note2:
            narrator.k("'Damit brauchst du mir nicht ankommen!'")