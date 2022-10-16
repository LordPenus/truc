#modules
from tkinter import *
from random import randint
from time import sleep

from lemmings_class import *

#creation de la fenetre
Mafenetre=Tk()
Mafenetre.geometry('550x550')
#zone de dessin
can1=Canvas(Mafenetre,bg="white",width=600,height=600)
can1.place(x=0,y=0)
# =============================================================================
# creation d'un niveau : images - matrice - dictionnaire
# =============================================================================
casesol=PhotoImage(file="sol.gif")
casemur2=PhotoImage(file="mur2.gif")
casemur=PhotoImage(file="mur.gif")
casesortie=PhotoImage(file="sortie.gif")
Lem_droite=PhotoImage(file="marioD.gif")
Lem_gauche=PhotoImage(file="marioG.gif")
#astuce : les cases de sortie sont toujours nommées S
L1=["MX","C","C","C","C","C","C","C","C","C","MX"]
L0=["MX","C","C","C","C","C","C","C","C","C","MX"]
L2=["MX","C","MX","C","C","C","C","C","C","C","MX"]
L3=["MX","C","C","C","C","C","C","C","C","C","MX"]
L4=["MX","C","C","C","C","C","C","C","C","C","MX"]
L5=["MX","MX","C","C","PX","C","C","C","MX","C","MX"]
L6=["MX","MX","C","PX","PX","C","C","C","C","C","MX"]
L7=["MX","C","C","C","PX","C","C","C","C","PX","PX"]
L8=["MX","C","MX","C","C","C","C","C","C","C","MX"]
L9=["MX","S","MX","MX","PX","C","C","C","S","MX","MX"]
L10=["MX","MX","C","C","PX","C","C","C","MX","C","MX"]
L11=["MX","MX","C","PX","PX","C","C","C","C","C","MX"]
L12=["MX","C","C","C","PX","C","C","C","C","PX","PX"]
L13=["MX","C","MX","C","C","C","C","C","C""C","MX"]
L14=["MX","S","MX","MX","PX","S","C","C","C","MX","MX"]
ma_matrice=[L0,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14]

dico={"C":casesol,"PX":casemur2,"MX":casemur,"S":casesortie}


niveau1 = Jeu(ma_matrice,dico,can1,["MX","PX"])
niveau1.dessine_matrice()
perso1 = Personnage(niveau1,4,3,0,Lem_droite,Lem_gauche)
perso1.affiche_lem()
niveau1.ajoute_liste_perso(perso1)
perso2 = Personnage(niveau1,1,1,1,Lem_droite,Lem_gauche)
perso2.affiche_lem()
niveau1.ajoute_liste_perso(perso2)

def deplace(perso):
    """deplace un perso en suivant les règles du jeu lemmings"""
    
    if niveau1.get_nature_case_dessous(perso) == True :
        niveau1.changement_nature_case(perso)
        perso.deplace_bas()
        niveau1.changement_nature_case(perso)
        #sinon si la direction est a droite
    elif perso.get_direction() == 0 and niveau1.get_nature_case_droite(perso) == True :
        niveau1.changement_nature_case(perso)
        perso.deplace_droite()
        niveau1.changement_nature_case(perso)
    elif perso.get_direction() == 0 and niveau1.get_nature_case_gauche(perso) == True :    
        niveau1.changement_nature_case(perso)
        perso.deplace_gauche()
        niveau1.changement_nature_case(perso)
    
           
                
#boucle du jeu qui finit par Mafenetre.update()
while niveau1.get_liste_perso() != []:
    sleep(0.5)
    for elt in niveau1.get_liste_perso() :
        deplace(elt)
        
    Mafenetre.update()

        
#lancement de la boucle tkinter       
Mafenetre.mainloop()

        