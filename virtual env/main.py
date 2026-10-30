from flask import Flask
import random

app = Flask(__name__)

facts_list = ["Kebanyakan orang yang menderita kecanduan teknologi mengalami stres yang kuat ketika mereka berada di luar area jangkauan jaringan atau tidak dapat menggunakan perangkat mereka",
"Menurut sebuah studi yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka bergantung pada ponsel pintar mereka.",
"Studi tentang ketergantungan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan",
"Menurut sebuah studi tahun 2019, lebih dari 60% orang merespons pesan pekerjaan di ponsel mereka dalam waktu 15 menit setelah pulang kerja",
"Salah satu cara untuk memerangi ketergantungan teknologi adalah dengan mencari kegiatan yang membawa kesenangan dan meningkatkan suasana hati"]

@app.route("/")
def fact():
    return f'<p>{random.choice(facts_list)}</p>'

coin = ["kepala","ekor"]

@app.route("/rahasia")
def koin():
    return f'<p>{random.choice(coin)}</p>'


app.run(debug=True)