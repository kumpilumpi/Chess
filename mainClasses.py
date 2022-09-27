

# Osnovni file za moje šahovske pustolovščine
# 
# Class 
#   mreža  
#   figure
#       Kmet, Kralj, Konj, Kraljica, Tekač


STARTINGPOSITION = []

class board:
    def __init__(self):
        #sestavi mrežo
        self.boardgame = self.boardCreate()
        self.pastMoves = []
        pass
    
    def boardCreate():
        game = []
        for i in range(7):
            game.append([0]*8)
        return game
    
#---Glavni class figure
class figure:
    '''Class figure(position, color). Attribute legalMoves.'''
    def __init__(self, position, color):
        self.position = position
        self.color = color
        self.legalMoves

#---Pod classi za specifične figure, se razlikuje le v legalMoves
class king(figure):
    def __init__(self):
        super().__init__()
        self.legalmoves = self.legalMoves()
        
    def legalMoves(board):
        return

class queen(figure):
    def __init__(self):
        super().__init__()
        self.legalmoves = self.legalMoves()
        
    def legalMoves(board):
        return

class rook(figure):
    def __init__(self):
        super().__init__()
        self.legalmoves = self.legalMoves()
        
    def legalMoves(board):
        return

class bishop(figure):
    def __init__(self):
        super().__init__()
        self.legalmoves = self.legalMoves()
        
    def legalMoves(board):
        return

class knight(figure):
    def __init__(self):
        super().__init__()
        self.legalmoves = self.legalMoves()
        
    def legalMoves(board):
        return

class pawn(figure):
    def __init__(self):
        super().__init__()
        self.legalmoves = self.legalMoves()
        
    def legalMoves(board):
        return