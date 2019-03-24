class Bmw:
    def __init__(self):
        self.models=['i8','x2','x6']

    def models_bmw(self):
        print("models are :")
        for models in self.models:
            print(models)

beamer=Bmw()
beamer.models_bmw()
