import re
import streamlit as st
import pandas as pd
from datetime import datetime
 
unsur = {
    "H": {"nama": "Hidrogen", "nomor_atom": 1, "massa_atom": 1.008, "golongan": "1A"},
    "He": {"nama": "Helium", "nomor_atom": 2, "massa_atom": 4.0026, "golongan": "8A"},
    "Li": {"nama": "Litium", "nomor_atom": 3, "massa_atom": 6.94, "golongan": "1A"},
    "Be": {"nama": "Berilium", "nomor_atom": 4, "massa_atom": 9.0122, "golongan": "2A"},
    "B": {"nama": "Boron", "nomor_atom": 5, "massa_atom": 10.81, "golongan": "3A"},
    "C": {"nama": "Karbon", "nomor_atom": 6, "massa_atom": 12.011, "golongan": "4A"},
    "N": {"nama": "Nitrogen", "nomor_atom": 7, "massa_atom": 14.007, "golongan": "5A"},
    "O": {"nama": "Oksigen", "nomor_atom": 8, "massa_atom": 15.999, "golongan": "6A"},
    "F": {"nama": "Fluorin", "nomor_atom": 9, "massa_atom": 18.998, "golongan": "7A"},
    "Ne": {"nama": "Neon", "nomor_atom": 10, "massa_atom": 20.180, "golongan": "8A"},
    "Na": {"nama": "Natrium", "nomor_atom": 11, "massa_atom": 22.990, "golongan": "1A"},
    "Mg": {"nama": "Magnesium", "nomor_atom": 12, "massa_atom": 24.305, "golongan": "2A"},
    "Al": {"nama": "Aluminium", "nomor_atom": 13, "massa_atom": 26.982, "golongan": "3A"},
    "Si": {"nama": "Silikon", "nomor_atom": 14, "massa_atom": 28.085, "golongan": "4A"},
    "P": {"nama": "Fosfor", "nomor_atom": 15, "massa_atom": 30.974, "golongan": "5A"},
    "S": {"nama": "Sulfur", "nomor_atom": 16, "massa_atom": 32.06, "golongan": "6A"},
    "Cl": {"nama": "Klorin", "nomor_atom": 17, "massa_atom": 35.45, "golongan": "7A"},
    "Ar": {"nama": "Argon", "nomor_atom": 18, "massa_atom": 39.948, "golongan": "8A"},
    "K": {"nama": "Kalium", "nomor_atom": 19, "massa_atom": 39.098, "golongan": "1A"},
    "Ca": {"nama": "Kalsium", "nomor_atom": 20, "massa_atom": 40.078, "golongan": "2A"},
    "Sc": {"nama": "Skandium", "nomor_atom": 21, "massa_atom": 44.956, "golongan": "3B"},
    "Ti": {"nama": "Titanium", "nomor_atom": 22, "massa_atom": 47.867, "golongan": "4B"},
    "V": {"nama": "Vanadium", "nomor_atom": 23, "massa_atom": 50.942, "golongan": "5B"},
    "Cr": {"nama": "Kromium", "nomor_atom": 24, "massa_atom": 51.996, "golongan": "6B"},
    "Mn": {"nama": "Mangan", "nomor_atom": 25, "massa_atom": 54.938, "golongan": "7B"},
    "Fe": {"nama": "Besi", "nomor_atom": 26, "massa_atom": 55.845, "golongan": "8B"},
    "Co": {"nama": "Kobalt", "nomor_atom": 27, "massa_atom": 58.933, "golongan": "8B"},
    "Ni": {"nama": "Nikel", "nomor_atom": 28, "massa_atom": 58.693, "golongan": "8B"},
    "Cu": {"nama": "Tembaga", "nomor_atom": 29, "massa_atom": 63.546, "golongan": "1B"},
    "Zn": {"nama": "Seng", "nomor_atom": 30, "massa_atom": 65.38, "golongan": "2B"},
    "Ga": {"nama": "Galium", "nomor_atom": 31, "massa_atom": 69.723, "golongan": "3A"},
    "Ge": {"nama": "Germanium", "nomor_atom": 32, "massa_atom": 72.630, "golongan": "4A"},
    "As": {"nama": "Arsen", "nomor_atom": 33, "massa_atom": 74.922, "golongan": "5A"},
    "Se": {"nama": "Selenium", "nomor_atom": 34, "massa_atom": 78.971, "golongan": "6A"},
    "Br": {"nama": "Bromin", "nomor_atom": 35, "massa_atom": 79.904, "golongan": "7A"},
    "Kr": {"nama": "Kripton", "nomor_atom": 36, "massa_atom": 83.798, "golongan": "8A"},
    "Rb": {"nama": "Rubidium", "nomor_atom": 37, "massa_atom": 85.468, "golongan": "1A"},
    "Sr": {"nama": "Stronsium", "nomor_atom": 38, "massa_atom": 87.62, "golongan": "2A"},
    "Y": {"nama": "Itrium", "nomor_atom": 39, "massa_atom": 88.906, "golongan": "3B"},
    "Zr": {"nama": "Zirkonium", "nomor_atom": 40, "massa_atom": 91.224, "golongan": "4B"},
    "Nb": {"nama": "Niobium", "nomor_atom": 41, "massa_atom": 92.906, "golongan": "5B"},
    "Mo": {"nama": "Molibdenum", "nomor_atom": 42, "massa_atom": 95.95, "golongan": "6B"},
    "Tc": {"nama": "Teknesium", "nomor_atom": 43, "massa_atom": 98, "golongan": "7B"},
    "Ru": {"nama": "Rutenium", "nomor_atom": 44, "massa_atom": 101.07, "golongan": "8B"},
    "Rh": {"nama": "Rodium", "nomor_atom": 45, "massa_atom": 102.906, "golongan": "8B"},
    "Pd": {"nama": "Paladium", "nomor_atom": 46, "massa_atom": 106.42, "golongan": "8B"},
    "Ag": {"nama": "Perak", "nomor_atom": 47, "massa_atom": 107.868, "golongan": "1B"},
    "Cd": {"nama": "Kadmium", "nomor_atom": 48, "massa_atom": 112.414, "golongan": "2B"},
    "In": {"nama": "Indium", "nomor_atom": 49, "massa_atom": 114.818, "golongan": "3A"},
    "Sn": {"nama": "Timah", "nomor_atom": 50, "massa_atom": 118.710, "golongan": "4A"},
    "Sb": {"nama": "Antimon", "nomor_atom": 51, "massa_atom": 121.760, "golongan": "5A"},
    "Te": {"nama": "Telurium", "nomor_atom": 52, "massa_atom": 127.60, "golongan": "6A"},
    "I": {"nama": "Iodin", "nomor_atom": 53, "massa_atom": 126.904, "golongan": "7A"},
    "Xe": {"nama": "Xenon", "nomor_atom": 54, "massa_atom": 131.293, "golongan": "8A"},
    "Cs": {"nama": "Sesium", "nomor_atom": 55, "massa_atom": 132.905, "golongan": "1A"},
    "Ba": {"nama": "Barium", "nomor_atom": 56, "massa_atom": 137.327, "golongan": "2A"},
    "La": {"nama": "Lantanum", "nomor_atom": 57, "massa_atom": 138.905, "golongan": "Lantanida"},
    "Ce": {"nama": "Serium", "nomor_atom": 58, "massa_atom": 140.116, "golongan": "Lantanida"},
    "Pr": {"nama": "Praseodimium", "nomor_atom": 59, "massa_atom": 140.908, "golongan": "Lantanida"},
    "Nd": {"nama": "Neodimium", "nomor_atom": 60, "massa_atom": 144.242, "golongan": "Lantanida"},
    "Pm": {"nama": "Prometium", "nomor_atom": 61, "massa_atom": 145, "golongan": "Lantanida"},
    "Sm": {"nama": "Samarium", "nomor_atom": 62, "massa_atom": 150.36, "golongan": "Lantanida"},
    "Eu": {"nama": "Europium", "nomor_atom": 63, "massa_atom": 151.964, "golongan": "Lantanida"},
    "Gd": {"nama": "Gadolinium", "nomor_atom": 64, "massa_atom": 157.25, "golongan": "Lantanida"},
    "Tb": {"nama": "Terbium", "nomor_atom": 65, "massa_atom": 158.925, "golongan": "Lantanida"},
    "Dy": {"nama": "Disprosium", "nomor_atom": 66, "massa_atom": 162.500, "golongan": "Lantanida"},
    "Ho": {"nama": "Holmium", "nomor_atom": 67, "massa_atom": 164.930, "golongan": "Lantanida"},
    "Er": {"nama": "Erbium", "nomor_atom": 68, "massa_atom": 167.259, "golongan": "Lantanida"},
    "Tm": {"nama": "Tulium", "nomor_atom": 69, "massa_atom": 168.934, "golongan": "Lantanida"},
    "Yb": {"nama": "Iterbium", "nomor_atom": 70, "massa_atom": 173.045, "golongan": "Lantanida"},
    "Lu": {"nama": "Lutesium", "nomor_atom": 71, "massa_atom": 174.967, "golongan": "Lantanida"},
    "Hf": {"nama": "Hafnium", "nomor_atom": 72, "massa_atom": 178.49, "golongan": "4B"},
    "Ta": {"nama": "Tantalum", "nomor_atom": 73, "massa_atom": 180.948, "golongan": "5B"},
    "W": {"nama": "Wolfram", "nomor_atom": 74, "massa_atom": 183.84, "golongan": "6B"},
    "Re": {"nama": "Renium", "nomor_atom": 75, "massa_atom": 186.207, "golongan": "7B"},
    "Os": {"nama": "Osmium", "nomor_atom": 76, "massa_atom": 190.23, "golongan": "8B"},
    "Ir": {"nama": "Iridium", "nomor_atom": 77, "massa_atom": 192.217, "golongan": "8B"},
    "Pt": {"nama": "Platina", "nomor_atom": 78, "massa_atom": 195.084, "golongan": "8B"},
    "Au": {"nama": "Emas", "nomor_atom": 79, "massa_atom": 196.967, "golongan": "1B"},
    "Hg": {"nama": "Merkuri", "nomor_atom": 80, "massa_atom": 200.592, "golongan": "2B"},
    "Tl": {"nama": "Talium", "nomor_atom": 81, "massa_atom": 204.38, "golongan": "3A"},
    "Pb": {"nama": "Timbal", "nomor_atom": 82, "massa_atom": 207.2, "golongan": "4A"},
    "Bi": {"nama": "Bismut", "nomor_atom": 83, "massa_atom": 208.980, "golongan": "5A"},
    "Po": {"nama": "Polonium", "nomor_atom": 84, "massa_atom": 209, "golongan": "6A"},
    "At": {"nama": "Astatin", "nomor_atom": 85, "massa_atom": 210, "golongan": "7A"},
    "Rn": {"nama": "Radon", "nomor_atom": 86, "massa_atom": 222, "golongan": "8A"},
    "Fr": {"nama": "Fransium", "nomor_atom": 87, "massa_atom": 223, "golongan": "1A"},
    "Ra": {"nama": "Radium", "nomor_atom": 88, "massa_atom": 226, "golongan": "2A"},
    "Ac": {"nama": "Aktinium", "nomor_atom": 89, "massa_atom": 227, "golongan": "Aktinida"},
    "Th": {"nama": "Torium", "nomor_atom": 90, "massa_atom": 232.038, "golongan": "Aktinida"},
    "Pa": {"nama": "Protaktinium", "nomor_atom": 91, "massa_atom": 231.036, "golongan": "Aktinida"},
    "U": {"nama": "Uranium", "nomor_atom": 92, "massa_atom": 238.029, "golongan": "Aktinida"},
    "Np": {"nama": "Neptunium", "nomor_atom": 93, "massa_atom": 237, "golongan": "Aktinida"},
    "Pu": {"nama": "Plutonium", "nomor_atom": 94, "massa_atom": 244, "golongan": "Aktinida"},
    "Am": {"nama": "Amerisium", "nomor_atom": 95, "massa_atom": 243, "golongan": "Aktinida"},
    "Cm": {"nama": "Kurium", "nomor_atom": 96, "massa_atom": 247, "golongan": "Aktinida"},
    "Bk": {"nama": "Berkelium", "nomor_atom": 97, "massa_atom": 247, "golongan": "Aktinida"},
    "Cf": {"nama": "Kalifornium", "nomor_atom": 98, "massa_atom": 251, "golongan": "Aktinida"},
    "Es": {"nama": "Einsteinium", "nomor_atom": 99, "massa_atom": 252, "golongan": "Aktinida"},
    "Fm": {"nama": "Fermium", "nomor_atom": 100, "massa_atom": 257, "golongan": "Aktinida"},
    "Md": {"nama": "Mendelevium", "nomor_atom": 101, "massa_atom": 258, "golongan": "Aktinida"},
    "No": {"nama": "Nobelium", "nomor_atom": 102, "massa_atom": 259, "golongan": "Aktinida"},
    "Lr": {"nama": "Lawrensium", "nomor_atom": 103, "massa_atom": 266, "golongan": "Aktinida"},
    "Rf": {"nama": "Rutherfordium", "nomor_atom": 104, "massa_atom": 267, "golongan": "4B"},
    "Db": {"nama": "Dubnium", "nomor_atom": 105, "massa_atom": 268, "golongan": "5B"},
    "Sg": {"nama": "Seaborgium", "nomor_atom": 106, "massa_atom": 269, "golongan": "6B"},
    "Bh": {"nama": "Bohrium", "nomor_atom": 107, "massa_atom": 270, "golongan": "7B"},
    "Hs": {"nama": "Hassium", "nomor_atom": 108, "massa_atom": 277, "golongan": "8B"},
    "Mt": {"nama": "Meitnerium", "nomor_atom": 109, "massa_atom": 278, "golongan": "8B"},
    "Ds": {"nama": "Darmstadtium", "nomor_atom": 110, "massa_atom": 281, "golongan": "8B"},
    "Rg": {"nama": "Roentgenium", "nomor_atom": 111, "massa_atom": 282, "golongan": "1B"},
    "Cn": {"nama": "Kopernisium", "nomor_atom": 112, "massa_atom": 285, "golongan": "2B"},
    "Nh": {"nama": "Nihonium", "nomor_atom": 113, "massa_atom": 286, "golongan": "3A"},
    "Fl": {"nama": "Flerovium", "nomor_atom": 114, "massa_atom": 289, "golongan": "4A"},
    "Mc": {"nama": "Moskovium", "nomor_atom": 115, "massa_atom": 290, "golongan": "5A"},
    "Lv": {"nama": "Livermorium", "nomor_atom": 116, "massa_atom": 293, "golongan": "6A"},
    "Ts": {"nama": "Tenesin", "nomor_atom": 117, "massa_atom": 294, "golongan": "7A"},
    "Og": {"nama": "Oganeson", "nomor_atom": 118, "massa_atom": 294, "golongan": "8A"}
} 

