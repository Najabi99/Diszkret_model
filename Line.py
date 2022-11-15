class Vonal:
    def __init__(self, allomasok):
        self.allomasok = allomasok




lines = {
    "A-L": [["A","C","E","I","L"],[i for i in range(25) if i%3 == 0]],
    "L-A": [["L","I","E","C","A"],[i for i in range(25) if i%3 == 0]],
    "B-K":[["B","C","D","G","K"],[i for i in range(25) if i%3 == 1]],
    "K-B": [["K","G","D","C","B"],[i for i in range(25) if i%3 == 1]],
    "F-J":[["F","G","H","I","J"],[i for i in range(25) if i%3 == 2]],
    "J-F":[["J","I","H","G","F"],[i for i in range(25) if i%3 == 2]]
}


Allomas = Vonal(lines)

print([i for i in range(25) if i%3 == 0])