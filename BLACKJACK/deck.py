import random
from karte import Karte
from faceCard import FaceCard
from aceCard import AceCard
class Deck:
    def __init__(self):
        #self.Karten_liste=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
        
        self.Karten_liste=[]
        
        for i in range(2,11):
            self.Karten_liste.append(Karte(i,'♡ rot',))
        lista=[FaceCard('J','♡ rot'),FaceCard('Q','♡ rot'),FaceCard('K','♡ rot'),AceCard('A','♡ rot')]
        self.Karten_liste.extend(lista)
        
        for i in range(2,11):
            self.Karten_liste.append(Karte(i,'♢ rot',))
        lista=[FaceCard('J','♢ rot'),FaceCard('Q','♢ rot'),FaceCard('K','♢ rot'),AceCard('A','♢ rot')]
        self.Karten_liste.extend(lista)
        
        for i in range(2,11):
            self.Karten_liste.append(Karte(i,'♤ schwarz',))
        lista=[FaceCard('J','♤ schwarz'),FaceCard('Q','♤ schwarz'),FaceCard('K','♤ schwarz'),AceCard('A','♤ schwarz')]
        self.Karten_liste.extend(lista)
        
        for i in range(2,11):
            self.Karten_liste.append(Karte(i,'♧ schwarz',))
        lista=[FaceCard('J','♧ schwarz'),FaceCard('Q','♧ schwarz'),FaceCard('K','♧ schwarz'),AceCard('A','♧ schwarz')]
        self.Karten_liste.extend(lista)
        
    
    def add_Karte(self):
        self.MyList.append(self.Karten_liste[-1])
        
        self.MyList2=list(map(lambda a: a.rang ,self.MyList)) #######
        
        self.Karten_liste2=list(map(lambda a: a.rang ,self.Karten_liste)) #######
        self.Karten_liste.pop()
        self.Karten_liste2.pop() #######
        
        
        return self.MyList
        
    def mischung(self):
        #_______________
        lista_test=[]
        lista_test.extend(self.Karten_liste)
        
        assert lista_test[0] not in lista_test[1:-1]
        #_______________
        random.shuffle(self.Karten_liste)
        
        #---------
        
        #varianta 1 de test pt mischung
        assert lista_test!=self.Karten_liste
        #varianta 2 de test pt mischung
        ok=1
        for i in range(0,5):
            if lista_test[i]==self.Karten_liste[i]:
                ok=0
                
        assert ok==1
        #---------
        self.Karten_liste2=list(map(lambda a: a.rang ,self.Karten_liste)) #######
     
    def reset_Karten_liste(self):
        self.Karten_liste.clear()
        
    def initializieren(self):
        self.MyList=[]
        self.MyList2=[] ########
        self.Karten_liste2=[] #######
        
    # def new_game(self):
    #     self.Karten_liste=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']   
        
    def summe(self):
        s=0
        k=0
        for elem in self.MyList2:
            if str(elem) in 'JQK':
                s+=10
                
            elif str(elem) =='A':
                k+=1
                
            else :
                s+=(elem)
                
        while k!=0 :
            s+=11
            if s>21:
                s-=10
                
            k-=1
        
        return s
    
    def pachet_carti(self):
        return self.Karten_liste
    
    def carti(self):
        return self.MyList
    
    
    def __str__(self):
        return f'{self.MyList}'
    
    __repr__=__str__


a=Deck()
a.initializieren()
a.mischung()