contoh_rumus = {
    # =========================
    # SENYAWA DASAR / GAS
    # =========================
    "Air": "H2O",
    "Karbon dioksida": "CO2",
    "Karbon monoksida": "CO",
    "Oksigen": "O2",
    "Nitrogen": "N2",
    "Hidrogen": "H2",
    "Klorin": "Cl2",
    "Amonia": "NH3",
    "Metana": "CH4",
    "Etana": "C2H6",
    "Propana": "C3H8",
    "Butana": "C4H10",
    "Nitrogen monoksida": "NO",
    "Nitrogen dioksida": "NO2",
    "Dinitrogen oksida": "N2O",
    "Sulfur dioksida": "SO2",
    "Sulfur trioksida": "SO3",
    "Hidrogen sulfida": "H2S",
 
    # =========================
    # ASAM
    # =========================
    "Asam klorida": "HCl",
    "Asam sulfat": "H2SO4",
    "Asam nitrat": "HNO3",
    "Asam fosfat": "H3PO4",
    "Asam asetat": "CH3COOH",
    "Asam oksalat": "H2C2O4",
    "Asam oksalat dihidrat": "H2C2O4(H2O)2",
    "Asam borat": "H3BO3",
    "Asam karbonat": "H2CO3",
    "Asam format": "HCOOH",
    "Asam sitrat": "C6H8O7",
 
    # =========================
    # BASA
    # =========================
    "Natrium hidroksida": "NaOH",
    "Kalium hidroksida": "KOH",
    "Kalsium hidroksida": "Ca(OH)2",
    "Magnesium hidroksida": "Mg(OH)2",
    "Amonium hidroksida": "NH4OH",
    "Barium hidroksida": "Ba(OH)2",
 
    # =========================
    # GARAM
    # =========================
    "Garam dapur": "NaCl",
    "Kalium klorida": "KCl",
    "Kalsium karbonat": "CaCO3",
    "Natrium karbonat": "Na2CO3",
    "Natrium bikarbonat": "NaHCO3",
    "Kalium nitrat": "KNO3",
    "Perak nitrat": "AgNO3",
    "Barium klorida": "BaCl2",
    "Kalsium klorida": "CaCl2",
    "Magnesium sulfat": "MgSO4",
    "Amonium sulfat": "(NH4)2SO4",
    "Amonium klorida": "NH4Cl",
    "Natrium nitrit": "NaNO2",
    "Natrium nitrat": "NaNO3",
    "Natrium fosfat": "Na3PO4",
    "Kalium fosfat": "K3PO4",
    "Kalium iodida": "KI",
    "Perak klorida": "AgCl",
    "Barium sulfat": "BaSO4",
 
    # =========================
    # OKSIDATOR / ANALITIK
    # =========================
    "Kalium permanganat": "KMnO4",
    "Kalium dikromat": "K2Cr2O7",
    "Hidrogen peroksida": "H2O2",
    "Iodin": "I2",
    "Natrium tiosulfat": "Na2S2O3",
    "Natrium oksalat": "Na2C2O4",
    "Kalium hidrogen ftalat": "KHC8H4O4",
    "Boraks": "Na2B4O7(H2O)10",
    "EDTA": "C10H16N2O8",
    "Disodium EDTA": "C10H14N2Na2O8",
 
    # =========================
    # SENYAWA LOGAM / LAB
    # =========================
    "Tembaga sulfat": "CuSO4",
    "Tembaga nitrat": "Cu(NO3)2",
    "Besi(II) sulfat": "FeSO4",
    "Besi(III) klorida": "FeCl3",
    "Besi(II) klorida": "FeCl2",
    "Aluminium sulfat": "Al2(SO4)3",
    "Tawas": "KAl(SO4)2(H2O)12",
    "FAS": "Fe(NH4)2(SO4)2(H2O)6",
 
    # =========================
    # SENYAWA ORGANIK
    # =========================
    "Glukosa": "C6H12O6",
    "Fruktosa": "C6H12O6",
    "Sukrosa": "C12H22O11",
    "Laktosa": "C12H22O11",
    "Etanol": "C2H5OH",
    "Metanol": "CH3OH",
    "Propanol": "C3H7OH",
    "Aseton": "C3H6O",
    "Benzena": "C6H6",
    "Toluena": "C7H8",
    "Fenol": "C6H5OH",
    "Urea": "CO(NH2)2",
    "Formaldehida": "CH2O",
    "Asetaldehida": "C2H4O",
 
    # =========================
    # MINERAL / INDUSTRI
    # =========================
    "Silika": "SiO2",
    "Alumina": "Al2O3",
    "Titanium dioksida": "TiO2",
    "Zink oksida": "ZnO",
    "Magnesium oksida": "MgO",
    "Kalsium oksida": "CaO",
    "Besi oksida": "Fe2O3",
    "Tembaga oksida": "CuO",
    "Mangan dioksida": "MnO2"
}
 
