import pyxel

class Jeu:
    def __init__(self) :
        """Initialise la classe Jeu et pyxel."""
        self.fenetre_x = 1000
        self.fenetre_y = 1000
        pyxel.init(self.fenetre_x, self.fenetre_y, title="Mario")
        self.debut = False
        self.M1=[[1,1,1,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,1,1,2]]
        self.M2=[[1,1,1,1,1,1,1,1,1,1],
                        [1,0,0,0,0,0,0,0,0,0],
                        [1,0,1,1,1,1,1,1,1,1],
                        [1,0,1,0,0,0,0,0,0,1],
                        [1,0,1,0,1,1,1,1,0,1],
                        [1,0,1,0,2,0,0,1,0,1],
                        [1,0,1,0,0,0,0,1,0,1],
                        [1,0,1,1,1,1,1,1,0,1],
                        [1,0,0,0,0,0,0,0,0,1],
                        [1,1,1,1,1,1,1,1,1,1]]
        self.M3=[[1,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1],
            [3,0,0,0,0,0,0,0,0,0]]
        self.maps = [self.M1,self.M2,self.M3]
        self.numero_map = 0
        self.collide = False
        # position initiale du vaisseau (origine des positions : coin haut gauche)
        self.vaisseau_x = 0
        self.vaisseau_y = 0
        self.vitesse = 10
        self.diagonale_vitesse = 7
        self.frame = 0
        self.minute = 0
        self.seconde = 0
        self.temps_total = []
        self.fin = False
    def personnage(self):
        pyxel.rect(self.vaisseau_x, self.vaisseau_y, 50, 50, 1)
        pyxel.rectb(self.vaisseau_x, self.vaisseau_y, 50, 50, 2)

            
    def voiture_deplacement(self):
        
        """Déplacement avec les touches de direction."""
        self.droite = pyxel.btn(pyxel.KEY_RIGHT)
        self.gauche = pyxel.btn(pyxel.KEY_LEFT)
        self.haut = pyxel.btn(pyxel.KEY_UP)
        self.bas = pyxel.btn(pyxel.KEY_DOWN)
        if self.debut:
            # Déplacement en diagonale en haut à droite
            if self.droite and self.haut and self.vaisseau_x < self.fenetre_x - 50 and self.vaisseau_y > 0:
                self.vaisseau_x += self.diagonale_vitesse
                self.vaisseau_y -= self.diagonale_vitesse
            # Déplacement en diagonale en haut à gauche
            elif self.gauche and self.haut and self.vaisseau_x > 0 and self.vaisseau_y > 0:
                self.vaisseau_x -= self.diagonale_vitesse
                self.vaisseau_y -= self.diagonale_vitesse
            # Déplacement en diagonale en bas à droite
            elif self.droite and self.bas and self.vaisseau_x < self.fenetre_x - 50 and self.vaisseau_y < self.fenetre_y - 50:
                self.vaisseau_x += self.diagonale_vitesse
                self.vaisseau_y += self.diagonale_vitesse
            # Déplacement en diagonale en bas à gauche
            elif self.gauche and self.bas and self.vaisseau_x > 0 and self.vaisseau_y < self.fenetre_y - 50:
                self.vaisseau_x -= self.diagonale_vitesse
                self.vaisseau_y += self.diagonale_vitesse
    
            # Déplacement vers la droite
            elif self.droite and self.vaisseau_x < self.fenetre_x - 50:
                self.vaisseau_x += self.vitesse
            # Déplacement vers la gauche
            elif self.gauche and self.vaisseau_x > 0:
                self.vaisseau_x -= self.vitesse
            # Déplacement vers le haut
            elif self.haut and self.vaisseau_y > 0:
                self.vaisseau_y -= self.vitesse
            # Déplacement vers le bas
            elif self.bas and self.vaisseau_y < self.fenetre_y - 50:
                self.vaisseau_y += self.vitesse

    def temps(self):
        """Calcule le temps de jeux."""
        if self.debut:
            self.frame += 1
            if self.frame % 30 == 0:
                self.seconde += 1
                if self.seconde == 60:
                    self.minute += 1
                    self.seconde = 0
            print(f"Temps : {self.minute} min {self.seconde} sec")
        if not self.debut and self.fin:
            pyxel.init(200,200,title="Fin")
            self.frame = 0
            self.seconde = 0
            self.minute = 0
            pyxel.text(150,100,f"Temps : {self.minute} min {self.seconde} sec",1)
            
    def dessine_matrice(self, m):
        if not self.fin:
            for y in range(len(m[0])):
                for x in range(len(m)):
                    if m[y][x] == 0:
                        pyxel.rect(x * 100, y * 100, 100, 100, 11) 
                    elif m[y][x] == 1: 
                        pyxel.rect(x * 100, y * 100, 100, 100, 13)
                    elif m[y][x] == 2:
                        pyxel.rect(x * 100, y * 100, 100, 100, 10)
                    elif m[y][x] == 2:
                        pyxel.rect(x * 100, y * 100, 100, 100, 8)
                        
    def collision(self, x, y):
        """Vérifie s'il y a une collision avec un obstacle dans la matrice."""
        case_x = x // 100
        case_y = y // 100
        if self.maps[self.numero_map][case_y][case_x] == 0:
            self.vitesse = 1
            self.diagonale_vitesse = 1
        elif self.maps[self.numero_map][case_y][case_x] == 2:
            self.numero_map +=1
            if self.numero_map == 1:
                self.vaisseau_x = 950
                self.vaisseau_y = 50
            if self.numero_map == 2:
                self.vaisseau_x = 0
                self.vaisseau_y = 0
        elif self.maps[self.numero_map][case_y][case_x] == 3:
            self.debut = False
            self.fin = True
        else:
            self.vitesse = 20
            self.diagonale_vitesse = 7
        print(self.numero_map)
            
    def debut_jeu(self):
        if pyxel.btn(pyxel.KEY_SPACE):
            self.debut = True
        # quand le jeu est en cours
            
    def update(self):
        """mise à jour des variables (30 fois par seconde)"""
        self.collision(self.vaisseau_x, self.vaisseau_y)
        
    def draw(self):
        """Créer et positionne les objets 30 fois par seconde"""
        pyxel.cls(0)
        self.dessine_matrice(self.maps[self.numero_map])
        self.personnage()
        self.voiture_deplacement()
        self.temps()
        self.debut_jeu()

    def run(self):
        pyxel.run(self.update, self.draw)

game = Jeu()
game.run()