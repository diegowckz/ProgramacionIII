class Figura(object):
    pi = 0
    radio = 0
    altura = 0

    def __init__(self, altura, radio):
        self.altura = altura
        self.radio = radio

class Esfera(Figura):
    pi = 3.1416
    radio_esfera = float(input("RADIO DE ESFERA: "))
    area_esfera = 4 * pi * radio_esfera ** 2
    volumen_esfera = (pi * radio_esfera ** 3) / 3
    print("EL AREA DE LA ESFERA ES: ", area_esfera)
    print("EL VOLUMEN DE LA ESFERA ES: ", volumen_esfera)

print(" ")
class Cilindro(Figura):
    pi = 3.1416
    radio_cilindro = float(input("RADIO DE CILINDRO: "))
    altura = float(input("DEME ALTURA DE CILINDRO"))
    area_cilindro = (2 * pi * radio_cilindro) * (radio_cilindro + altura)
    print("EL VOLUMEN DE EL CILINDRO ES: ", area_cilindro )

print(" ")
class Cono(Figura):
    pi = 3.1416
    radio_cono = float(input("RADIO DEL CONO: "))
    area = float(input("DEME ALTURA DEL CONO"))
    area_cono = (((radio_cono ** 2) * pi) * area) / 3
    print("EL VOLUMEN DE EL CILINDRO ES: ", area_cono )