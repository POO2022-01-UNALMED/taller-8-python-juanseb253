from __future__ import annotations


class Deportista():
    def __init__(self, deporte, añosPracticando):
        self._deporte = deporte
        self._añosPracticando = añosPracticando
    def getDeporte(self):
        return self._deporte
    def getAñosPracticando(self):
        return self._añosPracticando
    def setDeporte(self, deporte):
        self._deporte = deporte
    def serAñosPracticando(self, años):
        self._añosPracticando = años
