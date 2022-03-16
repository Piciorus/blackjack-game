from karte import *

# class FaceCard(Karte):
#     def __init__ (self, bild,rang,anzug,weiche=10, harte=10):
#         super().__init__(bild,rang,anzug)
        
#         self.weiche=weiche
#         self.harte=harte
        
class FaceCard(Karte):
    def __init__ (self,rang,anzug):
        super().__init__(rang,anzug)
        
        self.weiche=10
        self.harte=10
        
    def __str__(self) :
        return f'{self.rang} {self.anzug}'
    
    __repr__ = __str__    
    

def test ():
    lista=[FaceCard('J','♤ schwarz'),FaceCard('Q','♤ schwarz'),FaceCard('K','♤ schwarz')]
    
    for i in range (0,3):
        assert lista[i].weiche==10 and lista[i].harte==10
    
test()