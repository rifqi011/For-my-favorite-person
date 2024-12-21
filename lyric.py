import time
from threading import Thread, Lock
import sys
from pygame import mixer

lock = Lock()

# Fungsi untuk animasi teks
def textAnimation(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

# Fungsi untuk animasi lirik
def lyricSing(lyric, delay, speed):
    time.sleep(delay)
    textAnimation(lyric, speed)

# Fungsi utama untuk sinkronisasi lirik dan lagu
def sing():
    # Lirik lagu
    lyrics = [
        ("Maukah lagi kau mengulang ragu", 0.1),
        ("Dan sendu yang lama", 0.1),
        ("Dia yang dulu pernah bersamamu", 0.1),
        ("Memahat kecewa", 0.1),
        ("Atau kau inginkan yang baru", 0.1),
        ("Sungguh menyayangimu", 0.1),
        ("Aku ingin dirimu", 0.1),
        ("Yang menjadi milikku", 0.1),
        ("Bersamaku mulai hari ini", 0.1),
        ("Hilang ruang untuk cinta yang lain", 0.1),
        ("Separuh jalan pernah dilewati", 0.1),
        ("Meski ada kecewa", 0.1),
        ("Aku yang dulu tak begitu lagi", 0.1),
        ("Tak kan kuulangi", 0.1),
        ("Jangan dulu engkau berpaling", 0.1),
        ("Beriku kesempatan", 0.1),
        ("Aku ingin dirimu", 0.1),
        ("Tetap jadi milikku", 0.1),
        ("Bersamaku mulai hari baru", 0.1),
        ("Hilang ruang untuk cinta yang lain", 0.1),
        ("Lupakan dia pergi denganku", 0.1),
        ("Lupakan lah ragu denganku", 0.1),
        ("Aku ingin dirimu", 0.1),
        ("Tetap jadi milikku", 0.1),
        ("Jangan ulangi ragu", 0.1),
        ("Bersamaku mulai hari baru", 0.1),
        ("Hilang ruang untuk cinta yang lain", 0.1),
        ("Aku ingin dirimu", 0.1),
        ("Tuk menjadi milikku", 0.1),
        ("Setengah jalanmu denganku", 0.1),
        ("Bersamaku mulai hari ini", 0.1),
        ("Hilang ruang untuk cinta yang lain", 0.1),
        ("Layak untuk cantikmu itu aku", 0.1),
        ("I LOVE YOU ❤️🌟", 1)
    ]

    # Sinkronisasi waktu lirik
    delays = [
        11.0, 15.5, 21.0, 25.0, 29.2, 34.5, 39.4, 44.0, 49.0, 53.0,
        66.0, 70.7, 75.0, 80.2, 84.4, 90.0, 97.0, 101.5, 106.4, 111.0, 116.0, 121.0,
        145.0, 150.0, 152.5, 154.6, 159.1, 162.0, 167.0, 169.0, 171.5,
        176.0, 183.0, 200
    ]

    # Mulai lagu
    mixer.init()
    mixer.music.load("song.mp3")  # lagu
    mixer.music.play()

    # Animasi lirik
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=lyricSing, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

    mixer.music.stop()

if __name__ == "__main__":
    sing()
