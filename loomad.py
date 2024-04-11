#OLIVER OSTRAT, KEIRO TABUR, TANEL NÕMM
class Karakter:
    def _init_(self, nimi, elud, tegevus, kaotaElusi, lisaelusi):
        self.nimi = nimi
        self.elud = 100
        self.tugevus = 20
        self.kaotaElusi = 30
        self.lisaelusi = 40
         
class vaenlane:
    def __init__(self, elud, tugevus):
        self.elud = elud
        self.tugevus = tugevus
        elud = 50
        tugevus = 10

def combat_enemy_goblin():
    
    small_goblin_health = 100
    attack_basic = 100
    
    print("You are now in combat with a small goblin!")
    print("")
    print("")
    print("Small Goblin: ", small_goblin_health, "Health Points")

    while True:
        try:
            users_attack = int(input("""
            Your Moves
            ----------------------------
            1 - Basic attack [100]
           
            ----------------------------

            What do you choose? """))
            if  users_attack == 1:
                print("")
                print("You use your basic attack")
                print("")
                print("The goblin has taken some damage")
                print("")
                print("Small Goblin: ", small_goblin_health - 100, "Health points")
                print("")

                 

        except:
            print("")
            print("You cant do that!")
            print("")

combat_enemy_goblin()
