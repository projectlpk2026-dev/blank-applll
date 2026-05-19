import re
import streamlit as st
import pandas as pd

# =========================
# DATABASE UNSUR
# =========================

unsur = {
    "H": {"nama": "Hidrogen", "nomor_atom": 1, "massa_atom": 1.008},
    "He": {"nama": "Helium", "nomor_atom": 2, "massa_atom": 4.0026},
    "Li": {"nama": "Litium", "nomor_atom": 3, "massa_atom": 6.94},
    "Be": {"nama": "Berilium", "nomor_atom": 4, "massa_atom": 9.0122},
    "B": {"nama": "Boron", "nomor_atom": 5, "massa_atom": 10.81},
    "C": {"nama": "Karbon", "nomor_atom": 6, "massa_atom": 12.011},
    "N": {"nama": "Nitrogen", "nomor_atom": 7, "massa_atom": 14.007},
    "O": {"nama": "Oksigen", "nomor_atom": 8, "massa_atom": 15.999},
    "F": {"nama": "Fluorin", "nomor_atom": 9, "massa_atom": 18.998},
    "Ne": {"nama": "Neon", "nomor_atom": 10, "massa_atom": 20.180},
    "Na": {"nama": "Natrium", "nomor_atom": 11, "massa_atom": 22.990},
    "Mg": {"nama": "Magnesium", "nomor_atom": 12, "massa_atom": 24.305},
    "Al": {"nama": "Aluminium", "nomor_atom": 13, "massa_atom": 26.982},
    "Si": {"nama": "Silikon", "nomor_atom": 14, "massa_atom": 28.085},
    "P": {"nama": "Fosfor", "nomor_atom": 15, "massa_atom": 30.974},
    "S": {"nama": "Sulfur", "nomor_atom": 16, "massa_atom": 32.06},
    "Cl": {"nama": "Klorin", "nomor_atom": 17, "massa_atom": 35.45},
    "Ar": {"nama": "Argon", "nomor_atom": 18, "massa_atom": 39.948},
    "K": {"nama": "Kalium", "nomor_atom": 19, "massa_atom": 39.098},
    "Ca": {"nama": "Kalsium", "nomor_atom": 20, "massa_atom": 40.078},
    "Sc": {"nama": "Skandium", "nomor_atom": 21, "massa_atom": 44.956},
    "Ti": {"nama": "Titanium", "nomor_atom": 22, "massa_atom": 47.867},
    "V": {"nama": "Vanadium", "nomor_atom": 23, "massa_atom": 50.942},
    "Cr": {"nama": "Kromium", "nomor_atom": 24, "massa_atom": 51.996},
    "Mn": {"nama": "Mangan", "nomor_atom": 25, "massa_atom": 54.938},
    "Fe": {"nama": "Besi", "nomor_atom": 26, "massa_atom": 55.845},
    "Co": {"nama": "Kobalt", "nomor_atom": 27, "massa_atom": 58.933},
    "Ni": {"nama": "Nikel", "nomor_atom": 28, "massa_atom": 58.693},
    "Cu": {"nama": "Tembaga", "nomor_atom": 29, "massa_atom": 63.546},
    "Zn": {"nama": "Seng", "nomor_atom": 30, "massa_atom": 65.38},
    "Ga": {"nama": "Galium", "nomor_atom": 31, "massa_atom": 69.723},
    "Ge": {"nama": "Germanium", "nomor_atom": 32, "massa_atom": 72.630},
    "As": {"nama": "Arsen", "nomor_atom": 33, "massa_atom": 74.922},
    "Se": {"nama": "Selenium", "nomor_atom": 34, "massa_atom": 78.971},
    "Br": {"nama": "Bromin", "nomor_atom": 35, "massa_atom": 79.904},
    "Kr": {"nama": "Kripton", "nomor_atom": 36, "massa_atom": 83.798},
    "Rb": {"nama": "Rubidium", "nomor_atom": 37, "massa_atom": 85.468},
    "Sr": {"nama": "Stronsium", "nomor_atom": 38, "massa_atom": 87.62},
    "Y": {"nama": "Itrium", "nomor_atom": 39, "massa_atom": 88.906},
    "Zr": {"nama": "Zirkonium", "nomor_atom": 40, "massa_atom": 91.224},
    "Nb": {"nama": "Niobium", "nomor_atom": 41, "massa_atom": 92.906},
    "Mo": {"nama": "Molibdenum", "nomor_atom": 42, "massa_atom": 95.95},
    "Tc": {"nama": "Teknesium", "nomor_atom": 43, "massa_atom": 98},
    "Ru": {"nama": "Rutenium", "nomor_atom": 44, "massa_atom": 101.07},
    "Rh": {"nama": "Rodium", "nomor_atom": 45, "massa_atom": 102.906},
    "Pd": {"nama": "Paladium", "nomor_atom": 46, "massa_atom": 106.42},
    "Ag": {"nama": "Perak", "nomor_atom": 47, "massa_atom": 107.868},
    "Cd": {"nama": "Kadmium", "nomor_atom": 48, "massa_atom": 112.414},
    "In": {"nama": "Indium", "nomor_atom": 49, "massa_atom": 114.818},
    "Sn": {"nama": "Timah", "nomor_atom": 50, "massa_atom": 118.710},
    "Sb": {"nama": "Antimon", "nomor_atom": 51, "massa_atom": 121.760},
    "Te": {"nama": "Telurium", "nomor_atom": 52, "massa_atom": 127.60},
    "I": {"nama": "Iodin", "nomor_atom": 53, "massa_atom": 126.904},
    "Xe": {"nama": "Xenon", "nomor_atom": 54, "massa_atom": 131.293},
    "Cs": {"nama": "Sesium", "nomor_atom": 55, "massa_atom": 132.905},
    "Ba": {"nama": "Barium", "nomor_atom": 56, "massa_atom": 137.327},
    "La": {"nama": "Lantanum", "nomor_atom": 57, "massa_atom": 138.905},
    "Ce": {"nama": "Serium", "nomor_atom": 58, "massa_atom": 140.116},
    "Pr": {"nama": "Praseodimium", "nomor_atom": 59, "massa_atom": 140.908},
    "Nd": {"nama": "Neodimium", "nomor_atom": 60, "massa_atom": 144.242},
    "Pm": {"nama": "Prometium", "nomor_atom": 61, "massa_atom": 145},
    "Sm": {"nama": "Samarium", "nomor_atom": 62, "massa_atom": 150.36},
    "Eu": {"nama": "Europium", "nomor_atom": 63, "massa_atom": 151.964},
    "Gd": {"nama": "Gadolinium", "nomor_atom": 64, "massa_atom": 157.25},
    "Tb": {"nama": "Terbium", "nomor_atom": 65, "massa_atom": 158.925},
    "Dy": {"nama": "Disprosium", "nomor_atom": 66, "massa_atom": 162.500},
    "Ho": {"nama": "Holmium", "nomor_atom": 67, "massa_atom": 164.930},
    "Er": {"nama": "Erbium", "nomor_atom": 68, "massa_atom": 167.259},
    "Tm": {"nama": "Tulium", "nomor_atom": 69, "massa_atom": 168.934},
    "Yb": {"nama": "Iterbium", "nomor_atom": 70, "massa_atom": 173.045},
    "Lu": {"nama": "Lutesium", "nomor_atom": 71, "massa_atom": 174.967},
    "Hf": {"nama": "Hafnium", "nomor_atom": 72, "massa_atom": 178.49},
    "Ta": {"nama": "Tantalum", "nomor_atom": 73, "massa_atom": 180.948},
    "W": {"nama": "Wolfram", "nomor_atom": 74, "massa_atom": 183.84},
    "Re": {"nama": "Renium", "nomor_atom": 75, "massa_atom": 186.207},
    "Os": {"nama": "Osmium", "nomor_atom": 76, "massa_atom": 190.23},
    "Ir": {"nama": "Iridium", "nomor_atom": 77, "massa_atom": 192.217},
    "Pt": {"nama": "Platina", "nomor_atom": 78, "massa_atom": 195.084},
    "Au": {"nama": "Emas", "nomor_atom": 79, "massa_atom": 196.967},
    "Hg": {"nama": "Merkuri", "nomor_atom": 80, "massa_atom": 200.592},
    "Tl": {"nama": "Talium", "nomor_atom": 81, "massa_atom": 204.38},
    "Pb": {"nama": "Timbal", "nomor_atom": 82, "massa_atom": 207.2},
    "Bi": {"nama": "Bismut", "nomor_atom": 83, "massa_atom": 208.980},
    "Po": {"nama": "Polonium", "nomor_atom": 84, "massa_atom": 209},
    "At": {"nama": "Astatin", "nomor_atom": 85, "massa_atom": 210},
    "Rn": {"nama": "Radon", "nomor_atom": 86, "massa_atom": 222},
    "Fr": {"nama": "Fransium", "nomor_atom": 87, "massa_atom": 223},
    "Ra": {"nama": "Radium", "nomor_atom": 88, "massa_atom": 226},
    "Ac": {"nama": "Aktinium", "nomor_atom": 89, "massa_atom": 227},
    "Th": {"nama": "Torium", "nomor_atom": 90, "massa_atom": 232.038},
    "Pa": {"nama": "Protaktinium", "nomor_atom": 91, "massa_atom": 231.036},
    "U": {"nama": "Uranium", "nomor_atom": 92, "massa_atom": 238.029},
    "Np": {"nama": "Neptunium", "nomor_atom": 93, "massa_atom": 237},
    "Pu": {"nama": "Plutonium", "nomor_atom": 94, "massa_atom": 244},
    "Am": {"nama": "Amerisium", "nomor_atom": 95, "massa_atom": 243},
    "Cm": {"nama": "Kurium", "nomor_atom": 96, "massa_atom": 247},
    "Bk": {"nama": "Berkelium", "nomor_atom": 97, "massa_atom": 247},
    "Cf": {"nama": "Kalifornium", "nomor_atom": 98, "massa_atom": 251},
    "Es": {"nama": "Einsteinium", "nomor_atom": 99, "massa_atom": 252},
    "Fm": {"nama": "Fermium", "nomor_atom": 100, "massa_atom": 257},
    "Md": {"nama": "Mendelevium", "nomor_atom": 101, "massa_atom": 258},
    "No": {"nama": "Nobelium", "nomor_atom": 102, "massa_atom": 259},
    "Lr": {"nama": "Lawrensium", "nomor_atom": 103, "massa_atom": 266},
    "Rf": {"nama": "Rutherfordium", "nomor_atom": 104, "massa_atom": 267},
    "Db": {"nama": "Dubnium", "nomor_atom": 105, "massa_atom": 268},
    "Sg": {"nama": "Seaborgium", "nomor_atom": 106, "massa_atom": 269},
    "Bh": {"nama": "Bohrium", "nomor_atom": 107, "massa_atom": 270},
    "Hs": {"nama": "Hassium", "nomor_atom": 108, "massa_atom": 277},
    "Mt": {"nama": "Meitnerium", "nomor_atom": 109, "massa_atom": 278},
    "Ds": {"nama": "Darmstadtium", "nomor_atom": 110, "massa_atom": 281},
    "Rg": {"nama": "Roentgenium", "nomor_atom": 111, "massa_atom": 282},
    "Cn": {"nama": "Kopernisium", "nomor_atom": 112, "massa_atom": 285},
    "Nh": {"nama": "Nihonium", "nomor_atom": 113, "massa_atom": 286},
    "Fl": {"nama": "Flerovium", "nomor_atom": 114, "massa_atom": 289},
    "Mc": {"nama": "Moskovium", "nomor_atom": 115, "massa_atom": 290},
    "Lv": {"nama": "Livermorium", "nomor_atom": 116, "massa_atom": 293},
    "Ts": {"nama": "Tenesin", "nomor_atom": 117, "massa_atom": 294},
    "Og": {"nama": "Oganeson", "nomor_atom": 118, "massa_atom": 294}
}

