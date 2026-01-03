# exercicios/polimorfismos/classe_w_super.py

class Animal:

    def __init__(self, animal, barulho, genero):
        self.animal = animal
        self.barulho = barulho
        self.genero = genero


    def fazer_som(self):
        if self.genero == "f":
            return f"A {self.animal} faz {self.barulho}"
        elif self.genero == "m":
            return f"O {self.animal} faz {self.barulho}"
        else:
            return "Género inválido"


class Cao(Animal):
    def __init__(self, nome, genero):
        
        nomes = {
            "f": "cadela",
            "m": "cão"
        }

        if genero not in nomes:
            raise ValueError("Género invalido")
        
        animal_completo = nomes[genero] + " " + nome
        
        super().__init__(animal_completo, "au", genero)


class gato(Animal):
    def __init__(self, nome, genero):

        nomes = {
            "f": "gata",
            "m": "gato"
        }

        if genero not in nomes:
            raise ValueError("Género invalido")
        
        animal_completo = nomes[genero] + " " + nome

        super().__init__(animal_completo, "miau", genero)

    
Kiara = Cao("Kiara", "f")
print(Kiara.fazer_som())

Mia = gato("Mia", "f")
print(Mia.fazer_som())