from deck import Deck
from datetime import date

class Scores():
    def __init__ (self, my_list, dealer_list, nume, runde, geld, spiel_geld):
        self.my_list=my_list
        self.dealer_list=dealer_list
        self.nume=nume
        self.runde=runde
        self.geld=geld
        self.spiel_geld=spiel_geld
    
    def ergebniss(self):
        f=open("ergebnisse.txt","r")
        for line in f:
            pass
        last_line = line
        f.close()
            
        return last_line
        
    def aktuelle_partitur(self):
        
        self.my_list2=list(map(lambda a: a.rang ,self.my_list)) #######
        self.dealer_list2=list(map(lambda a: a.rang ,self.dealer_list)) #######
        
        s1=0
        k=0
        for elem in self.my_list2:
            if str(elem) in 'JQK':
                s1+=10
                
            elif str(elem) =='A':
                k+=1
                
            else :
                s1+=elem
                
        while k!=0 :
            s1+=11
            if s1>21:
                s1-=10
                
            k-=1
            
        
        s2=0
        k=0
        for elem in self.dealer_list2:
            if str(elem) in 'JQK':
                s2+=10
                
            elif str(elem) =='A':
                k+=1
                
            else :
                s2+=elem
                
        while k!=0 :
            s2+=11
            if s2>21:
                s2-=10
                
            k-=1
            
        
        
        if s1==s2 and s1<21:
            print("Es ist Gleichheit")
            f=open("ergebnisse.txt","a")
            f.write("equal\n")   
            f.close()
            
            self.geld+=self.spiel_geld
            f=open("Rez.txt","a")
            f.write(str(date.today()) + " " + str(self.runde) + " " + self.nume + " " + str(self.geld) +"\n")   
            f.close()  
                
        elif s2==21:
            print("Du hast verloren :(")
            f=open("ergebnisse.txt","a")
            f.write("lose\n")   
            f.close()
            
            f=open("Rez.txt","a")
            f.write(str(date.today()) + " " + str(self.runde) + " " + self.nume + " " + str(self.geld)+"\n")   
            f.close()
        
        elif s2>21:
            print("Du hast gewonnen!!!")
            f=open("ergebnisse.txt","a")
            f.write("win\n")   
            f.close()
            
            self.geld+=2*self.spiel_geld
            f=open("Rez.txt","a")
            f.write(str(date.today()) + " " + str(self.runde) + " " + self.nume + " " + str(self.geld)+"\n")   
            f.close()
        
        elif s1-s2>0:
            print("Du hast gewonnen!!!")
            f=open("ergebnisse.txt","a")
            f.write("win\n")   
            f.close() 
            
            self.geld+=2*self.spiel_geld
            f=open("Rez.txt","a")
            f.write(str(date.today()) + " " + str(self.runde) + " " + self.nume + " " + str(self.geld)+"\n")   
            f.close()
        
        elif s1-s2<0:
            print("Du hast verloren :(")
            f=open("ergebnisse.txt","a")
            f.write("lose\n")   
            f.close() 
            
            f=open("Rez.txt","a")
            f.write(str(date.today()) + " " + str(self.runde) + " " + self.nume + " " + str(self.geld)+"\n")   
            f.close()
            
         
            
            