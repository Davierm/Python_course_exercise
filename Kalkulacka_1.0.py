#   /////////////*                                                                        
#   ///////////////////                               
#   ///////////////////////                           
#   ////////////////                                  
#   ////////////    ,//////////                       
#   /////////*   ////////////////                     
#   ////////   ///////////////////                    
#   ///////  */////////////////////                   
#   //////  .//////////////////////                   
#   /////   ///////////////////////,                  
#   /////   ///////////////////////*                  
#   /////   ///////////////////////,                  
#   //////   //////////////////////                   
#   ///////  ,/////////////////////                   
#   ////////   ///////////////////                    
#   //////////   ////////////////                     
#   ////////////     //////////                       
#   ////////////////                                  
#   //////////////////////,                           
#   ///////////////////                               
#   /////////////                                     

#   DAVIERM - David Čermák
#   https://davierm.cz
#   kontakt@davierm.cz                                                                

def nacti_cislo(text_zadani, text_chyba):
    spatne = True
    while spatne:
        try:
            cislo = float(input(text_zadani))
            spatne = False
        except ValueError:
            print(text_chyba)
        else:
            return cislo
        
def dalsi_priklad():
    nezadano = True
    while nezadano:
        odpoved = input("\nPřejete si zadat další příklad? y / n ")
        if (odpoved == "y" or odpoved == "Y"):
            return True
        elif (odpoved == "n" or odpoved == "N"):
            return False
        else:
            pass
        
def volba(prvni_cislo, druhe_cislo):
    print("1 - sčítání")
    print("2 - odčítání")
    print("3 - násobení")
    print("4 - dělení")
    print("5 - umocňování")
    cislo_operace = nacti_cislo("Zadej volbu: ", "Neplatné zadání!\n")
    if cislo_operace == 1:
        print("Jejich součet je: ", prvni_cislo + druhe_cislo)
    elif cislo_operace == 2:
        print("Jejich rozdíl je: ", prvni_cislo - druhe_cislo)
    elif cislo_operace == 3:
        print("Jejich součin je: ", prvni_cislo * druhe_cislo)
    elif cislo_operace == 4:
        mezivysledek = 0
        try:
            mezivysledek = prvni_cislo / druhe_cislo
            print("Jejich podíl je: ", mezivysledek)
        except ZeroDivisionError:
            print("Dělení nulou!")
    elif cislo_operace == 5:
        print(prvni_cislo, "na", druhe_cislo, "je", prvni_cislo ** druhe_cislo)
    else:
        print("Neplatná volba!")
        
def main():
    print("Kalkulačka 1.0\n")
    pokracovat = True
    while pokracovat:
        prvni_cislo = nacti_cislo("Zadej číslo: ", "Neplatné číslo!\n")
        druhe_cislo = nacti_cislo("Zadej číslo: ", "Neplatné číslo!\n")
        volba(prvni_cislo, druhe_cislo)
        if dalsi_priklad():
            pass
        else:
            pokracovat = False
    input("\nStiskněne klávesu Enter....")

main()