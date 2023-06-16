# Python gif converter

from moviepy.editor import *

# videoyu yükleyelim
clip = VideoFileClip("myvideo.mp4")

# videonun ilk 3 saniyesini getirelim.
clip = clip.subclip(0, 3)

# videoyu gif olarak kayıt edelim.
clip.write_gif("mygif.gif")