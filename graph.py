# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 01:39:12 2022

@author: HP
"""

# -*- coding: utf-8 -*-
"""
@author: KONE Siriky Youssouf
"""
# Importer les librairies
import mpld3
import math
import numpy as np
import matplotlib 
matplotlib.use("TkAgg")

from matplotlib.figure import Figure

global L0, L1, L2, O1, O2, XB, YB, SO1, CO1, nbrePas, nbreMaxPas, X_Pi, Y_Pi,canvas,largeur,hauteur,pointA,absA,ordA,XA0,YA0

XA0=0
YA0=0
nbrePas=0
X_Pi = []
Y_Pi = []


# Fonction Model Geometrik Direct
def calcul(l0, l1, l2, o1, o2, xb, yb, nbpas, temp):
    
    L0 = int(l0)
    L1 = int(l1)
    L2 = int(l2)
    O1 = math.radians(o1)
    O2 = math.radians(o2)
    nbrePas = int(nbpas)
    YB = int(yb)
    XB = int(xb)
    temps = int(temp)

    #LES MATRICES DE PASSAGE DIRECTE
    Mat0T1 = np.array([[math.cos(O1),-math.sin(O1),0,L0],[math.sin(O1),math.cos(O1),0,0],[0,0,1,0],[0,0,0,1]])
    Mat1T2 = np.array([[math.cos(O2),-math.sin(O2),0,L1],[math.sin(O2),math.cos(O2),0,0],[0,0,1,0],[0,0,0,1]])
    Mat0T2 = Mat0T1.dot(Mat1T2)
    print(Mat0T1) # --> debug
    A2=np.array([[L2],[0],[0],[1]]) 
    A21=np.array([[L1],[0],[0],[1]]) 
    A0 = Mat0T2.dot(A2)
    #Position de A2 dans le R0
    A20 = Mat0T1.dot(A21)
    print(A20) # --> debug

    return [ L0, A20, A0, L1, L2,nbrePas,YB,XB,temps]


def inverse(x, y, l0, l1, l2,):
     
    # Cette fonction implémente le modèle géométrique inverse
    L0 = int(l0)
    L1 = int(l1)
    L2 = int(l2)
   
    B1 = -2*y*L1
    B2 = 2*L1*(L0-x)
    B3 = L2**2-y**2-(L0-x)**2-L1**2
    teta_1=0
    teta_2=0
    SO1 = 0
    CO1 = 0
    epsi = 1
    if B3==0 :
        teta_1 = math.degrees(math.atan2(-B2,B1))
    else:
        if ((B1**2+B2**2-B3**2)>=0) :
            SO1 = (B3*B1+epsi*B2*math.sqrt(B1**2+B2**2-B3**2))/(B1**2+B2**2)
            CO1 = (B3*B2-epsi*B1*math.sqrt(B1**2+B2**2-B3**2))/(B1**2+B2**2)
            teta_1 = math.degrees(math.atan2(SO1,CO1))
        
    Yn1 = L2*SO1
    Yn2 = L2*CO1
    if L2!=0 :
        teta_2 = math.degrees(math.atan2(Yn1/L2,Yn2/L2))
    print(teta_1) # --> debug
    print(teta_2) # --> debug

    return [teta_1,teta_2]

def dessiner(l0, l1, l2, o1, o2, xb, yb, nbpas, temp):
    plot.cla()
   
    result = calcul(l0, l1, l2, o1, o2, xb, yb, nbpas, temp)
    L0 = result[0]
    A20 = result[1]
    A0 = result[2]
    #YB = result[4]
    #XB = result[5]
    #nbreMaxPas = result[0]
    plot.set_xlabel('Axe Y0')
    plot.set_ylabel('Axe X0')
    plot.yaxis.set_ticks_position('right')
    plot.set_xticks(range(10))
    plot.set_yticks(range(10))
    plot.set_xlim((9,0))
    plot.set_ylim((0, 9))
    plot.grid(True)

    #tracer L0
    plot.plot([0.5,0.5],[0.0,L0],"b-",lw=7)
    #tracer L1
    plot.plot([0.5,A20[1]],[L0,A20[0]],"b-",lw=7)
    #tracer L2
    plot.plot([A20[1],A0[1]],[A20[0],A0[0]],"b-",lw=7)
    #Le point A
    plot.scatter([A0[1]], [A0[0]], s =500, color = 'red')
    #Le point B
    #plot.scatter([YB], [XB], s =500, color = 'red')
    #Les Articulations
    plot.scatter([0.5], [L0], s =500, color = 'orange')
    plot.scatter([A20[1]], [A20[0]], s =500, color = 'orange')
    #La base et le sol
    plot.plot([0.5,0.7],[0.0,0.0],"k-",lw=10)
    plot.plot([0.0,15.0],[0.0,0.0],"k--",lw=3)

    return mpld3.fig_to_html(schema, figid='graph').split('}else{')[1].split('''mpld3_load_lib("https://d3js.org/d3.v5.js", function(){
         mpld3_load_lib("https://mpld3.github.io/js/mpld3.v0.5.9.js", function(){''')[1].split(';')[0]

 
def simuler(l0, l1, l2, o1, o2, nbpas, yb, xb, temp):
    x_i = ''
    y_i = ''
    pos = []
    global X_Pi, Y_Pi
    X_Pi = []
    Y_Pi = []
    result = calcul(l0, l1, l2, o1, o2, nbpas, yb, xb, temp)
    nbrePas = result[5]
    L0 = result[0]
    L1 = result[3]
    YB = result[6]
    A0 = result[2]
    XB = result[7]
    
    for i in range(1,nbrePas+1):

        # On efface le graphe dessiné dans le cavas puis 
        # on redessine le nouveau graphe avec les mêmes 
        # caracteristiques.

        plot.cla()
        
        plot.set_xlabel('Axe Y0')
        plot.set_ylabel('Axe X0')
        plot.yaxis.set_ticks_position('right')
        plot.set_xticks(range(10))
        plot.set_yticks(range(10))
        plot.set_xlim((9,0))
        plot.set_ylim((0,9))
        plot.grid(True)
        
        # On détermine les coordonnées du point Pk

        #Distance dans la direction X
        disXPas = (XB-A0[0])/nbrePas
        if disXPas<0:
            disXPas = -disXPas

        #Distance dans la direction Y
        disYPas = (YB-A0[1])/nbrePas
        if disYPas<0:
            disYPas = -disYPas
        
        # Coordonnées du point Pk
        if XB>=A0[0] :
            Xi = A0[0]+i*disXPas
        else:
            Xi = A0[0]-i*disXPas

        if YB>A0[1]:
            Yi = A0[1]+i*disYPas
        else:
            Yi = A0[1]-i*disYPas

        # Détermination des variables articulaires théta 1 et théta 2

        theta=inverse(Xi,Yi, l0, l1, l2)
        
        # Coordonnées du point A2

        XA2i =L1*math.cos(math.radians(theta[0]))+L0
        YA2i =L1*math.sin(math.radians(theta[0]))
        
        #Trajectoire
        
        XA0 = result[2][0]
        XB = result[7]
        YA0 = result[2][1]
        YB = result[6]
        a = (YA0-YB)/(XA0-XB)
        b = YB-a*XB
        x=range(-100,101)
        y = a*x + b
         #Trace la droite
        plot.plot([YB,YA0],[XB,XA0],lw=5)
        
        #Droite entre A et Pi
        plot.plot([A0[1],Yi],[A0[0],Xi],"y-",lw=5)
        #sauvegarde les coordonnees des Pi
        X_Pi.append(Xi)
        Y_Pi.append(Yi)
        if x_i == '' :
            x_i = str(Xi[0])
            y_i = str(Yi[0])
        else :
            x_i += ' ' + str(Xi[0])
            y_i += ' ' + str(Yi[0])
        
        #Les Pas
        
        for j in range(0,len(X_Pi)) :
            plot.scatter([Y_Pi[j]], [X_Pi[j]], color = '#FF00CC')

        #tracer L0
        plot.plot([0.5,0.5],[0.0,L0],"b-",lw=7)
        #tracer L1
        plot.plot([0.5,YA2i],[L0,XA2i],"b-",lw=7)
        #tracer L2
        plot.plot([YA2i,Yi],[XA2i,Xi],"b-",lw=7)
        #Point Pi
        plot.scatter([Yi], [Xi], color = '#FF0000')
        #Point A0
        plot.scatter([0.5], [L0], s =500, color = 'black')
        #Point A2
        plot.scatter([YA2i], [XA2i], s =500, color = 'black')
        if i!=0:
            #Le point A
            plot.scatter([A0[1]], [A0[0]], s =100, color = '#006633')
        else:
            #Le point A
            plot.scatter([A0[1]], [A0[0]], s =500, color = '#FF0000')
            
        if i==nbrePas:
            #Le point B
            plot.scatter([YB], [XB], s =300, color = '#FF0000')
        else:
            #Le point B
            plot.scatter([YB], [XB], s =300, color = '#00FF33')
        
        #Le sol
        plot.plot([0.5,0.7],[0.0,0.0],"k-",lw=10)
        plot.plot([0.0,15.0],[0.0,0.0],"k--",lw=3)
        
        pos.append(mpld3.fig_to_html(schema, figid='graph').split('}else{')[1].split('''mpld3_load_lib("https://d3js.org/d3.v5.js", function(){
         mpld3_load_lib("https://mpld3.github.io/js/mpld3.v0.5.9.js", function(){''')[1].split(';')[0])
    
    return [pos, x_i, y_i]

   
# Partie construction graphique

largeur=255
hauteur=265
schema = Figure(figsize=(7.5, 7.18), dpi=35)
plot = schema.add_subplot(1, 1, 1)
plot.set_xlabel('Axe Y0')
plot.set_ylabel('Axe X0')
plot.yaxis.set_ticks_position('right')
plot.set_xticks(range(10))
plot.set_yticks(range(10))
plot.set_xlim((7,0))
plot.set_ylim((0, 9))
plot.grid(True)


# fen_simulation.mainloop()