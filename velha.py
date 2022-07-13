class Velha:
    matriz = [["1","2","3"],["4","5","6"],["7","8","9"]]
    def verify(self):

        for x in range(0,3):
            if self.matriz[x].count("X") == 3:
                return (f" X Win's",True)
            elif self.matriz[x].count("O") == 3:
                return (f" O Win's",True)

            elif self.matriz[0][x] == self.matriz[1][x] and self.matriz[1][x] == self.matriz[2][x]:
                return (f"{self.matriz[0][x]} Win's",True)

        if (self.matriz[0][0] == self.matriz[2][2] and self.matriz[0][0] == self.matriz[1][1]) or (self.matriz[0][2] ==   self.matriz[2][0] and  self.matriz[0][2] == self.matriz[1][1]): 
            return (f"{self.matriz[1][1]} Win's",True)
            
        return ("velha",False)
    
    def menu(self,):
        return f"  {self.matriz[0][0]} | {self.matriz[0][1]} | {self.matriz[0][2]}\n----+---+----\n  {self.matriz[1][0]} | {self.matriz[1][1]} | {self.matriz[1][2]}\n----+---+----\n  {self.matriz[2][0]} | {self.matriz[2][1]} | {self.matriz[2][2]}"

    def insert(self,pos1,pos2,player):
        self.matriz[pos1][pos2] = player
             
    def pos(self,value,player):
        match value:
            case 1:
                self.insert(0,0,player)
            case 2:
                self.insert(0,1,player)
            case 3:
                self.insert(0,2,player)
            case 4:
                self.insert(1,0,player)
            case 5:
                self.insert(1,1,player)
            case 6:
                self.insert(1,2,player)
            case 7:
                self.insert(2,0,player)
            case 8:
                self.insert(2,1,player)
            case 9:
                self.insert(2,2,player)
