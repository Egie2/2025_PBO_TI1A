from model import Tugas
import database

class ManajerTugas:
    def tambah_tugas(self, tugas: Tugas):
        sql = "INSERT INTO tugas (judul, deskripsi, deadline, status) VALUES (?, ?, ?, ?)"
        return database.execute_query(sql, (tugas.judul, tugas.deskripsi, tugas.deadline, tugas.status))

    def ambil_semua(self):
        sql = "SELECT id, judul, deskripsi, deadline, status FROM tugas ORDER BY deadline ASC"
        rows = database.fetch_all(sql)
        return [Tugas(id_tugas=r[0], judul=r[1], deskripsi=r[2], deadline=r[3], status=r[4]) for r in rows]

    def tandai_selesai(self, id_tugas):
        sql = "UPDATE tugas SET status='Selesai' WHERE id=?"
        database.execute_query(sql, (id_tugas,))

    def hapus_tugas(self, id_tugas):
        sql = "DELETE FROM tugas WHERE id=?"
        database.execute_query(sql, (id_tugas,))
