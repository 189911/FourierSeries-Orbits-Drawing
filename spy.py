# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 02:45:51 2020

@author: renec
"""
import pygame,sys
import random
import time
import os
import math
import cmath
from math import pi
import numpy as np
import io as op
reloj = pygame.time.Clock()

"""------------This directory must be changed------- Use \\ instead \ """ 
coordenadas="C:\\Users\\renec\\OneDrive\\Documentos\\Ptos.txt" 

#------In the next lines I am reading the information------------------
#------of the file made by mathematica, becouse i could---------------
#------could not change the format directly from Mathematica.---------
with open(coordenadas) as coor:
    lines=coor.readlines()
Num_puntos=len(lines)
print(Num_puntos)
lista2=[]
print(lines[1][1:-2])
for i in range(len(lines)):
    for f in range(len(lines[i])):
        if lines[i][f]==",":
            a=f
             
    lista2.append([lines[i][1:a-1],lines[i][a+1:-2]])
a=open("Ptos2.txt","w")
for i in range(Num_puntos):
    a.write(lista2[i][0]+" "+lista2[i][1]+"\n")
a.close()

text=np.loadtxt("Ptos2.txt")

def distanciaprom(text,N):
    sum=0
    for i in range(N-1):
        sum=sum+((text[i,0]-text[i+1,0])**2+(text[i,1]-text[i+1,1])**2)**(1/2)
    return sum/(N)

#--------------------------------------------------------------------------------------    
    
    
os.environ["SDL_VIDEO_CENTERED"]='1'
pygame.init()


#pygame configurations
width,height = 1000, 650
fps= 60
pygame.display.set_caption("Rene Series")
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
 
#colors
white = (230, 230, 230)
black = (28, 28, 28)
gray = (100, 100, 100)
green = (54, 255, 141)
gray2 = (80, 80,100)
yellow = (255, 255, 0)
screen.fill(white)
#incialisamos el tiempo
def func(t,text,ht):
    a=int(t/ht)
    f=complex(-text[a,0],text[a,1])
    return f
def integrar(t,L,ht,n):
    integral=0
    while t<=L:
        integral=integral+func(t,text,ht)*complex(math.cos(-2*pi*n*t/L),math.sin(-2*pi*n*t/L))*ht/L
                                                           
        t+=ht
    return integral

#---------------------------------------------------------------------
#----------------------------------------------------------------------
#datos de la funcion

#-------------------
i=0
t=0 #variable de tiempo
L=3*pi #periodo
vec_Num=400 #numero de vectores
ht=L/Num_puntos
lista=[]
n=int((vec_Num-1)/2)
i=-n
ind=0
while i<=n:
    lista.append(integrar(t,L,ht,i))
    ind+=1
    t=0
    i+=1
print(lista[n])


t=0

x=500
y=325

esca=-2

#------------------Esta es la parte en donde empezamos a editar plasmar en imagen cada-----------------
index=1
historial=[]
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    #color de fondo---
    screen.fill(black)
    ######-----------Drawing zone-------------
    
    for f in range(n,vec_Num-1):
        u=abs(esca)*abs(lista[f])
        if f==n:
            s=f-n
            pygame.draw.circle(screen,white,(x, y),abs(esca)*abs(lista[f]),width=1)
            pygame.draw.aaline(screen, white,(x, y),(esca*abs(lista[f])*math.cos(s*2*pi*t/L+cmath.phase(lista[f]))+x,esca*abs(lista[f])*math.sin(s*2*pi*t/L+cmath.phase(lista[f]))+y), 1)
            
        else:
            s=-int(abs(n-f))
            pygame.draw.circle(screen,white,(x, y),abs(esca)*abs(lista[n+s]),width=1)
            pygame.draw.aaline(screen, white,(x, y),(esca*abs(lista[n+s])*math.cos(s*2*pi*t/L+cmath.phase(lista[n+s]))+x,esca*abs(lista[n+s])*math.sin(s*2*pi*t/L+cmath.phase(lista[n+s]))+y), 1)
            x=esca*abs(lista[n+s])*math.cos(s*2*pi*t/L+cmath.phase(lista[n+s]))+x
            y=esca*abs(lista[n+s])*math.sin(s*2*pi*t/L+cmath.phase(lista[n+s]))+y
            s=int(f-n)

            pygame.draw.circle(screen,white,(x, y),abs(esca)*abs(lista[f]),width=1)
            pygame.draw.aaline(screen,white,(x, y),(esca*abs(lista[f])*math.cos(s*2*pi*t/L+cmath.phase(lista[f]))+x,esca*abs(lista[f])*math.sin(s*2*pi*t/L+cmath.phase(lista[f]))+y), 1)
        x=esca*abs(lista[f])*math.cos(s*2*pi*t/L+cmath.phase(lista[f]))+x
        y=esca*abs(lista[f])*math.sin(s*2*pi*t/L+cmath.phase(lista[f]))+y
    ######-----------zona de dibujo--------------
    #---Se actualiza la pantalla--
    historial.append((x,y))
    if index>1:
        for u in range(1,index): 
            pygame.draw.aaline(screen,yellow,historial[u-1],historial[u],1)

    index+=1
    t+=0.01
    x=500
    y=325
    pygame.display.update()
    reloj.tick(100)

pygame.quit()         
        
        

