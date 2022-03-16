# class Spiel:
#     def __init__(self, me, dealer):
#         self.me=me
#         self.dealer=dealer

from dealer import Dealer
from nutzer import Nutzer
from scores import Scores
from datetime import date

def main():
  
    name=str(input("name: ")) 
    a=Nutzer(name,100)
    
    runde=1
    new_game=1
    while new_game==1 and runde<=5 and a.geldbetrag>0:
        print("Geld: " + str(a.geldbetrag))
        spiel_geld=int(input("wie viel willst du wetten?: "))
        
        a.initializieren()
        a.mischung()
        
        a.geldbetrag-=spiel_geld
        print("Deine Karte ist:   " + str(a.add_Karte()) + "  Du hast: "+ str(a.geldbetrag)+  "   Der Wettbetrag ist: " + str(spiel_geld))
        
        
        print ('''
                
                option 1: get Karte
                option 2: Erhöhen Sie den Wettbetrag?
                option 3: Ich möchte aufhören
                
                ''')
        
        option=int(input("option: "))
        
        ok=1
        while option!=3:
            
            if option==1:
                print("Deine Karten sind:   " + str(a.add_Karte())+ "   Du hast: "+ str(a.geldbetrag)+ "   Der Wettbetrag ist: " + str(spiel_geld))
                
                if a.summe()== 21:
                    print ("Du hast gewonnen!!!")
                    option=3
                    ok=2
                    
                elif a.summe()> 21:
                    print ("Du hast verloren :(")
                    option=3
                    ok=0
                else:
                        
                    print ('''
                    
                    option 1: get Karte
                    option 2: Erhöhen Sie den Wettbetrag?
                    option 3: Ich möchte aufhören
                    
                    ''')
                
                    option=int(input("option: "))
                
            elif option==2:
                
                new=int(input("Wie viel willst du noch wetten? : "))
                
                spiel_geld+=new
                a.geldbetrag-=new
                
                print("Deine Karten sind:   " + str(a.carti())+ "   Du hast: "+ str(a.geldbetrag)+ "   Der Wettbetrag ist: " + str(spiel_geld))
                
                print ('''
                    
                    option 1: get Karte
                    option 2: Erhöhen Sie den Wettbetrag?
                    option 3: Ich möchte aufhören
                    
                    ''')
                
                option=int(input("option: "))
                
                
        if option==3:
            if ok==2:
                f=open("ergebnisse.txt","a")
                f.write("win\n")   
                f.close()
                
                a.geldbetrag+=2*spiel_geld
                
                f=open("Rez.txt","a")
                f.write(str(date.today()) + " " + str(runde) + " " + name + " " + str(a.geldbetrag)+"\n")   
                f.close()
            
            elif ok==0:
                f=open("ergebnisse.txt","a")
                f.write("lose\n")   
                f.close()
                
                f=open("Rez.txt","a")
                f.write(str(date.today()) + " " + str(runde) + " " + name + " " + str(a.geldbetrag)+"\n")
                f.close()
            
            else:
                b=Dealer(a.pachet_carti())
                b.initializieren()
                b.add_Karte()
                while b.summe()<=16:
                    b.add_Karte()
                
                print("Dealer hat:" + str(b.carti()) + " => " + str(b.summe()) + " Punkten" )
            
                rez=Scores(a.carti(), b.carti(), name, runde, a.geldbetrag, spiel_geld)
                rez.aktuelle_partitur()
                
                if rez.ergebniss()=='win\n':
                    a.geldbetrag+=2*spiel_geld
                elif rez.ergebniss()=='lose\n':
                    pass
                elif rez.ergebniss()=='equal\n':
                    a.geldbetrag+=spiel_geld
                    
            print("Dein Geldbetrag ist: " + str(a.geldbetrag))
                
            print('''
                  Willst du noch ein mal spielen?
                  ''')
            
            new_game2=str(input("ja/nein:  "))
            
            if new_game2=="ja":
                new_game=1
                runde+=1
            else:
                new_game=0
            
        

  
  
    
main()