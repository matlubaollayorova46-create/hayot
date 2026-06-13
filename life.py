import tkinter as tk
from tkinter import messagebox, scrolledtext

# --- OOP: Klass yaratish ---
class SongGeneratorAI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Music Composer v1.0")
        self.root.geometry("600x700")
        self.root.configure(bg="#121212")  # To'q rangli mavzu (Dark mode)

        self.create_widgets()

    def create_widgets(self):
        """Interfeys elementlarini yaratish"""
        
        # Sarlavha
        self.label_title = tk.Label(
            self.root, text="🎵 AI Qo'shiq Yaratuvchi",
            font=("Helvetica", 24, "bold"), fg="#1DB954", bg="#121212", pady=20
        )
        self.label_title.pack()

        # Yo'riqnoma
        self.label_hint = tk.Label(
            self.root, text="Mavzu yoki kalit so'zni kiriting:",
            font=("Arial", 12), fg="#FFFFFF", bg="#121212"
        )
        self.label_hint.pack(pady=5)

        # Kiritish maydoni (Entry)
        self.topic_entry = tk.Entry(
            self.root, font=("Arial", 14), width=30, 
            bg="#282828", fg="white", insertbackground="white", borderwidth=0
        )
        self.topic_entry.pack(pady=10, ipady=8)
        self.topic_entry.focus()

        # Tugma (Button)
        self.generate_btn = tk.Button(
            self.root, text="Qo'shiq yaratish", command=self.generate_song,
            font=("Arial", 12, "bold"), bg="#1DB954", fg="white",
            activebackground="#1ed760", cursor="hand2", width=20, bd=0
        )
        self.generate_btn.pack(pady=20)

        # Natija ko'rsatish maydoni (ScrolledText)
        self.result_area = scrolledtext.ScrolledText(
            self.root, font=("Georgia", 13, "italic"), width=50, height=18,
            bg="#181818", fg="#B3B3B3", borderwidth=0, padx=10, pady=10
        )
        self.result_area.pack(pady=10)

        # Pastki qism
        self.footer = tk.Label(
            self.root, text="Powered by Gemini AI Technology",
            font=("Arial", 8), fg="#535353", bg="#121212"
        )
        self.footer.pack(side="bottom", pady=10)

    def generate_song(self):
        """Mantiqiy qism: Qo'shiq matnini generatsiya qilish"""
        topic = self.topic_entry.get().strip()
        
        if not topic:
            messagebox.showwarning("Xato", "Iltimos, avval so'z kiriting!")
            return

        self.result_area.delete(1.0, tk.END)
        self.result_area.insert(tk.END, f"'{topic}' mavzusida qo'shiq tayyorlanmoqda...\n\n" + "-"*30 + "\n\n")

        # Sun'iy intellekt "mantiqi" (Simulyatsiya)
        # Haqiqiy API bo'lmagani uchun shablon asosida ajoyib matn tuzamiz
        lyrics = self.compose_lyrics(topic)
        self.result_area.insert(tk.END, lyrics)

    def compose_lyrics(self, word):
        """Qo'shiq matni tuzuvchi algoritm"""
        # Bu yerda sun'iy intellekt algoritmi ishlashi mumkin
        text = f"""[Naqarot]
Oh, {word}, qalbimning sadosi sanan,
Samolardan tushgan nurli bir makon.
Har bir harfingda bor ming bitta ma'no,
Dunyo bo'ylab senga bo'larman shaydo.

[1-kuplet]
Tong otganda eslaganim sensan o'zing,
Ko'zlarimda porlar sening har bir so'zing.
Hayot yo'llarida izlagan choram,
{word} bilan butun bo'lar bu olam.

[2-kuplet]
Vaqt o'tsa ham o'chmas sening izlaring,
Yulduzlardan baland sening bo'ylaring.
Men kuylayman dildan sening madhingni,
Anglatarsan menga baxtning qadrini.

[Xotima]
Faqat {word}... faqat sen...
Abadiy qolasan yuragimda man..."""
        return text

# --- Dasturni ishga tushirish ---
if __name__ == "__main__":
    root = tk.Tk()
    app = SongGeneratorAI(root)
    root.mainloop()