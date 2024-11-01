#tutor agar tidak error
#pip install spacy
#python -m spacy download en_core_web_sm
#pip install tk

import tkinter as tk
from tkinter import scrolledtext
import random
import spacy

nlp = spacy.load("en_core_web_sm")

patterns = {
    #sapaan
    "hi":["Hi!","Aloha","yo"],
    "hai" :["Hai! Ada yang bisa aku bantu?","Gimana, apa cerita?","Ada apa ini ?"],
    "halo" : ["Iya, halo.","Halo jugaaa :)","Yaa, ada yang bisa dibantu?","Halooo, aku siap mendengar cerita mu yang menakjubkan!"],
    "hello" : ["Aku disini! Ada yang bisa aku bantu?","Heloo, cerita apa kali ini?"],
    "makasih": ["ya sama-sama","Okeyyy","Jangan khawatir, senang mengobrol dengan mu!","Tidak masalah, saya senang bisa memberikan dukungan"],
    "thanks" :  ["Sama-sama, senang rasanya bisa membuat mu merasa lebih baik","Senang bisa membantu mu","Anda selalu dipersilakan jika ingin curhat" "Jangan ragu untuk bertanya jika ada yang diperlukan, anda selalu dipersilahkan"],
    "terima kasih" : ["Terimakasih juga telah memilih ku sebagai teman curhat mu. Ingat! Jangan pernah berkecil hati dan teruslah melakukan apa yang menurutmu benar!","Senang bisa memberikan kontribusi. Jika Anda membutuhkan bantuan lagi, saya di sini"],
    "sampai jumpa" : ["Terima kasih sudah mengobrol. Sampai jumpa lagi!","Sampai jumpa lagi!"],

    #minta
    "mau curhat dong": ["Ceritakan pada ku semuanya! Aku disini siap mengatasi keresahan mu.","Ceritakan hal yang membuat mu resah! Mungkin aku punya solusinya.","Curhatkan saja kepada ku, aku dibuat untuk membantu mu"],
    "saya bosen kasih saran dong ": ["Yukkk Nonton!","Membaca novel seru loh. Banyak hal yang bisa kita dapat juga dari cerita-cerita novel!","Ngopi dengan teman mu bisa membuat waktu bosan mu menjadi seru loh!"],
    "Selain itu ada gak" : ["Bermain game mungkin bisa menghilangkan rasa bosen mu","Membaca komik jugak bisa menghilangkan rasa jenuh mu"],
    "saran makanan penambah mood": ["Makan Makanan pedas seperti Seblak atau Nasi Goreng mungkin bisa membuat mu merasa lebih bersemangat","Hari-hari mu sibuk dan cuaca sedang panas? Mungkin Ice Cream bisa membuat diri mu lebih adem dan rileks"],
    "gombalin aku dong": ["ehemm siap ya!, ada satu tinta yang gak bisa di hapus di dunia ini .iya tintaku padamu <3","jika aku bisa kembali ke 20 oktober hari sumpah pemuda maka aku akan menulis sumpah aku mencintaimu"],
    "kasih lelucon dong " :["kendaraan apa yang paling imut? jawabanya kereta api cute cutee","kenapa air mata warnanya bening kalau hijau air matcha"],
    "apa ya hal yang membuat bahagia":['Maafkan aku mungkin aku tidak bisa memberi mu solusi spesifik untuk pertanyaan mu, karena bahagia nya setiap orang itu pasti berbeda-beda.'],
    "Rekomendasi game dong":['Ada seperti Game Toram Online mungkin bisa membuat mu merasa seperti hidup di zaman abad pertengahan',"Jiwa kamu kompetitif? Mungkin kamu bisa coba memainkan Mobile Legends atau PUBG untuk mengisi waktu luang mu"],
    "Selain itu game" : ["Kalau kamu suka game bergenre fighter maka Tekken atau Mortal Kombat adalah jawabannya","Ingin merasakan seperti apa dunia di tahun 2077, coba mainkan Cyberpunk2077","Kalau kamu suka game RPG seperti Skyrim, coba deh The Witcher 3 : Wild Hunt.Saya jamin kamu bakal ketagihan"],
    "Rekomendasi Kegiatan harian":['Bersih-bersih akan menjadi kegiatan yang sangat bermanfaat untuk dilakukan setiap hari',"Mencatat peristiwa-peristiwa yang kamu alami mungkin bisa menjadi ide yang bagus untuk mengabadikan pengalam mu"],
    "Rekomendasi tempat bagus":['Pantai akan sangat bagus jika kamu ingin mencari angin segar sambil melihat lautan yang luas',"Puncak gunung akan menjadi tempat yang sangat bagus jika kamu ingin bersantai dan menikmati udara yang sejuk"],


    #feelings
    "saya merasa kesepian": ["Mungkin kamu bisa mencari teman atau pasangan agar hari-hari mu terasa lebih ramai","Cobalah untuk bersosialisasi dan mencari teman. Aku yakin hari-hari mu tidak kesepian lagi","Mencari teman yang se-hobi adalah pilihan yang tepat untuk meramaikan hari-harimu"],
    "saya sedang stres karena pekerjaan": ["Ambillah beberapa hari untuk cuti dan pergi kemanapun yang kamu suka!","Melakukan hal-hal yang kamu sukai di waktu luang mu mungkin bisa melepaskan stres mu"],
    "saya merasa cemas tentang masa depan": ["Cobalah untuk mencatat apa-apa saja yang menjadi tujuan mu di masa depan dan lakukan cara untuk meraih nya.\nMungkin dengan itu kamu bisa menjalani hari-hari mu dengan lebih semangat karena memiliki tujuan","Cemas tentang masa depan adalah suatu hal wajar, tetapi coba untuk tidak membiarkannya menguasai pikiran Anda. Fokus pada langkah kecil yang dapat diambil untuk meraih tujuan Anda","Saat Anda cemas tentang masa depan, coba untuk menulis rencana yang konkret dan mengambil tindakan yang dapat membantu Anda merasa lebih siap menghadapi apa pun yang akan datang"],
    "saya merasa sedih": ["Ketika Anda merasa sedih, penting untuk memberi diri Anda waktu untuk berduka","Coba lakukan aktivitas yang Anda nikmati dan berbicara dengan seseorang yang Anda percayai","Jika Anda merasa sedih, ingatlah bahwa perasaan itu akan berlalu.Cari dukungan dari teman atau keluarga, dan bahkan bantuan dari profesional jika diperlukan"],                        
    "saya memiliki masalah dalam hubungan": ["Cobalah untuk menyampaikan dengan pikiran terbuka kepada orang yang memiliki masalah dengan mu,\nMungkin dengan begitu kamu dan dia bisa menemukan jalan tengah nya","Berkonsultasi lah dengan orang tua mu. Karena orang tua mu pasti memiliki sebuah solusi dari pengalaman nya yang banyak"],
    "saya bingung":["Apa yang membuat mu bingung?","Ceritakan kepadaku! Mungkin aku punya solusi untuk membantu menghilangkan kebingungan itu.","Ada yang bisa aku bantu?"],
    "saya cemburu ": ["Cemburu hanyalah sebuah rasa yang akan membuat mu tertahan di satu tempat. Teruslah berkembang agar sesuatu yang kamu cemburui bisa kamu capai!","Lupakan rasa cemburu mu dan teruslah melangkah maju. Cemburu hanya membuat hidup mu suram"],
    "saya takut" : ["Jangan takut, aku ada disini untuk mu","Ayo beranikan dirimu! Berani adalah langkah awal untuk mencapai sesuatu","Jangan mau menghambat pertumbuhan mu dengan rasa takut.\nCobalah perlahan untuk memberanikan dirimu!"],
    "saya depresi":["kayaknya kamu perlu healing deh jalan jalan gitu","apa yang membuat anda depresi bisa cerita disini"],
    "saya khawatir":["Merasa khawatir dapat membuat kamu kelelahan,kamu perlu cari kegiatan agar lebih tenang atau bisa curhat sama saya?","Ketika Anda sedang khawatir, penting untuk mencoba tetap tenang. Coba identifikasi apa yang membuat Anda khawatir dan cari solusi yang mungkin untuk masalah tersebut"],
    "saya panik": ["Anda harus menenangkan diri anda karena panik bukan hal yang baik","Cobalah untuk mengambil napas dalam-dalam dan hitung sampai sepuluh.Ingatlah bahwa perasaan panik akan mereda seiring waktu","Cobalah lakukan pernapasan dalam-dalam dan fokus pada hal-hal yang dapat Anda kendalikan"],
 
    #respons
    "terserah":['Jangan gitu dong',"Tolong lebih spesifik agar aku bisa mengerti apa yang kamu inginkan."],
    "gpp":[":(","Dry text itu ga baik loh."],
   

    #kejadian
    "saya dibully":["Cobalah untuk melapor kepada guru BK atau orang tua mu","Kamu bisa menjerat mereka dengan pasal perundungan","Ayo lawan! Tunjukkan kalau kamu bukan sekedar mangsa yang mudah!"],
    "saya dikucilkan":["Cobalah untuk berbaur dengan mereka melalui hobi atau sesuatu yang mereka sukai","Jangan bersedih hati! Aku ada disini untuk menemani hari-harimu"],
    "saya melihat hantu":["mungkin saja anda kelelahan","aaaa Takuut","serius?"],
    "saya ditolak": ["uuuuh nice try jangan sedih", "uluhuluh jangan sedih Tuhan bersama kita"],

    #tak dipahami
    "default": [""],
    "help": ["Berikut list acak yang bisa kamu coba denganku"],

}

