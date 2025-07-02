import datetime

class Tugas:
    def __init__(self, judul, deskripsi, deadline, status="Belum Selesai", id_tugas=None):
        self.id = id_tugas
        self.judul = judul or "Tanpa Judul"
        self.deskripsi = deskripsi or "-"
        self.deadline = deadline if isinstance(deadline, datetime.date) else datetime.date.today()
        self.status = status
