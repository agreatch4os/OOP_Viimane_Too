#OLIVER OSTRAT, KEIRO TABUR, TANEL NÕMM
class Karakter:
    def _init_(self, nimi, elud, tugevus):
        self.nimi = nimi
        self.elud = elud
        self.tugevus = tugevus

    def kaotasElusi(self, kaotatud_elud):
        self.elud -= kaotatud_elud

    def lisaElusi(self, lisatud_elud):
        self.elud += lisatud_elud
        self.elud < 80
        self.elud = lisatud_elud + 10
        print(f"sa taastusid 10 elu!")

         
class vaenlane:
    def __init__(self, elud, tugevus):
        self.elud = elud
        self.tugevus = tugevus

elud1 = 100
elud = 100
tugevus = 20

print("Sa võitled vaenlasega!")
print("")
print("")
print("Vastane: ", elud, "elud")
print("Sina:", elud1, "elud")

while True:
    if elud1 <=0:
        break
    try:
        runnak = int(input("""
        Sinu valik
        ----------------------------
        1 - löök [50]
        2 - liigu edasi
        ----------------------------

        Mida sa valid? """))
        if  runnak == 1:
            elud1-=20
            elud-=50
            print("")
            print("löö teda")
            print("")
            print("vastane kaotas elusid")
            print("")
            print("Vastane: ", elud, "elud")
            print("")
            print("Sina: ", elud1, "elud")
            print("")
       

        elif runnak == 2:
                        print("")
                        print(" liikusid edasi")      

    except ValueError:
        print("")
        print("Liikusid edasi")
        print("")
