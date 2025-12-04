# ===============================================
# File: uts_app.py
# Ini adalah APLIKASI STREAMLIT LENGKAP KITA
# ===============================================

import streamlit as st
import pandas as pd

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Program Audit COBIT",
    page_icon="✅",
    layout="wide"
)

# --- Judul Aplikasi ---
st.title("Program Audit COBIT - Ujian MID AUSI")
st.write("Tema: Sistem Informasi Marketplace Tokopedia")
st.markdown("""
**Disusun oleh Kelompok :**
* 1. Nafar Ja'far Ashidiqi (202353135)
* 2. Selamet Ahmad Faisal (202353103)
* 3. Rafli Zudha Sasongko (202353095)
* 4. Endhito Hafiz Meifaza  (202353148)
""")

# --- Sidebar untuk Menu ---
st.sidebar.title("Menu Navigasi Domain COBIT")
menu_pilihan = st.sidebar.radio(
    "Silakan pilih domain untuk dievaluasi:",
    (
        "EDM (Evaluate, Direct and Monitor)",
        "APO (Align, Plan and Organize)",
        "BAI (Build, Acquire and Implement)",
        "DSS (Deliver, Service and Support)",
        "MEA (Monitor, Evaluate and Assess)"
    )
)

# --- Panduan Skala Likert (di dalam fungsi agar bisa dipanggil) ---
def tampilkan_panduan():
    st.info("""
    **Panduan Penilaian (Skala Likert):**
    * **1:** Sangat Tidak Setuju / Sangat Buruk
    * **2:** Tidak Setuju / Buruk
    * **3:** Netral
    * **4:** Setuju / Baik
    * **5:** Sangat Setuju / Sangat Baik
    """)

# --- Tampilkan Hasil (di dalam fungsi agar bisa dipanggil) ---
def tampilkan_hasil(domain_name, total_score, num_questions, rec_error, rec_warn, rec_success):
    st.write("---")
    st.header(f"Hasil Evaluasi Domain {domain_name}")
    
    rata_rata_skor = total_score / num_questions
    
    st.metric(label=f"Rata-rata Skor Domain {domain_name}", value=f"{rata_rata_skor:.2f} / 5.00")
    
    if rata_rata_skor < 3:
        st.error(f"Rekomendasi: {rec_error}")
    elif rata_rata_skor < 4:
        st.warning(f"Rekomendasi: {rec_warn}")
    else:
        st.success(f"Rekomendasi: {rec_success}")

# ==================================================================
# --- KONTEN HALAMAN SESUAI MENU ---
# ==================================================================

if menu_pilihan == "EDM (Evaluate, Direct and Monitor)":
    st.header("Domain 1: EDM (Evaluate, Direct and Monitor)")
    st.subheader("Evaluasi dan Pengarahan TI")
    st.write("---")
    tampilkan_panduan()
    
    with st.form(key="form_edm"):
        edm01_score = st.radio("EDM01: Sejauh mana dewan direksi/manajemen puncak Tokopedia memastikan kerangka tata kelola TI (Marketplace) ditetapkan?", (1, 2, 3, 4, 5), horizontal=True)
        edm02_score = st.radio("EDM02: Sejauh mana manajemen puncak memastikan bahwa investasi TI (fitur baru Marketplace) memberikan nilai?", (1, 2, 3, 4, 5), horizontal=True)
        edm03_score = st.radio("EDM03: Bagaimana penilaian Anda terhadap cara manajemen puncak Tokopedia mengelola risiko TI (keamanan data, downtime)?", (1, 2, 3, 4, 5), horizontal=True)
        
        submitted_edm = st.form_submit_button("Hitung Hasil Evaluasi EDM")

    if submitted_edm:
        total = edm01_score + edm02_score + edm03_score
        tampilkan_hasil("EDM", total, 3,
            "Tata kelola (governance) TI di level dewan/direksi perlu evaluasi dan perbaikan segera.",
            "Tata kelola TI sudah berjalan, namun perlu peningkatan pada pemantauan.",
            "Tata kelola TI di level dewan/direksi sudah berjalan sangat baik.")

elif menu_pilihan == "APO (Align, Plan and Organize)":
    st.header("Domain 2: APO (Align, Plan and Organize)")
    st.subheader("Perencanaan dan Pengorganisasian TI")
    st.write("---")
    tampilkan_panduan()
        
    with st.form(key="form_apo"):
        apo01_score = st.radio("APO01: Sejauh mana Tokopedia telah menetapkan kerangka kerja tata kelola TI (Marketplace) dengan jelas?", (1, 2, 3, 4, 5), horizontal=True)
        apo02_score = st.radio("APO02: Apakah strategi TI (Marketplace) Tokopedia sudah selaras dengan strategi bisnis perusahaan?", (1, 2, 3, 4, 5), horizontal=True)
        apo04_score = st.radio("APO04: Bagaimana efektivitas Tokopedia dalam mengidentifikasi dan menerapkan inovasi (misal: AI, live shopping)?", (1, 2, 3, 4, 5), horizontal=True)

        submitted_apo = st.form_submit_button("Hitung Hasil Evaluasi APO")

    if submitted_apo:
        total = apo01_score + apo02_score + apo04_score
        tampilkan_hasil("APO", total, 3,
            "Perlu adanya perbaikan signifikan pada domain APO.",
            "Domain APO sudah cukup baik, namun perlu optimasi.",
            "Domain APO sudah berjalan dengan sangat baik.")

