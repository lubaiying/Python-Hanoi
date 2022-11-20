#partie A
#1
def init(n):
  lst_plateau=[[],[],[]]
  for i in range(n,-1,-1):
    lst_plateau[0].append(i)
  lst_plateau[0].pop(n)
  return lst_plateau
#2
import math
def nombre_disque(plateau,numtour):
    a=plateau[numtour]
    numdisque=len(a)
    return numdisque
#3
def disque_superieur(plateau,numtour):
  if len(plateau[int(numtour)])==0:
    return -1
  else:
    lst=[]
    for i in plateau[int(numtour)]:
      if i>numtour:
        lst.append(str(i))
    return (",".join(lst))
#4
def position_disque(plateau,numdisque):
    if numdisque in plateau[0]:
        a=0
    elif numdisque in plateau[1]:
        a=1
    elif numdisque in plateau[2]:
        a=2
    return a
#5
def verifier_deplacement(plateau,nt1,nt2):
  if len(plateau[nt1])!=0:
    if len(plateau[nt2])==0:
      return True
    else:
      tour2_contenu=disque_superieur(plateau,nt2)
      tour2_contenu=tour2_contenu.replace(',','')
      if int(min(plateau[nt1]))<int(min(tour2_contenu)):
        return True
      else:
        return False
  else:
    return False
#6
def verifier_victoir(plateau,n):
    res=True
    a=len(plateau[0])+len(plateau[1])
    b=len(plateau[2])
    if b!=n or a!=0 :
        res=False
    if res:
        for i in range(b-1):
            if plateau[2][i]>plateau[2][i+1]:
                res=True
            else:
                res=False
    return res
#Partie B


#1
def returne_origine():
  t.up()
  t.pensize(1.5)
  t.speed(100)
  t.goto(-300,-200)
  t.down()
def text(n):
  t.up()
  t.pencolor("black")
  t.goto(-300+(((((40+(n-1)*10)*3)+100)/2)-(((40+(n-1)*10)*3)+100)/4),-250)
  t.fillcolor("black")
  t.begin_fill()
  for i in range(4):
    t.forward((((40+(n-1)*10)*3)+100)/2)
    t.right(90)
  t.end_fill()
  t.up()
  t.pencolor("white")
  t.pensize(3)
  t.goto((-300+(((((40+(n-1)*10)*3)+100)/2)-(((40+(n-1)*10)*3)+100)/4))+(((((40+(n-1)*10)*3)+100)/2)/3),-250-((((40+(n-1)*10)*3)+100)/2)/3)
  t.write("Projet Hanota\nXIN kai et Xu sicong")
  returne_origine()
  
def dessine_plateau(n):
  def tour_bas():
      returne_origine()
      t.forward(((40+(n-1)*10)*3)+100)
      # 60 pour changer espace entre deux disque.
      t.right(90)
      t.forward(20)
      t.right(90)
      t.forward(((40+(n-1)*10)*3)+100)
      t.right(90)
      t.forward(20)
  tour_bas()
  def tour(x):
      returne_origine()
      t.up()
      t.right(90)
      t.forward((((((40+(n-1)*10)*3)+100)/4)*x)-5)
      t.down()
      t.left(90)
      t.forward((n*20)+20)
      t.right(90)
      t.forward(10)
      t.right(90)
      t.forward((n*20)+20)
      t.right(180)
  tour(1)
  tour(2)
  tour(3)
  returne_origine()

#2
def dessine_disque(nd,plateau,n):
  returne_origine()
  dessine_plateau(n)
  a=position_disque(plateau,nd)+1
  t.up()
  t.right(90)
  t.forward((((((40+(n-1)*10)*3)+100)/4)*a)-((40+(nd-1)*10)/2))
  t.left(90)
  t.forward(((n*20))-(nd*20))
  t.right(90)
  t.down()
  t.left(90)
  t.forward(20)
  t.right(90)
  t.forward(40+(nd-1)*10)
  t.right(90)
  t.forward(20)
  t.right(90)
  t.forward(40+(nd-1)*10)
  t.right(180)
  