# =========================
# FUNGSI PARSING RUMUS KIMIA
# =========================

def parse_rumus(rumus):
    stack = [{}]
    i = 0

    while i < len(rumus):
        karakter = rumus[i]

        if karakter == "(":
            stack.append({})
            i += 1

        elif karakter == ")":
            if len(stack) == 1:
                raise ValueError("Tanda kurung tidak sesuai.")

            grup = stack.pop()
            i += 1

            angka = ""
            while i < len(rumus) and rumus[i].isdigit():
                angka += rumus[i]
                i += 1

            pengali = int(angka) if angka else 1

            for simbol, jumlah in grup.items():
                stack[-1][simbol] = stack[-1].get(simbol, 0) + jumlah * pengali

        elif karakter.isupper():
            simbol = karakter
            i += 1

            if i < len(rumus) and rumus[i].islower():
                simbol += rumus[i]
                i += 1

            angka = ""
            while i < len(rumus) and rumus[i].isdigit():
                angka += rumus[i]
                i += 1

            jumlah = int(angka) if angka else 1
            stack[-1][simbol] = stack[-1].get(simbol, 0) + jumlah

        else:
            raise ValueError("Format rumus kimia tidak valid.")

    if len(stack) != 1:
        raise ValueError("Tanda kurung tidak sesuai.")

    return stack[0]


