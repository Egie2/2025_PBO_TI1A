import streamlit as st
import datetime
from model import Tugas
from manajer_tugas import ManajerTugas

manajer = ManajerTugas()
st.set_page_config(page_title="Manajemen Tugas", layout="centered")
st.title("📋 Aplikasi Manajemen Tugas")

# FORM TAMBAH
with st.form("form_tugas"):
    judul = st.text_input("Judul Tugas")
    deskripsi = st.text_area("Deskripsi")
    deadline = st.date_input("Tenggat Waktu", value=datetime.date.today())
    submitted = st.form_submit_button("Tambah Tugas")

    if submitted and judul:
        tugas = Tugas(judul, deskripsi, deadline)
        manajer.tambah_tugas(tugas)
        st.success("Tugas berhasil ditambahkan.")
        st.rerun()

# LIST TUGAS
st.subheader("📌 Daftar Tugas")
daftar = manajer.ambil_semua()
if daftar:
    for t in daftar:
        with st.expander(f"{t.judul} (📅 {t.deadline})"):
            st.write(f"📝 {t.deskripsi}")
            st.write(f"Status: **{t.status}**")
            col1, col2 = st.columns(2)
            with col1:
                if t.status == "Belum Selesai":
                    if st.button("✅ Tandai Selesai", key=f"selesai_{t.id}"):
                        manajer.tandai_selesai(t.id)
                        st.success("Status diperbarui.")
                        st.rerun()
            with col2:
                if st.button("🗑️ Hapus", key=f"hapus_{t.id}"):
                    manajer.hapus_tugas(t.id)
                    st.warning("Tugas dihapus.")
                    st.rerun()
else:
    st.info("Belum ada tugas.")