def respond(message):
    doc = nlp(message)
    matched_response = random.choice(patterns["default"])

    if message.lower() == "help":
        matched_response = "pertanyaan acak ini bisa kamu coba dengankuuuu:\n"
        random_patterns = random.sample(list(patterns.keys()), 5)
        for pattern in random_patterns:
            if pattern != "default" and pattern != "help":
                matched_response += f"- {pattern}\n"
    else:
        for key_phrase in patterns:
            if key_phrase == "default" or key_phrase == "help":
                continue
            key_tokens = nlp(key_phrase)
            if all(token.text.lower() in [t.text.lower() for t in doc] for token in key_tokens):
                matched_response = random.choice(patterns[key_phrase])
                break

    return matched_response

def send_message(event=None):
    user_input = entry.get()
    if user_input:
        conversation.config(state=tk.NORMAL)
        conversation.insert(tk.END, f"You: {user_input}\n", 'user')
        conversation.yview(tk.END)  
        conversation.config(state=tk.DISABLED)

        response = respond(user_input)
        conversation.config(state=tk.NORMAL)
        conversation.insert(tk.END, f"Vera: {response}\n\n", 'bot')
        conversation.yview(tk.END)  
        conversation.config(state=tk.DISABLED)

        entry.delete(0, tk.END)

