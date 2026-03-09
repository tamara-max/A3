from coche_electrico import CocheElectrico
from coche_combustion import CocheCombustion

class CocheHibrido(CocheElectrico, CocheCombustion):
    def avanzar(self, km):

        consumo_electrico = 0.02 * km

        # Priorizamos el eléctrico
        if self.carga >= consumo_electrico:
            print("Modo eléctrico")
            CocheElectrico.avanzar(self, km)

        else:
            print("Modo combustión")
            CocheCombustion.avanzar(self, km)
