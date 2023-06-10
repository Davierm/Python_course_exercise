#   /////////////                                                                        
#   ///////////////////                               
#   ///////////////////////                           
#   ////////////////                                  
#   ////////////     //////////                       
#   //////////   ////////////////                     
#   ////////   ///////////////////                    
#   ///////   /////////////////////                   
#   //////   //////////////////////                   
#   /////   ////////////////////////                  
#   /////   ////////////////////////                  
#   /////   ////////////////////////                
#   //////   //////////////////////                   
#   ///////   /////////////////////                   
#   ////////   ///////////////////                    
#   //////////   ////////////////                     
#   ////////////     //////////                       
#   ////////////////                                  
#   ///////////////////////                           
#   ///////////////////                               
#   /////////////                                     

#   DAVIERM - David Čermák
#   https://davierm.cz
#   kontakt@davierm.cz            

class Kalkulacka:
    def scitani(self):
        print("Součet:", cislo_1 + cislo_2)
    
    def odcitani(self):
        print("Rozdíl:", cislo_1 - cislo_2)
        
    def nasobeni(self):
        print("Součin:", cislo_1 * cislo_2)
        
    def deleni(self):
        print("Podíl:", cislo_1 / cislo_2)
        
cislo_1 = float(input("Zadej 1. číslo: "))
cislo_2 = float(input("Zadej 2. číslo: "))

kalkulacka = Kalkulacka()

kalkulacka.scitani()
kalkulacka.odcitani()
kalkulacka.nasobeni()
kalkulacka.deleni()

input()