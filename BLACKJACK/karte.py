# class Karte:
#     def __init__ (self, bild, rang, anzug):
#         self.bild=bild
#         self.rang=rang
#         self.anzug=anzug
        
#     def __str__(self) :
#         return f'{self.rang} {self.anzug}'

class Karte:
    def __init__ (self,rang, anzug):
        self.rang=rang
        self.anzug=anzug

    
    def __str__(self) :
        return f'{self.rang} {self.anzug}'
    
    def __eq__(self, other):
        return self.rang==other.rang and self.anzug==other.anzug
    
    __repr__ = __str__
        
# cards = [chr(code) for code in range(ord('🂡'), ord('🃞')+1)]
# cards = [code for code in cards if code not in [ '🃏','', '\U0001f0af', '\U0001f0b0','\U0001f0c0','\U0001f0d0']]