#3  
def efface_disque(nd,plateau,n):
  returne_origine()
  dessine_plateau(n)
  t.pencolor("white")
  a=position_disque(plateau,nd)+1
  t.up()
  t.right(90)
  t.forward((((((40+(n-1)*10)*3)+100)/4)*a)-((40+(nd-1)*10)/2))
  t.left(90)
  t.forward(((n*20))-(nd*20))
  t.right(90)
  t.down()
  t.left(90)
  t.forward(20)
  t.right(90)
  t.forward(40+(nd-1)*10)
  t.right(90)
  t.forward(20)
  t.right(90)
  t.forward(40+(nd-1)*10)
  t.pencolor("black")
  t.right(180)
  dessine_plateau(n)
  t.right(90)

  
#4
def dessine_config(plateau, n):
  for i in plateau:
    if len(i)!=0:
      for j in i:
        dessine_disque(j,plateau,n)
        
#5 
def efface_tout(plateau,n):
  for i in plateau:
    if len(i)!=0:
      for j in i:
        efface_disque(j,plateau,n)
#partie C

#1
def lire_coords(plateau):
    a=int(input("depart?"))
    while True:
        if a==-1:
            c=input("abandonner?")
            if c=="o":
                
                return []
                break
            while c=="n":
                c=""
                a=int(input("depart?"))
        elif not(a>=0 and a<=2):
            a=int(input("depart?"))
        elif a>=0 and a<=2:
            if len(plateau[a])==0:
                print("vide")
                a=int(input("depart?"))
            else:
                b=int(input("arrive?"))
                if not(b>=0 and b<=2):
                    b=int(input("arrive?"))
                else:
                    if len(plateau[b])!=0 and plateau[b][-1]<plateau[a][-1]:
                        print("grand")
                    
                    elif len(plateau[b])==0 or (len(plateau[b])!=0 and plateau[b][-1]>=plateau[a][-1]):
                        print("deplace de",a,"a",b)
                        return [a,b]
                        break

#2
def jouer_un_coup(plateau,n):
    n_t=lire_coords #list[depart,arrive]
    t_d=n_t[0]
    t_a=n_t[1]
    numtour=t_d
    nd=int(min(plateau[t_d]))
    efface_disque(nd,plateau,n)
    plateau[t_d].remove(nd)
    plateau[t_a].append(nd)
    dessine_disque(nd,plateau.n)
    print(plateau)
    return plateau
    
#3
"""
def boucle_jeu(plateau,n):
  limite_fois=int((2**n)+(n/2))
  fois_instant=0
  while (verifier_victoir(plateau,n)!=True)or(fois_instant<=limite_fois):
    lire_coords(plateau)
    fois_instant+=1
  if fois_instant>limite_fois:
    if verifier_victoir(plateau,n)!=True:
      res=("Vous avez gagne !\nAurevoir")
    else:
      res=("Perdu, trop de coupe !\nAurevoir")
  elif fois_instant<=limite_fois:
    if verifier_victoir(plateau,n)!=True:
      res="Vous avez gagne !\nAurevoir"
    else:
      res=("Abandon de la partie apres ",fois_instant-1," coups.\nAurevoir")
  return res
"""
#3
def boucle_jeu(plateau,n):
    coup_limite=int((2**n)+(n/2))
    coup_joue=1
    v=verifier_victoir(plateau,n)
    l=len(lire_coords(plateau))
    while True:
        if coup_joue<coup_limite and v==False:
            if l!=0:
                lire_coords(plateau)
                jouer_un_coup(plateau,n)
                coup_joue+=1
                v=v and verifier_victoir(plateau,n)
            elif l==0:
                print("abandon de la partie apres",coup_joue,"coups.")
                break
        if coup_jour==coup_limite:
            print("Perdu, trop de coupe !")
            break
        if v==Vrai:
            print("Vous avez gagne !")
            break
    print("Au-revoir.")
#4
plateau=[[3,2,1],[],[]]
n=3

print("Bienvenue dans les Tours de Hanoio")
n=int(input("Combien de disques?"))

lire_coords(plateau)

"""
#partie D
#2
def annuler_dernier_coup(coups,ndc):
    del dict[ndc-1]
    plateau=coups[ndc-2]
    ndc=ndc-2
#4 supprimer
#partieE
#2
if #win Condition
    nj=input("votre nom?")
    enregistre_score
#4
def localtime():
    import time
    print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    #enregistre
#6
def 

"""

























    
