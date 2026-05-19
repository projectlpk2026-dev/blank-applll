import re
import streamlit as st
import pandas as pd

# =========================
# DATABASE UNSUR
# =========================

unsur = {
    "H": {"nama": "Hidrogen", "nomor_atom": 1, "massa_atom": 1.00794},
    "He": {"nama": "Helium", "nomor_atom": 2, "massa_atom": 4.002602},
    "Li": {"nama": "Litium", "nomor_atom": 3, "massa_atom": 6.941},
    "Be": {"nama": "Berilium", "nomor_atom": 4, "massa_atom": 9.012182},
    "B": {"nama": "Boron", "nomor_atom": 5, "massa_atom": 10.811},
    "C": {"nama": "Karbon", "nomor_atom": 6, "massa_atom": 12.0107},
    "N": {"nama": "Nitrogen", "nomor_atom": 7, "massa_atom": 14.0067},
    "O": {"nama": "Oksigen", "nomor_atom": 8, "massa_atom": 15.9994},
    "F": {"nama": "Fluorin", "nomor_atom": 9, "massa_atom": 18.9984032},
    "Ne": {"nama": "Neon", "nomor_atom": 10, "massa_atom": 20.1797},
    "Na": {"nama": "Natrium", "nomor_atom": 11, "massa_atom": 22.98976928},
    "Mg": {"nama": "Magnesium", "nomor_atom": 12, "massa_atom": 24.3050},
    "Al": {"nama": "Aluminium", "nomor_atom": 13, "massa_atom": 26.9815386},
    "Si": {"nama": "Silikon", "nomor_atom": 14, "massa_atom": 28.0855},
    "P": {"nama": "Fosfor", "nomor_atom": 15, "massa_atom": 30.973762},
    "S": {"nama": "Sulfur", "nomor_atom": 16, "massa_atom": 32.065},
    "Cl": {"nama": "Klorin", "nomor_atom": 17, "massa_atom": 35.453},
    "Ar": {"nama": "Argon", "nomor_atom": 18, "massa_atom": 39.948},
    "K": {"nama": "Kalium", "nomor_atom": 19, "massa_atom": 39.0983},
    "Ca": {"nama": "Kalsium", "nomor_atom": 20, "massa_atom": 40.078},
    "Fe": {"nama": "Besi", "nomor_atom": 26, "massa_atom": 55.845},
    "Cu": {"nama": "Tembaga", "nomor_atom": 29, "massa_atom": 63.546},
    "Zn": {"nama": "Seng", "nomor_atom": 30, "massa_atom": 65.38},
    "Ag": {"nama": "Perak", "nomor_atom": 47, "massa_atom": 107.8682},
    "I": {"nama": "Iodin", "nomor_atom": 53, "massa_atom": 126.90447},
    "Ba": {"nama": "Barium", "nomor_atom": 56, "massa_atom": 137.327},
    "Au": {"nama": "Emas", "nomor_atom": 79, "massa_atom": 196.966569},
    "Hg": {"nama": "Merkuri", "nomor_atom": 80, "massa_atom": 200.59}
}

# =========================
# FUNGSI HITUNG BM / Mr
# =========================

def hitung_bobot_molekul(rumus):
    rumus = rumus.strip()

    if rumus == "":
        return None, None, "Rumus kimia tidak boleh kosong."

    pola_validasi = r'^([A-Z][a-z]?\d*)+$'

    if not re.fullmatch(pola_validasi, rumus):
        return None, None, "Format rumus kimia tidak valid. Contoh yang benar: H2O, CO2, NaCl, C6H12O6."

    pola = r'([A-Z][a-z]?)(\d*)'
    hasil = re.findall(pola, rumus)

    total = 0
    detail = []

    for simbol, jumlah in hasil:
        if simbol not in unsur:
            return None, None, f"Unsur '{simbol}' tidak ditemukan dalam database."

        jumlah_atom = int(jumlah) if jumlah != "" else 1
        massa_atom = unsur[simbol]["massa_atom"]
        subtotal = massa_atom * jumlah_atom
        total += subtotal

        detail.append({
            "Simbol Unsur": simbol,
            "Nama Unsur": unsur[simbol]["nama"],
            "Nomor Atom": unsur[simbol]["nomor_atom"],
            "Jumlah Atom": jumlah_atom,
            "Massa Atom": massa_atom,
            "Subtotal Massa": round(subtotal, 3)
        })

    return round(total, 3), detail, None


# =========================
# TAMPILAN STREAMLIT
# =========================

st.set_page_config(
    page_title="Kalkulator Bobot Molekul",
    page_icon="⚗️",
    layout="centered"
)

st.title("⚗️ Kalkulator Bobot Molekul / Mr")
st.write("Masukkan rumus kimia untuk menghitung bobot molekul senyawa.")

rumus = st.text_input(
    "Rumus Kimia",
    placeholder="Contoh: H2O, CO2, NaCl, C6H12O6"
)

if st.button("Hitung Bobot Molekul"):
    total, detail, error = hitung_bobot_molekul(rumus)

    if error:
        st.error(error)
    else:
        df = pd.DataFrame(detail)

        st.subheader("Tabel Hasil Perhitungan")
        st.dataframe(df, use_container_width=True)

        st.subheader("Total Bobot Molekul")
        st.success(f"Mr {rumus} = {total} g/mol")

        st.subheader("Rincian Perhitungan")
        for item in detail:
            st.write(
                f"{item['Simbol Unsur']} ({item['Nama Unsur']}) = "
                f"{item['Massa Atom']} × {item['Jumlah Atom']} = "
                f"{item['Subtotal Massa']} g/mol"
            )
