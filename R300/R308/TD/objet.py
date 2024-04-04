class tasse:
    def __init__(self, name, cost, color, matiere, fill, position,state, typeliquid):
        self.name = name
        self.cost = cost
        self.color = color
        self.matiere = matiere
        self.fill = False
        self.position= position 
        self.state=state
        self.typeliquid=typeliquid
    
    def getliquid(self):
        return self.typeliquid

    def getcolor(self):
        return self.color

    def getetat(self):
        return self.state
    
    def fall(self):
        self.state="cassé"
        self.fill=False
        self.typeliquid="none"
        return self.state, self.fill, self.typeliquid
    
    # A regarder pour savoir comment appeler la valeur booléenne de fill
    # def fill(self):
    #     self.fill=True
    #     return self.fill
    
    # def empty(self):
        # self.fill=False
        # return self.fill


tasse1 = tasse("tasse1", 10, "rouge", "porcelaine", False, "droite", "cassé", "café")
tasse2= tasse("tasse2", 10, "violet", "porcelaine", False, "gauche", "cassé", "chocolat")


