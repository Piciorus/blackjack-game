from faceCard import *

# class AceCard(FaceCard):
#     def __init__ (self,bild,rang,anzug,weiche, harte):
#         super().__init__(bild,rang,anzug,weiche, harte)
        
#         self.weiche=1
#         self.harte=10

class AceCard(FaceCard):
    def __init__ (self,rang,anzug):
        super().__init__(rang,anzug)
        
        self.weiche=1
        self.harte=11
        
    def __str__(self) :
        return f'{self.rang} {self.anzug}'
    
    __repr__ = __str__
    
def test ():
    lista=[AceCard('A','♡ rot'),AceCard('A','♢ rot'),AceCard('A','♤ schwarz'),AceCard('A','♧ schwarz')]
    
    for i in range (0,3):
        assert lista[i].weiche==1 and lista[i].harte==11
    
test()