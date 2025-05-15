import pyxel
import time

class Game():
    def __init__(self):
        pyxel.init(256, 256, title="Nuit du Code")
        pyxel.load("jeu_echec.pyxres")
        pyxel.mouse(True)
        Plateau()
        PionBlanc1()
        self.tour_de_jeu = "Blanc"
        pyxel.run(self.update, self.draw)
    def update(self):
        pass
#gérer les tours de jeux et aussi si il y a échec et mats

    def draw(self):
        pass

class Plateau:
    def __init__(self):

        """
        -------
        Plateau
        -------
        """

        self.coordonnee_plateau_x = 0
        self.coordonnee_plateau_y = 0
        self.coordonne_pyxel_editor_x = 0
        self.coordonne_pyxel_editor_y = 24

        """
        ------------
        Case_Cliquer
        ------------
        """
        self.case_blanche_cliquer_x = 0
        self.case_blanche_cliquer_y = 0
        self.case_noir_cliquer_x = 0
        self.case_noir_cliquer_y = 0
        
        pyxel.run(self.update, self.draw)
                  
    def update(self):
        pass
        
    def draw(self):
        self.plateau()
        self.case_cliquer()

    def plateau(self):
        self.coordonnee_plateau_x = 0
        self.coordonnee_plateau_y = 0
        self.coordonne_pyxel_editor_x = 0
        self.coordonne_pyxel_editor_y = 24
        pyxel.blt(self.coordonnee_plateau_x,self.coordonnee_plateau_y,0,self.coordonne_pyxel_editor_x,self.coordonne_pyxel_editor_y,32,32)
        for i in range(8):
            for i in range(7):
                self.coordonnee_plateau_x = self.coordonnee_plateau_x + 32
                if self.coordonne_pyxel_editor_x == 0:
                    self.coordonne_pyxel_editor_x = 32
                    self.coordonne_pyxel_editor_y = 24
                else:
                    self.coordonne_pyxel_editor_x = 0
                    self.coordonne_pyxel_editor_y = 24
                pyxel.blt(self.coordonnee_plateau_x,self.coordonnee_plateau_y,0,self.coordonne_pyxel_editor_x,self.coordonne_pyxel_editor_y,32,32)
            self.coordonnee_plateau_x = 0
            self.coordonnee_plateau_y = self.coordonnee_plateau_y + 32
            pyxel.blt(self.coordonnee_plateau_x,self.coordonnee_plateau_y,0,self.coordonne_pyxel_editor_x,self.coordonne_pyxel_editor_y,32,32)
            
    def case_cliquer(self):
        self.coordonnee_plateau_x = 256
        self.coordonnee_plateau_y = 0
        for i in range(8):
            for i in range(2):
                pyxel.blt(self.coordonnee_plateau_x, self.coordonnee_plateau_y, 0, 64, 0, 32,32)
                self.coordonnee_plateau_x = self.coordonnee_plateau_x + 32
            self.coordonnee_plateau_x = 256
            pyxel.blt(self.coordonnee_plateau_x, self.coordonnee_plateau_y, 0, 64, 0, 32,32)
            self.coordonnee_plateau_y = self.coordonnee_plateau_y + 32
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            colonne = pyxel.mouse_x // 32
            ligne = pyxel.mouse_y // 32
            if (colonne + ligne) % 2 == 0:
                print("=> Case blanche")
            else:
                print("=> Case noire")
            self.coordonnee_text_x = 266
            self.coordonnee_text_y = 10
            self.text_semi_round = 0
            self.text_round = 0
            if colonne < 8:
                colonne = chr(colonne + 65)
                ligne = abs(ligne - 8)
                print(f"{colonne}{ligne})")

class PionBlanc1():
    def __init__(self):

        self.coordonnee_x = 193
        self.coordonnee_y = 10
        
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.coordonnee_x, self.coordonne_y, 0, 0, 0, 8,8)










Game()

