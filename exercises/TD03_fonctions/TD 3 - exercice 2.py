def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    secondes = temps [3] + 60*temps[2] + 3600*temps[1] + 24*3600 *temps[0]   
    return (secondes)  

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   




def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jour = seconde // (24*3600)
    heure = (seconde % (24*3600))//3600
    minute = ((seconde %(24*3600))% 3600) //60
    secondes = ((seconde % (24*3600)) % 3600) % 60
    return(jour, heure, minute, secondes)

temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")


 #temps = ensemble de temps 
 # print(secondes)


def affichePluriel (nombre, mot) :
    '''affiche le nombre puis le mot en mettant éventuellement le mot au pluriel, n'affiche rien si nombre=0 '''
    if nombre > 1 :
        print (nombre, mot + 's', end=" ")
    elif nombre == 1 :
         print(nombre, mot, end=" ")

def afficheTemps (temps): 
    ''' affichage de temps'''
    affichePluriel (temps[0], "jour")
    affichePluriel (temps[1], "heure")
    affichePluriel (temps[2], "minute")
    affichePluriel (temps[3], "seconde")
    print()
   
print(afficheTemps((2,1,0,8)))
   
def demandeTemps ():
    '''saisie d'un temps avec vérification de la validité'''
    jour = int(input("choisir un nombre"))
    if jour<0 :
         print ("saisie invalide")
         return
    heure = int(input("nombre d'heure "))
    if not 0<= heure<= 23 :
                        print('saisie invalide')
                        return
    minute = int(input("nombre de minute"))
    if not 0<= minute <= 59 :
        print ('saisie invalide')
        return
    seconde = int(input("nombre de seconde"))
    if not 0<= seconde <= 59 :
        print ('saisie invalide') 
        return    
    return (jour, heure, minute, seconde)
    
afficheTemps(demandeTemps()) 



def sommeTemps(temps1,temps2):
    seconde1 = tempsEnSeconde(temps1)
    seconde2 = tempsEnSeconde(temps2)
    seconde = seconde1 + seconde2
    return secondeEnTemps(seconde)
print(sommeTemps((0,21,27,30),(0,3,59,45)))
    





   




    


    

