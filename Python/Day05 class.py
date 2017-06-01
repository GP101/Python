class KCar:
    color = 1
    def SetColor(self, c):
        self.color = c
        return
    def GetColor(self):
        return self.color
class KSportCar(KCar):
    def ApplyTurbo(self):
        print 'Turbo Applied'
        return

c = KCar()
c.SetColor(3)
print c.GetColor()

c2 = KSportCar()
c2.SetColor(4)
c2.ApplyTurbo()
