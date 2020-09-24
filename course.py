import sys
import math

#Peut on passer un virage a une vitesse donnee
def testVirage(angleVirage, vitesse):
    result = 0
    angleCourreur = (vitesse*vitesse) / (angleVirage * 9.81)
    angleCourreur = math.degrees(math.atan(angleCourreur))
    if angleCourreur <= 60 :
        result = 1
    return result

def minimum(liste):
    result = 360
    for i in range(len(liste)) :
        tmp = liste[i]
        if tmp < result :
            result = tmp
    return result

def victoire(angleVirages):
    angleMax = minimum(angleVirages)
    result = 0
    angle = 60
    vitesse = 1
    while result < angle:
        result = (vitesse*vitesse) / (angleMax * 9.81)
        result = math.degrees(math.atan(result))
        vitesse = vitesse + 1
    vitesse = vitesse - 2
    return vitesse

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

#Declarations des variables
nbParticipants = int(input())
nbVirages = int(input())

#Tableaux
vitesseParticipants = nbParticipants*[0]
nomParticipant = 'a'
angleVirages = nbVirages*[0]
#remplissage des tableaux
for i in range(nbParticipants):
    speed = int(input())
    vitesseParticipants[i] = speed
for i in range(nbVirages):
    bends = int(input())
    angleVirages[i]=bends

#Traitement
maVictoire = victoire (angleVirages)
print (maVictoire)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)