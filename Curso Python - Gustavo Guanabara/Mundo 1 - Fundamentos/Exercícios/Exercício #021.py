# Desafios 21

from pygame import mixer

mixer.init()

mixer.music.load('abc.mp3')

mixer.music.play()

input('Digite para desligar.')