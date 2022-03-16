from deck import Deck

class Dealer(Deck):
    def __init__ (self, lista):
        super().__init__()
        self.Karten_liste=lista
    
    def initializieren(self):
        return super().initializieren()
    
    def add_Karte(self):
        return super().add_Karte()
    
    
    def reset_Karten_liste(self):
        return super().reset_Karten_liste()
        
    def new_game(self):
        return super().new_game()
    
    def summe(self):
        return super().summe()
    
    def pachet_carti(self):
        return super().pachet_carti()
    
    def carti(self):
        return super().carti()
        
    def __str__(self):
        return super().__str__()