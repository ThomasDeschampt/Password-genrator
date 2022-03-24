import random
caractere = ""
mdp =""

print("Combien de caractères dans votre mot de passe ?")
a = int(input())
if a == 0 :
    a = int(input())
else : 
    print("Voulez vous utlisez des majuscules et des minuscules ou seulement des minuscules ? (oui / non)")
    rep = input()
    if rep == "oui" : 
        caractere += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else : 
        caractere += "abcdefghijklmnopqrstuvwxyz"
    
    print("Voulez vous utlisez des chiffres ? (oui / non)")
    rep2 = input()
    if rep2 == "oui" : 
        caractere += "0123456789"
    
    print("Voulez vous utlisez des caractères spéciaux ? (oui / non)")
    rep3 = input()
    if rep3 == "oui":
        caractere += "@[]^!)(&}{*+,-./:;<>=|~?€#"
    
    for i in range (a) :
        mdp += random.choice(caractere)
    print(mdp)
        

print("Appuyer sur entrer pour fermer le programme")
e=input()


