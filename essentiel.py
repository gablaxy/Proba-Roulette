import numpy as np
import numpy.random as rd


def tirage_num(n): # renvoie une liste de n nombres tirés aléatoirement entre 0 et 36
    return rd.randint(0, 36, n)

def rouge_noir(nb): # detecte si un nb correcpond à une case rouge, noir ou verte
    rouge = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    noir = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    if nb in rouge:
        return 1
    elif nb in noir:
        return 2
    else:
        return 0

def tiers(nb): # renvoie le tiers auquel appartient le nombre
    tiers_1 = [3,6,9,12,15,18,21,24,27,30,33,36]
    tiers_2 = [2,5,8,11,14,17,20,23,26,29,32,35]
    tiers_3 = [1,4,7,10,13,16,19,22,25,28,31,34]
    
    if nb in tiers_1:
        return 1
    elif nb in tiers_2:
        return 2
    elif nb in tiers_3:
        return 3
    else:
        return 0

def pair_impair(nb): # renvoie 0 si pair et 1 si impair
    if nb % 2 == 0:
        return 0
    else:
        return 1
    
def victoire_pair_rouge(nb, argent): # on considère que l'on joue à chaque partie 1€ sur rouge et 1€ sur pair
    argent -= 2
    if(rouge_noir(nb) == 1 and pair_impair(nb) == 0):
        argent += 4
    elif(rouge_noir(nb) == 1):
        argent += 2
    elif(pair_impair(nb) == 0):
        argent += 2
    if(pair_impair(nb) == 1 and rouge_noir(nb) == 2 ):
        argent += 0
        
    return argent

def victoire_tiers(nb, argent): # on regarde si on tombe sur un nombre qui appartient à un des tiers sur lesquels on a misé
    argent -= 2
    if(tiers(nb) == 1 or tiers(nb) == 2): # on considère que l'on joue à chaque partie 1€ sur le tiers 1 et 1€ sur le tiers 2
        argent += 3
        
    return argent


def partie(cashin,tirage): # joue un tour de roulette et renvoie l'argent restant
    # cashin = prix auquel on veut stopper la partie, tirage = nombre de tirage par partie 
    argent_base = 10
    maximum = argent_base
    
    for i in tirage_num(tirage): 
        if(argent_base > 0 and argent_base < cashin): # on vérifie que l'on a de l'argent et que l'on ne dépasse pas le cashin
            argent_base = victoire_tiers(i, argent_base)
            if(argent_base > maximum):
                maximum = argent_base
                
        else: # sinon on arrête la partie
            break
    return argent_base

def npartie_return_argent(n,cashin, tirage): # comme au dessus mais renvoie la liste de l'argent restant à la fin de chaque partie comprenant x(tirage) tirages
    liste = [] 
    for i in range(n):
        argent_base = 10
        for i in tirage_num(tirage):
            if(argent_base > 0 and argent_base < cashin):
                argent_base = victoire_tiers(i, argent_base)
            else:
                break
        liste.append(argent_base)
    return liste
    
def npartie(n,cashin,tirage): # n = nombre de partie que l'on veut faire, cashin = prix auquel on veut stopper la partie, tirage = nombre de tirage par partie
    nb = 0
    gagnee = 0
    perdue = 0
    autre = 0
    for y in range(n):
        nb = partie(cashin,tirage)
        if(nb == cashin):
            gagnee += 1
        elif(nb > 0 and nb < cashin):
            autre += 1
        elif(nb == 0):
            perdue += 1
    return gagnee, perdue, autre



