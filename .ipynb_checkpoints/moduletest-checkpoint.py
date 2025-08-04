### EXAMPLE PYTHON MODULE
# Define some variables:
numberone = 1
nameOfJames = "James"

# define some functions
def printhello():
    print("Hello, c'est une importation")

def timesfour(input):
    print(input * 4)

# define a class
class Piano:
    def __init__(self):
        self.type = input("Quel type de piano ? ")
        self.height = input("Quelle hauteur (en pieds) ? ")
        self.price = input("Combien a-t-il coûté ? ")
        self.age = input("Quel âge a-t-il (en années) ? ")
    
    def printdetails(self):
        print("Ce piano mesure " + self.height + " pieds de haut,")
        print("c'est un piano " + self.type + ", âgé de " + self.age + " ans et ayant coûté " + self.price + " dollars.")