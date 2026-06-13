import tkinter as tk
from tkinter import messagebox
from random import choice

# Song class, foydalanuvchi kiritgan so'zga asoslangan qo'shiq yaratish
class Song:
    def __init__(self, keyword):
        self.keyword = keyword
        
    def generate_song(self):
        # Kengroq va ko'proq misralarga ega qo'shiq yaratish
        verses = [
            f"Yorug'likdan ko'rgan har bir narsa, {self.keyword} bilan yanada porloq,\n",
            f"{self.keyword} har doim yonimda, yurakda o'zining issiq nafasi,\n",
            f"Shunda hech qanday qorong'ulik bo'lmas, faqat {self.keyword}ni his qilaman,\n",
            f"{self.keyword}dagi sevgi menga kuch bag'ishlaydi,\n",
            f"Chiroyli bir olam bu, {self.keyword} bilan to'la, sog'inchni yo'qotaman.\n"
        ]
        return ''.join(verses)

# Rasmlar yaratish uchun (DALL·E API ishlatish haqida xabar)
def generate_image(keyword):
    # Rasmlar yaratish bo'yicha fikrni faqat tasavvur qiling
    # Bu yerda rasm yaratish kodini yozish mumkin
    # Hozircha, tasodifiy rasmni generatsiya qilish uchun o'zgaruvchi tasavvur qiling
    image_urls = [
        "https://via.placeholder.com/150?text=So'z+rasmi+1",
        "https://via.placeholder.com/150?text=So'z+rasmi+2",
        "https://via.placeholder.com/150?text=So'z+rasmi+3"
    ]
    return choice(image_urls)

# Tkinter interfeysi
class SongGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Qo'shiq Generator")
        self.root.geometry("600x600")
        
        # Kirish maydoni
        self.label = tk.Label(self.root, text="Bir so'z kiriting:", font=("Helvetica", 14))
        self.label.pack(pady=10)
        
        # So'z kiritish maydoni
        self.entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.entry.pack(pady=10)
        
        # Qo'shiqni generatsiya qilish tugmasi
        self.generate_button = tk.Button(self.root, text="Qo'shiqni Yaratish", font=("Helvetica", 14), command=self.generate_song)
        self.generate_button.pack(pady=20)
        
        # Natija uchun matn oynasi
        self.result_text = tk.Text(self.root, height=10, width=50, font=("Helvetica", 12), wrap=tk.WORD)
        self.result_text.pack(pady=10)
        
        # Rasmni ko'rsatish uchun labellar
        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=10)

    def generate_song(self):
        # Foydalanuvchidan kiritilgan so'zni olish
        keyword = self.entry.get().strip()
        
        # Agar so'z kiritilmagan bo'lsa, xabar ko'rsatish
        if not keyword:
            messagebox.showerror("Xatolik", "Iltimos, so'zni kiriting!")
            return
        
        # Song ob'ektini yaratish va qo'shiqni olish
        song = Song(keyword)
        song_lyrics = song.generate_song()
        
        # Rasmlar yaratish
        image_url = generate_image(keyword)

        # Qo'shiqni matn oynasiga chiqarish
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, song_lyrics)

        # Rasmni ko'rsatish
        self.show_image(image_url)
    
    def show_image(self, image_url):
        # Rasmlar URL manzilini ko'rsatish
        # Tkinter yordamida tasvirni olish va ko'rsatish
        self.image_label.config(text=f"Rasm: {image_url}")
        
# Asosiy dastur
if __name__ == "__main__":
    root = tk.Tk()
    app = SongGeneratorApp(root)
    root.mainloop()