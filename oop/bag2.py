
dataPegawai = {"SDM": [], "Keuangan": [], "Produksi": []}


class Pegawai:
    def __init__(self, id, nama, alamat, departemen, gaji):
        self.id = id
        self.nama = nama
        self.alamat = alamat
        self.departmen = departemen
        self.gaji = gaji

    def __str__(self):
        return f'{self.id}, Nama: {self.nama}, Alamat: {self.alamat}, Department: {self.departmen}, Gaji: {self.gaji}'
    
    