def show_credits_window():
    credits_window = tk.Toplevel(root)
    credits_window.title("Credits")

    credits_label = tk.Label(credits_window, text="Vera AI\n\nCreated by\nJustin\nVio\nFadjri\nFaqih\n\nStructure Code\nJustin\n\nHelp Menu\nJustin\n\nQuestion Pattern\nVio\nFadjri\n\nAnswer Pattern\nFaqih\nFadjri\n\nDesign\nJustin\nVio\nVersion 1.0")
    credits_label.pack(padx=20, pady=20)

root = tk.Tk()
root.title("Vera AI")

marigold_yellow = "#FFD54F"
marigold_orange = "#FFA000"
marigold_brown = "#8D6E63"
marigold_dark_green = "#388E3C"
marigold_light_green = "#C5E1A5"

root.configure(bg=marigold_yellow)

font_family = "Roboto"
text_font = (font_family, 12)
button_font = (font_family, 13, "bold")
entry_font = (font_family, 13)

conversation = scrolledtext.ScrolledText(root, width=61, height=31, bg=marigold_orange, font=text_font)
conversation.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
conversation.tag_config('bot', foreground='black')
conversation.tag_config('user', foreground='black')
conversation.config(state=tk.DISABLED)

initial_message = "Vera: Haloooo\n(tekan 'help' untuk melihat list pertanyaan yang bisa ditanyakan)\n\n"
conversation.config(state=tk.NORMAL)
conversation.insert(tk.END, initial_message, 'bot')
conversation.config(state=tk.DISABLED)

entry = tk.Entry(root, width=40, font=entry_font, relief=tk.FLAT, bd=2)
entry.grid(row=1, column=0, padx=10, pady=10)

send_button = tk.Button(root, text="Kirim", width=10, command=send_message, bg=marigold_orange, fg=marigold_brown, relief=tk.FLAT, font=button_font)
send_button.grid(row=1, column=1, padx=10, pady=10)

credits_button = tk.Button(root, text="Credits", width=10, command=show_credits_window, bg=marigold_orange, fg="white", relief=tk.FLAT, font=button_font)
credits_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.bind("<Return>", send_message)

def close_window():
    root.destroy()
    exit()

root.protocol("WM_DELETE_WINDOW", close_window)

root.mainloop()
