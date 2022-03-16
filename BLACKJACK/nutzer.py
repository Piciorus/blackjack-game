from deck import Deck

class Nutzer(Deck):
    def __init__ (self, name, geldbetrag):
        super().__init__()
        
        self.name=name
        self.geldbetrag=geldbetrag
        
    def initializieren(self):
        return super().initializieren()
    
    def add_Karte(self):
        return super().add_Karte()
    
    def mischung(self):
        return super().mischung()
    
    def reset_Karten_liste(self):
        return super().reset_Karten_liste()
    
    def summe(self):
        return super().summe()
    
    def pachet_carti(self):
        return super().pachet_carti()
    
    def carti(self):
        return super().carti()
        
        
    def __str__(self):
        return super().__str__()