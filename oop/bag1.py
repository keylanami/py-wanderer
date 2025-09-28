class Diagram:
    def __init__(self, judul, pengarang, harga):
        self.judul = judul
        self.pengarang = pengarang
        self.harga = harga

    def displays(self):
        print(f'{self.judul} | {self.pengarang} | {self.harga}')


harpot = Diagram('Harry Potter', 'J.K. Rowling', 300000)
uml = Diagram('UML', 'Ivar Jacobson', 400000)

harpot.displays()
uml.displays()
