from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from tkinter import messagebox
from tkinter import Toplevel
from tkinter import Text
from tkinter import Radiobutton
from tkinter import DoubleVar
from tkinter import Label
import random

# Path relatif ke assets
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Achmad Roykhan Sabiq\OneDrive\Dokumen\kuliah\KCB\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Fungsi keluar aplikasi
def exit_application():
    window.destroy()
    
gejala = {
    "G1": "Kualitas telur jelek",
    "G2": "Mencret bercampur darah",
    "G3": "Kelihatan ngantuk dan bulu berdiri",
    "G4": "Produksi telur menurun",
    "G5": "Tidur paruhnya turun ke bawah",
    "G6": "Bersin bersin",
    "G7": "Sayap menggantung",
    "G8": "Duduk membungkuk",
    "G9": "Kaki pincang",
    "G10": "Pembengkakan dari sinus dan mata",
    "G11": "Keluar nanah dari mata",
    "G12": "Mencret keputih-putihan",
    "G13": "Sempoyongan",
    "G14": "Kelopak mata kemerahan",
    "G15": "Mencret kehijauan",
    "G16": "Diare",
    "G17": "Muka pucat",
    "G18": "Napas cepat",
    "G19": "Tampak lesu",
    "G20": "Bulu kusam dan mengkerut",
    "G21": "Badan kurus",
    "G22": "Nafsu makan berkurang",
}

cf_bawaan = {
    "Tipus Ayam": {"G3": 0.85, "G15": 0.4, "G16": 0.4, "G19": 0.35, "G20": 0.4, "G21": 0.25, "G22": 0.25},
    "Berak Darah": {"G2": 0.9, "G4": 0.5, "G17": 0.4, "G20": 0.45, "G21": 0.35, "G22": 0.35},
    "Salesma Ayam": {"G4": 0.4, "G6": 0.8, "G10": 0.7, "G11": 0.6, "G14": 0.5, "G16": 0.35, "G22": 0.3},
    "Gumboro": {"G5": 0.85, "G8": 0.7, "G12": 0.6, "G19": 0.4, "G20": 0.35, "G22": 0.2},
    "Mareks": {"G7": 0.8, "G9": 0.7, "G13": 0.6, "G17": 0.4, "G18": 0.35, "G21": 0.3, "G22": 0.3},
    "Produksi Telur": {"G1": 0.9, "G4": 0.85, "G15": 0.5, "G18": 0.4},
}

def calculate_cf(answers):
    diagnosis = {}
    for penyakit, gejala_penyakit in cf_bawaan.items():
        cf_rule = 0
        for gejala_id, cf_gejala in gejala_penyakit.items():
            cf_user = answers.get(gejala_id, 0)  # CF pengguna untuk gejala ini
            cf_current = cf_user * cf_gejala    # CF hasil perkalian
            cf_rule = cf_rule + cf_current * (1 - cf_rule)  # Kombinasi CF
        diagnosis[penyakit] = cf_rule * 100
    return diagnosis

# Fungsi untuk mendapatkan pertanyaan berikutnya
def get_next_question(answers, relevant_gejala):
    remaining_gejala = relevant_gejala - set(answers.keys())
    if remaining_gejala:
        return random.choice(list(remaining_gejala))
    return None

# Fungsi untuk menampilkan hasil
def show_results(answers, expert_window):
    # Cek jika semua jawaban adalah "Tidak" (0)
    if all(cf == 0 for cf in answers.values()):
        messagebox.showinfo(
            "Hasil Diagnosa",
            "Ayam anda tidak terdiagnosa tipus ayam, berak darah, salesma ayam, gumboro, mareks, maupun produksi telur."
        )
        expert_window.destroy()
        return

    # Hitung CF untuk setiap penyakit
    diagnosis = calculate_cf(answers)
    max_penyakit, max_cf = max(diagnosis.items(), key=lambda x: x[1])

    if max_cf > 0:
        if max_penyakit == "Tipus Ayam":
            hasil_text = (
                f"Ayam anda kemungkinan {max_cf:.2f}% didiagnosa terkena penyakit {max_penyakit}. Dianjurkan untuk membersihkan kandang secara rutin, vaksinasi, gunakan induk yang bebas dari infeksi Salmonella pullorum, pisahkan ayam yang baru dibeli atau menunjukkan gejala dari populasi utama."
                f" Antibiotik yang dapat digunakan adalah Sulfaquinoxaline, Furazolidone, atau obat lain yang direkomendasikan oleh dokter hewan."
            )
        elif max_penyakit == "Berak Darah":
            hasil_text = (
                f"Ayam anda kemungkinan {max_cf:.2f}% didiagnosa terkena penyakit {max_penyakit}. Dianjurkan untuk membersihkan feses secara teratur, jaga kandang tetap kering, pastikan pakan dan air bersih, vaksinasi, dan berikan profilaksis."
                f" Pengobatan untuk berak darah pada ayam adalah menggunakan obat amprolium, Sulfaquinoxaline, atau Toltrazuril. Berikan juga vitamin dan elektrolit serta konsultasi dengan dokter hewan."
            )
        elif max_penyakit == "Salesma Ayam":
            hasil_text = (
                f"Ayam anda kemungkinan {max_cf:.2f}% didiagnosa terkena penyakit {max_penyakit}. Dianjurkan untuk menjaga kebersihan dan ventilasi kandang, hindari kepadatan ayam terlalu tinggi, vaksinasi, isolasi ayam yang terinfeksi, dan berikan probiotik."
                f" Antibiotik yang dapat digunakan adalah tylosin, tiamulin, atau doxycyline, serta erythoromycin. Berikan vitamin dan mineral serta konsultasi dengan dokter hewan."
            )
        elif max_penyakit == "Gumboro":
            hasil_text = (
                f"Ayam anda kemungkinan {max_cf:.2f}% didiagnosa terkena penyakit {max_penyakit}. Dianjurkan untuk melakukan vaksinasi, bersihkan kandang secara rutin menggunakan disinfektan, hindari kontaminasi silang dari kandang atau peternakan lain, dan hindari stres pada ayam."
                f" Tidak ada pengobatan langsung untuk gumboro karena disebabkan oleh virus. Namun, tindakan suportif dapat membantu ayam yang terinfeksi dengan memeberikan elektrolit dan vitamin, antibiotik, dan lakukan isolasi."
            )
        elif max_penyakit == "Mareks":
            hasil_text = (
                f"Ayam anda kemungkinan {max_cf:.2f}% didiagnosa terkena penyakit {max_penyakit}. Dianjurkan untuk melakukan vaksinasi, bersihkan kandang secara rutin menggunakan disinfektan, hindari kontaminasi silang dari kandang atau peternakan lain, dan hindari stres pada ayam."
                f" Tidak ada pengobatan langsung untuk gumboro karena disebabkan oleh virus. Namun, tindakan suportif dapat membantu ayam yang terinfeksi dengan memeberikan vitamin, antibiotik, dan lakukan isolasi."
            )
        elif max_penyakit == "Produksi Telur":
            hasil_text = (
                f"Ayam anda kemungkinan {max_cf:.2f}% didiagnosa terkena penyakit {max_penyakit}. Dianjurkan untuk rutin vaksinasi, perawatan lingkungan, gunakan pakan berkualitas, lakukan pemeriksaan rutin."
            )
    else:
        hasil_text = (
            "Ayam anda tidak terdiagnosa tipus ayam, berak darah, salesma ayam, gumboro, mareks, maupun produksi telur."
        )

    messagebox.showinfo("Hasil Diagnosa", hasil_text)
    expert_window.destroy()  # Pastikan jendela ditutup

    