elif menu_pilihan == "BAI (Build, Acquire and Implement)":
    st.header("Domain 3: BAI (Build, Acquire and Implement)")
    st.subheader("Pengembangan dan Implementasi TI")
    st.write("---")
    tampilkan_panduan()
    
    with st.form(key="form_bai"):
        bai01_score = st.radio("BAI01: Bagaimana penilaian Anda terhadap cara Tokopedia mengelola proyek-proyek TI (misal: peluncuran fitur baru Marketplace) agar selesai tepat waktu?", (1, 2, 3, 4, 5), horizontal=True)
        bai03_score = st.radio("BAI03: Sejauh mana proses pengembangan (coding) dan desain solusi di Tokopedia sudah terdefinisi dan berkualitas baik?", (1, 2, 3, 4, 5), horizontal=True)
        bai06_score = st.radio("BAI06: Bagaimana efektivitas Tokopedia dalam mengelola perubahan (update) pada aplikasi Marketplace agar meminimalkan bug atau gangguan?", (1, 2, 3, 4, 5), horizontal=True)

        submitted_bai = st.form_submit_button("Hitung Hasil Evaluasi BAI")

    if submitted_bai:
        total = bai01_score + bai03_score + bai06_score
        tampilkan_hasil("BAI", total, 3,
            "Proses pengembangan dan implementasi TI (rilis fitur baru) memiliki kelemahan besar.",
            "Proses pengembangan TI sudah baik, namun perlu peningkatan pada manajemen perubahan.",
            "Proses pengembangan dan implementasi TI sudah matang.")

elif menu_pilihan == "DSS (Deliver, Service and Support)":
    st.header("Domain 4: DSS (Deliver, Service and Support)")
    st.subheader("Penyampaian dan Dukungan Layanan TI")
    st.write("---")
    tampilkan_panduan()
    
    with st.form(key="form_dss"):
        dss01_score = st.radio("DSS01: Bagaimana penilaian Anda terhadap keandalan operasional (ketersediaan server, minim downtime) dari platform Marketplace Tokopedia?", (1, 2, 3, 4, 5), horizontal=True)
        dss02_score = st.radio("DSS02: Sejauh mana efektivitas Tokopedia (Customer Service) dalam menanggapi dan menyelesaikan keluhan atau insiden dari pengguna?", (1, 2, 3, 4, 5), horizontal=True)
        dss05_score = st.radio("DSS05: Bagaimana penilaian Anda terhadap pengelolaan layanan keamanan TI di Tokopedia (perlindungan data pengguna, keamanan transaksi)?", (1, 2, 3, 4, 5), horizontal=True)
        
        submitted_dss = st.form_submit_button("Hitung Hasil Evaluasi DSS")

    if submitted_dss:
        total = dss01_score + dss02_score + dss05_score
        tampilkan_hasil("DSS", total, 3,
            "Layanan operasional dan dukungan pelanggan (CS) memiliki masalah serius.",
            "Layanan operasional sudah cukup baik, namun perlu peningkatan pada kecepatan respons.",
            "Layanan operasional, dukungan pelanggan, dan keamanan sudah berjalan sangat baik.")

elif menu_pilihan == "MEA (Monitor, Evaluate and Assess)":
    st.header("Domain 5: MEA (Monitor, Evaluate and Assess)")
    st.subheader("Pemantauan dan Evaluasi Kinerja TI")
    st.write("---")
    tampilkan_panduan()
    
    with st.form(key="form_mea"):
        mea01_score = st.radio("MEA01: Seberapa baik Tokopedia memantau kinerja platform Marketplace (kecepatan, uptime) dan membandingkannya dengan target?", (1, 2, 3, 4, 5), horizontal=True)
        mea02_score = st.radio("MEA02: Bagaimana efektivitas sistem audit internal (kontrol internal) Tokopedia dalam mengevaluasi proses TI?", (1, 2, 3, 4, 5), horizontal=True)
        mea03_score = st.radio("MEA03: Sejauh mana Tokopedia memastikan platform Marketplace-nya patuh terhadap regulasi eksternal (misal: UU Perlindungan Data Pribadi)?", (1, 2, 3, 4, 5), horizontal=True)

        submitted_mea = st.form_submit_button("Hitung Hasil Evaluasi MEA")

    if submitted_mea:
        total = mea01_score + mea02_score + mea03_score
        tampilkan_hasil("MEA", total, 3,
            "Proses pemantauan, evaluasi, dan kepatuhan (compliance) sangat lemah.",
            "Proses pemantauan sudah berjalan, namun perlu penguatan pada area audit internal.",
            "Proses pemantauan, evaluasi, dan kepatuhan sudah sangat matang.")