st.set_page_config(
    page_title="Kalkulator BM/Mr Kimia",
    page_icon="⚗️",
    layout="wide"
)
 
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
 
:root {
    --bg: #070b14;
    --panel: rgba(15, 23, 42, 0.78);
    --panel-solid: #0f172a;
    --line: rgba(56, 189, 248, 0.28);
    --text: #f8fbff;
    --muted: #cbd5e1;
    --cyan: #38bdf8;
    --blue: #2563eb;
    --green: #39ff14;
    --yellow: #facc15;
    --white: #ffffff;
}
 
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}
 
.stApp {
    color: var(--text);
    background:
        radial-gradient(circle at 15% 20%, rgba(37, 99, 235, 0.28), transparent 32%),
        radial-gradient(circle at 85% 10%, rgba(34, 197, 94, 0.16), transparent 28%),
        radial-gradient(circle at 55% 85%, rgba(56, 189, 248, 0.16), transparent 30%),
        linear-gradient(135deg, #020617 0%, #08111f 45%, #020617 100%);
    background-size: 140% 140%;
    animation: gradientMove 12s ease infinite;
}
 
@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
 
[data-testid="stSidebar"] {
    background: rgba(2, 6, 23, 0.88);
    border-right: 1px solid rgba(56, 189, 248, 0.18);
}
 
[data-testid="stSidebar"] * {
    color: #ffffff !important;
}
 
.block-container {
    padding-top: 2rem;
}
 
.hero {
    position: relative;
    overflow: hidden;
    display: grid;
    grid-template-columns: 130px 1fr;
    gap: 24px;
    align-items: center;
    padding: 34px;
    border-radius: 30px;
    background: linear-gradient(135deg, rgba(15,23,42,.96), rgba(21,46,103,.88), rgba(8,47,73,.78));
    border: 1px solid rgba(56, 189, 248, 0.35);
    box-shadow: 0 24px 80px rgba(0, 0, 0, 0.40), inset 0 0 55px rgba(56, 189, 248, 0.08);
    color: white;
    margin-bottom: 26px;
}
 
.hero::before {
    content: "";
    position: absolute;
    inset: -2px;
    background: linear-gradient(120deg, transparent, rgba(56,189,248,.26), transparent);
    transform: translateX(-100%);
    animation: shine 4.5s ease-in-out infinite;
}
 
@keyframes shine {
    0% { transform: translateX(-100%); }
    48%, 100% { transform: translateX(100%); }
}
 
.logo-wrap {
    position: relative;
    width: 112px;
    height: 112px;
    display: grid;
    place-items: center;
    border-radius: 28px;
    background: rgba(15, 23, 42, 0.72);
    border: 1px solid rgba(56, 189, 248, 0.32);
    box-shadow: 0 0 35px rgba(56,189,248,.28);
    z-index: 1;
}
 
.logo-core {
    position: absolute;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background: radial-gradient(circle, #e0f2fe 0%, #38bdf8 45%, #2563eb 100%);
    box-shadow: 0 0 28px rgba(56,189,248,.9);
}
 
.orbit {
    position: absolute;
    width: 82px;
    height: 36px;
    border: 2px solid rgba(125, 211, 252, 0.85);
    border-radius: 50%;
    animation: spin 4s linear infinite;
}
 
.orbit:nth-child(2) { transform: rotate(60deg); animation-duration: 5.2s; }
.orbit:nth-child(3) { transform: rotate(120deg); animation-duration: 6.4s; }
 
@keyframes spin {
    from { rotate: 0deg; }
    to { rotate: 360deg; }
}
 
.hero-content {
    position: relative;
    z-index: 1;
}
 
.hero h1 {
    margin: 0 0 10px 0;
    font-size: clamp(32px, 5vw, 54px);
    font-weight: 800;
    letter-spacing: -1px;
    background: linear-gradient(90deg, #ffffff, #7dd3fc, #22c55e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
 
.hero p {
    margin: 0;
    color: #ffffff;
    font-size: 16px;
    line-height: 1.65;
    max-width: 920px;
}
 
.badge-row {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 18px;
}
 
.badge {
    padding: 8px 12px;
    border-radius: 999px;
    background: rgba(56, 189, 248, 0.12);
    border: 1px solid rgba(56, 189, 248, 0.28);
    color: #ffffff !important;
    font-size: 13px;
    font-weight: 700;
}
 
.card {
    padding: 22px;
    border-radius: 22px;
    background: linear-gradient(145deg, rgba(15, 23, 42, 0.92), rgba(30, 41, 59, 0.74));
    border: 1px solid rgba(56, 189, 248, 0.25);
    box-shadow: 0 16px 38px rgba(0,0,0,0.30);
    transition: transform .25s ease, border-color .25s ease, box-shadow .25s ease;
}
 
.card:hover {
    transform: translateY(-4px);
    border-color: rgba(56, 189, 248, 0.55);
    box-shadow: 0 20px 55px rgba(56,189,248,0.14);
}
 
.card p {
    color: #ffffff !important;
    margin-bottom: 8px;
    font-weight: 700;
}
 
.metric-value {
    font-size: 34px;
    font-weight: 800;
    color: #39ff14 !important;
    text-shadow: 0 0 8px rgba(57,255,20,.65), 0 0 18px rgba(57,255,20,.35);
}
 
/* PERBAIKAN FONT LABEL: Masukkan rumus kimia, Tulis pertanyaan, Cari unsur, Pilih senyawa */
.stTextInput label,
.stTextArea label,
.stSelectbox label,
[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] p,
label {
    color: #ffffff !important;
    font-size: 16px !important;
    font-weight: 800 !important;
    letter-spacing: .2px;
    text-shadow: 0 0 8px rgba(56, 189, 248, 0.55);
}
 
.stTextInput input,
.stTextArea textarea {
    background: rgba(15, 23, 42, 0.96) !important;
    color: #ffffff !important;
    border: 1px solid rgba(56, 189, 248, 0.70) !important;
    border-radius: 14px !important;
    font-weight: 700 !important;
    font-size: 15px !important;
}
 
.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #c7f9ff !important;
    opacity: 1 !important;
}
 
/* SELECTBOX PILIH SENYAWA */
.stSelectbox div[data-baseweb="select"] > div {
    background: rgba(15, 23, 42, 0.98) !important;
    color: #ffffff !important;
    border: 1px solid rgba(56, 189, 248, 0.75) !important;
    border-radius: 14px !important;
    font-weight: 800 !important;
}
 
.stSelectbox div[data-baseweb="select"] span {
    color: #ffffff !important;
    font-weight: 800 !important;
    opacity: 1 !important;
}
 
/* DROPDOWN MENU */
div[data-baseweb="popover"] {
    background-color: #0f172a !important;
    border: 1px solid rgba(56, 189, 248, 0.35) !important;
    border-radius: 12px !important;
}
 
div[data-baseweb="popover"] * {
    color: #ffffff !important;
    background-color: #0f172a !important;
    font-weight: 600 !important;
}
 
div[data-baseweb="popover"] [role="option"]:hover {
    background-color: #1e40af !important;
    color: #ffffff !important;
}
 
/* TAMPILAN HASIL CONTOH RUMUS NEON TERANG: BaSO4, BaCl2, dll */
.formula-neon {
    margin-top: 10px;
    padding: 14px 16px;
    border-radius: 16px;
    background: rgba(2, 6, 23, 0.92);
    border: 1px solid rgba(57, 255, 20, 0.65);
    color: #39ff14 !important;
    font-family: 'Courier New', monospace;
    font-size: 22px;
    font-weight: 900;
    text-align: center;
    letter-spacing: 1px;
    text-shadow: 0 0 5px rgba(57,255,20,.95), 0 0 14px rgba(57,255,20,.75), 0 0 28px rgba(57,255,20,.45);
    box-shadow: inset 0 0 22px rgba(57,255,20,.08), 0 0 20px rgba(57,255,20,.16);
}
 
.stButton button, .stDownloadButton button {
    border: 0 !important;
    border-radius: 16px !important;
    color: #00111f !important;
    font-weight: 800 !important;
    background: linear-gradient(90deg, #38bdf8, #22c55e) !important;
    box-shadow: 0 12px 30px rgba(56,189,248,.22) !important;
    transition: transform .2s ease, filter .2s ease !important;
}
 
.stButton button:hover, .stDownloadButton button:hover {
    transform: translateY(-2px);
    filter: brightness(1.1);
}
 
[data-testid="stDataFrame"], .stAlert {
    border-radius: 18px !important;
    overflow: hidden;
}
 
.chat-user {
    background: rgba(37, 99, 235, 0.20);
    border: 1px solid rgba(96, 165, 250, 0.35);
    color: #ffffff;
    padding: 14px;
    border-radius: 16px;
    margin-bottom: 10px;
    font-weight: 600;
}
 
.chat-bot {
    background: rgba(15, 23, 42, 0.86);
    border: 1px solid rgba(34, 197, 94, 0.30);
    color: #dcfce7;
    padding: 14px;
    border-radius: 16px;
    margin-bottom: 14px;
    font-weight: 600;
}
 
h1, h2, h3, h4, label, p, span {
    color: inherit;
}
 
@media (max-width: 720px) {
    .hero {
        grid-template-columns: 1fr;
        text-align: center;
    }
    .logo-wrap {
        margin: auto;
    }
    .badge-row {
        justify-content: center;
    }
}
</style>
""", unsafe_allow_html=True)
 
 
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
 
 
def hitung_bm_mr(rumus):
    rumus = rumus.strip().replace(" ", "")
 
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
 
        data = unsur[simbol]
        massa_atom = data["massa_atom"]
        subtotal = massa_atom * jumlah_atom
        total += subtotal
 
        detail.append({
            "Simbol Unsur": simbol,
            "Nama Unsur": data["nama"],
            "Nomor Atom": data["nomor_atom"],
            "Golongan": data["golongan"],
            "Jumlah Atom": jumlah_atom,
            "Massa Atom": massa_atom,
            "Subtotal Massa": round(subtotal, 3),
            "Persentase Massa (%)": 0
        })
 
    for item in detail:
        item["Persentase Massa (%)"] = round(
            item["Subtotal Massa"] / total * 100, 2
        )
 
    return round(total, 3), detail, None
 
 
def buat_pembahasan(rumus, total, detail):
    unsur_terlibat = ", ".join(
        [f"{d['Nama Unsur']} ({d['Simbol Unsur']})" for d in detail]
    )
 
    rincian = "; ".join(
        [
            f"{d['Simbol Unsur']} sebanyak {d['Jumlah Atom']} atom "
            f"dengan subtotal {d['Subtotal Massa']} g/mol"
            for d in detail
        ]
    )
 
    dominan = max(detail, key=lambda x: x["Subtotal Massa"])
 
    return (
        f"Berdasarkan hasil perhitungan, senyawa {rumus} tersusun atas unsur "
        f"{unsur_terlibat}. Perhitungan BM/Mr dilakukan dengan mengalikan "
        f"massa atom relatif setiap unsur dengan jumlah atomnya, kemudian "
        f"seluruh subtotal massa dijumlahkan. Rinciannya adalah {rincian}. "
        f"Dari hasil tersebut diperoleh BM/Mr {rumus} sebesar {total} g/mol. "
        f"Unsur dengan kontribusi massa terbesar adalah {dominan['Nama Unsur']} "
        f"({dominan['Simbol Unsur']}) sebesar {dominan['Persentase Massa (%)']}%."
    )
 
 
def chatbot_jawab(pertanyaan):
    teks = pertanyaan.lower()
 
    if pertanyaan.strip() == "":
        return "Tulis pertanyaan dulu. Chatbot ini belum bisa membaca pikiran."
 
    if "apa itu bm" in teks or "apa itu mr" in teks:
        return (
            "BM atau Mr adalah jumlah massa atom relatif dari seluruh unsur "
            "penyusun suatu senyawa."
        )
 
    if "cara" in teks and "hitung" in teks:
        return (
            "Cara menghitung BM/Mr adalah: pisahkan unsur, tentukan jumlah atom, "
            "kalikan jumlah atom dengan massa atom, lalu jumlahkan semuanya."
        )
 
    if "fas" in teks:
        total, detail, error = hitung_bm_mr("Fe(NH4)2(SO4)2(H2O)6")
        return f"BM/Mr FAS Fe(NH4)2(SO4)2·6H2O adalah {total} g/mol."
 
    pola = re.search(r"([A-Z][A-Za-z0-9()]+)", pertanyaan)
    if pola:
        rumus = pola.group(1)
        total, detail, error = hitung_bm_mr(rumus)
 
        if error:
            return error
 
        return f"BM/Mr {rumus} = {total} g/mol."
 
    return (
        "Saya bisa membantu menghitung BM/Mr. Contoh pertanyaan: "
        "'hitung Mr H2SO4' atau 'berapa BM FAS?'."
    )
 
 
if "riwayat" not in st.session_state:
    st.session_state.riwayat = []
 
if "chat" not in st.session_state:
    st.session_state.chat = []
 
 
st.markdown("""
<div class="hero">
    <div class="logo-wrap">
        <div class="orbit"></div>
        <div class="orbit"></div>
        <div class="orbit"></div>
        <div class="logo-core"></div>
    </div>
    <div class="hero-content">
        <h1>Kalkulator BM / Mr Kimia</h1>
        <p> Aplikasi kalkulator kimia interaktif yang membantu menghitung Bobot Molekul (BM/Mr) senyawa secara cepat, akurat, dan mudah, dilengkapi fitur visualisasi data, database unsur, dan chatbot edukatif.</p>
    </div>
</div>
""", unsafe_allow_html=True)
 
 
with st.sidebar:
    st.header("Menu")
    menu = st.radio(
        "Pilih Fitur",
        [
            "Kalkulator BM/Mr",
            "Riwayat Pencarian",
            "Chatbot Mini",
            "Database Unsur"
        ]
    )
 
    st.subheader("Contoh Rumus")
    pilihan = st.selectbox("Pilih senyawa", list(contoh_rumus.keys()))
    st.markdown(f"<div class='formula-neon'>{contoh_rumus[pilihan]}</div>", unsafe_allow_html=True)
 
 
if menu == "Kalkulator BM/Mr":
    st.subheader("Input Rumus Kimia")
 
    col1, col2 = st.columns([2, 1])
 
    with col1:
        rumus = st.text_input(
            "Masukkan rumus kimia",
            value=contoh_rumus[pilihan],
            placeholder="Contoh: H2O, CO2, Ca(OH)2"
        )
 
    with col2:
        st.markdown("### Rumus Dasar")
        st.info("BM/Mr = Σ massa atom × jumlah atom")
 
    if st.button("Hitung BM/Mr", use_container_width=True):
        total, detail, error = hitung_bm_mr(rumus)
 
        if error:
            st.error(error)
        else:
            rumus_bersih = rumus.strip().replace(" ", "")
            df = pd.DataFrame(detail)
 
            st.session_state.riwayat.insert(0, {
                "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Rumus": rumus_bersih,
                "BM/Mr": total
            })
 
            st.success("Perhitungan berhasil.")
 
            c1, c2, c3,c4 = st.columns(4)
 
            with c1:
                st.markdown(
                    f"<div class='card'><p>Rumus Kimia</p><div class='metric-value'>{rumus_bersih}</div></div>",
                    unsafe_allow_html=True
                )
 
            with c2:
                st.markdown(
                    f"<div class='card'><p>Total BM/Mr</p><div class='metric-value'>{total}</div></div>",
                    unsafe_allow_html=True
                )
 
            with c3:
                st.markdown(
                    f"<div class='card'><p>Jumlah Unsur</p><div class='metric-value'>{len(detail)}</div></div>",
                    unsafe_allow_html=True
                )

            with c4:
               golongan_list = ", ".join(sorted(set([d["Golongan"] for d in detail])))
               st.markdown(
                   f"<div class='card'><p>Golongan</p><div class='metric-value'>{golongan_list}</div></div>",
                   unsafe_allow_html=True
               )
         
            st.subheader("Tabel Hasil Perhitungan")
            st.dataframe(df, use_container_width=True, hide_index=True)
 
            st.subheader("Grafik Persentase Massa Unsur")
            st.bar_chart(df.set_index("Simbol Unsur")[["Persentase Massa (%)"]])
 
            st.subheader("Pembahasan Otomatis")
            st.info(buat_pembahasan(rumus_bersih, total, detail))
 
            st.download_button(
                "Download Hasil CSV",
                data=df.to_csv(index=False).encode("utf-8"),
                file_name=f"hasil_bm_mr_{rumus_bersih}.csv",
                mime="text/csv",
                use_container_width=True
            )
 
 
elif menu == "Riwayat Pencarian":
    st.subheader("Riwayat Pencarian")
 
    if len(st.session_state.riwayat) == 0:
        st.warning("Belum ada riwayat pencarian.")
    else:
        df_riwayat = pd.DataFrame(st.session_state.riwayat)
        st.dataframe(df_riwayat, use_container_width=True, hide_index=True)
 
        if st.button("Hapus Riwayat"):
            st.session_state.riwayat = []
            st.rerun()
 
 
elif menu == "Chatbot Mini":
    st.subheader("Chatbot Mini BM/Mr")
 
    pertanyaan = st.text_input("Tulis pertanyaan")
 
    if st.button("Kirim"):
        jawaban = chatbot_jawab(pertanyaan)
        st.session_state.chat.append({
            "user": pertanyaan,
            "bot": jawaban
        })
 
    for chat in reversed(st.session_state.chat):
        st.markdown(
            f"<div class='chat-user'><b>Anda:</b> {chat['user']}</div>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<div class='chat-bot'><b>Bot:</b> {chat['bot']}</div>",
            unsafe_allow_html=True
        )
 
 
elif menu == "Database Unsur":
    st.subheader("Database Unsur")
 
    keyword = st.text_input("Cari unsur")
 
    df_unsur = pd.DataFrame([
        {
            "Simbol": simbol,
            "Nama Unsur": data["nama"],
            "Nomor Atom": data["nomor_atom"],
            "Golongan": data["golongan"],
            "Massa Atom": data["massa_atom"]
        }
        for simbol, data in unsur.items()
    ])
 
    if keyword:
        keyword = keyword.lower()
        df_unsur = df_unsur[
            df_unsur["Simbol"].str.lower().str.contains(keyword)
            | df_unsur["Nama Unsur"].str.lower().str.contains(keyword)
        ]
 
    st.dataframe(df_unsur, use_container_width=True, hide_index=True)
 
st.caption("Aplikasi Kalkulator BM/Mr Kimia berbasis Streamlit.")