def ask_question(question_label, answer_var, answers, relevant_gejala, expert_window):
    global current_question
    if current_question:
        # Simpan jawaban pengguna
        user_cf = answer_var.get()
        answers[current_question] = user_cf

        # Update gejala relevan jika CF >= 0.5
        if user_cf >= 0.5:
            related_rules = [penyakit for penyakit, gejalas in cf_bawaan.items() if current_question in gejalas]
            relevant_gejala = set()
            for penyakit in related_rules:
                relevant_gejala.update(cf_bawaan[penyakit].keys())
            relevant_gejala -= set(answers.keys())  # Hapus gejala yang sudah dijawab

    # Pilih pertanyaan berikutnya
    current_question = get_next_question(answers, relevant_gejala)
    if current_question:
        question_label.config(text=f"Apakah ayam bergejala {gejala[current_question]}?")
        answer_var.set(0)
    else:
        show_results(answers, expert_window)  # Tambahkan expert_window


# Fungsi untuk membuka sistem pakar
def open_expert_system():
    global current_question, relevant_gejala
    current_question = None
    relevant_gejala = set(gejala.keys())
    answers = {}

    # Buat jendela baru sebagai Toplevel
    expert_window = Toplevel(window)
    expert_window.title("Sistem Pakar Penyakit Ayam")
    expert_window.geometry("500x400")

    # Label untuk menampilkan status sistem pakar
    label = Label(expert_window, text="Sistem Pakar Dimulai!", font=("Arial", 16))
    label.pack(pady=20)

    # Label untuk pertanyaan
    question_label = Label(expert_window, text="", font=("Arial", 14), wraplength=400)
    question_label.pack(pady=20)

    # Radio button untuk jawaban
    answer_var = DoubleVar()
    options = [("Tidak", 0), ("Tidak Seberapa", 0.25), ("Lumayan", 0.5), ("Lumayan Parah", 0.75), ("Iya", 1)]
    for text, value in options:
        rb = Radiobutton(expert_window, text=text, variable=answer_var, value=value, font=("Arial", 12))
        rb.pack(anchor="w")

    # Tombol untuk melanjutkan
    next_button = Button(
        expert_window, 
        text="Lanjut", 
        command=lambda: ask_question(question_label, answer_var, answers, relevant_gejala, expert_window),
        bg="blue", 
        fg="white"
    )
    next_button.pack(pady=20)

    # Mulai pertanyaan pertama
    current_question = random.choice(list(gejala.keys()))
    question_label.config(text=f"Apakah ayam bergejala {gejala[current_question]}?")

    


# Main window
window = Tk()
window.title("Sistem Pakar Penyakit Ayam")
window.geometry("500x300")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=300,
    width=500,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Tambahkan teks dan elemen lain
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(250.0, 22.0, image=image_image_1)

canvas.create_text(
    170.0,
    13.0,
    anchor="nw",
    text="Sistem Pakar Penyakit Ayam",
    fill="#000000",
    font=("Jost Medium", 12 * -1)
)

# Tombol mulai
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_expert_system,  # Panggil sistem pakar
    relief="flat"
)
button_1.place(
    x=150.0,
    y=105.0,
    width=200.0,
    height=45.0
)

# Tombol keluar
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=exit_application,  # Keluar dari aplikasi
    relief="flat"
)
button_2.place(
    x=150.0,
    y=180.0,
    width=200.0,
    height=45.0
)

window.resizable(False, False)
window.mainloop()