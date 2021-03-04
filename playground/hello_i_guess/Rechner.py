#Klassen mit Methoden
class Normal():
    def Add(self, Num):
        for i in range(len(Num)-1):
            Num2 = Num[i] + Num[i+1]
        print(Num2)
    
    def Sub(self, Num):
        for i in range(len(Num)-1):
            Num2 = Num[i] - Num[i+1]
        print(Num2)

    def Mul(self, Num):
        for i in range(len(Num)-1):
            Num2 = Num[i] * Num[i+1]
        print(Num2)

    def Div(self, Num):
        for i in range(len(Num)-1):
            Num2 = Num[i] / Num[i+1]
        print(Num2)

#Objekte der Klassen erzeugen
Normal = Normal()

#Eingabe der Operation
OpStr = input("Term: ")
#print(OpStr)

if OpStr.find('+'):
    Num = OpStr.split('+')
else:
    if OpStr.find('-'):
        Num = OpStr.split('-')
    else:
        if OpStr.find('*'):
            Num = OpStr.split('*')
        else:
            if OpStr.find('/'):
                Num = OpStr.split('/')
            else:
                print("Ungültiges Rechenzeichen.")

#print(Num)
Num = [int(x) for x in Num]
#print(Num)

#Wahl der Korrekten Methode
if OpStr.find("+"):
    Normal.Add(Num)
else:
    if OpStr.find("-"):
        Normal.Sub(Num)
    else:
        if OpStr.find("*"):
            Normal.Mul(Num)
        else:
            if OpStr.find("/"):
                Normal.Div(Num)
            else:
                print("Nicht unterstützt.")