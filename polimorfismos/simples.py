# exercicios/polimorfismos/classe.py

class Animal:

    def fazer_som(self):
        pass

class Cao(Animal):           #(Animal) significa que esta a herdar tudo da classe mãe "Animal"
    
    def fazer_som(self):
        return "O cão ladra"
    
class Gato(Animal):

    def fazer_som(self):
        return "O gato mia"
    


Kiara = Cao()
Mia = Gato()

print(Kiara.fazer_som())
print(Mia.fazer_som())