# =========================
# FUNGSI HITUNG BOBOT MOLEKUL
# =========================

def hitung_bobot_molekul(rumus):
    rumus = rumus.strip()

    if rumus == "":
        return None, None, "Rumus kimia tidak boleh kosong."

    try:
        hasil_parse = parse_rumus(rumus)
    except ValueError as e:
        return None, None, str(e)

    total = 0
    detail = []

    for simbol, jumlah_atom in hasil_parse.items():
        if simbol not in unsur:
            return None, None, f"Unsur '{simbol}' tidak ditemukan dalam database."

        nama_unsur = unsur[simbol]["nama"]
        nomor_atom = unsur[simbol]["nomor_atom"]
        massa_atom = unsur[simbol]["massa_atom"]
        subtotal = massa_atom * jumlah_atom
        total += subtotal

        detail.append({
            "Simbol Unsur": simbol,
            "Nama Unsur": nama_unsur,
            "Nomor Atom": nomor_atom,
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

st.write(
    "Aplikasi ini digunakan untuk menghitung bobot molekul atau Mr "
    "berdasarkan rumus kimia senyawa."
)

rumus = st.text_input(
    "Masukkan Rumus Kimia",
    placeholder="Contoh: H2O, CO2, NaCl, C6H12O6, Ca(OH)2, Al2(SO4)3"
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
