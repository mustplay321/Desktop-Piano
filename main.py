# Desktop Piano
# Kaden Christie
# Last Updated 2/10/23

#Libraries
import turtle as trtl
import turtle as tortle
import turtle as turt
from pygame import mixer

mixer.init()

#Variables
    #Screen/Piano
phil = trtl.Turtle()
wn = trtl.Screen()
wn.tracer(False)
piano = 'Pianonew.GIF'
wn.addshape(piano)
phil.hideturtle()
pianoX = 0
pianoY = 0
keys = ['C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 0]
keyboardKeys = ['A','S','D','F','G','H','J','K','L','P',0]

    #Writer
writer = tortle.Turtle()
writerX = -250
writerY = -110
writerColor = "black"
writerFont = "Arial", 25, "bold"
writerFontKeyboard = "Arial",45
currentLetter = keys.pop(0)
writerInterval = 51

    #Notes
left = "LeftKeyDown.gif"
middle = "MiddleKeyDown.gif"
right = "RightKeyDown.gif"
wn.addshape(left)
wn.addshape(middle)
wn.addshape(right)

currentNote = turt.Turtle()
currentNote.shape('circle')
currentNote.penup()
currentNote.speed(0)
currentNote.showturtle()
currentNote.color("red")
noteInterval = 55
noteX = -235
noteY = 120

#Turtle setup
writer.hideturtle()
writer.shape('classic')
writer.color(writerColor)
writer.penup()
writer.goto(writerX,writerY + 10)

#Functions
def drawPiano(currentpiano): #draws the piano and letters
    global pianoX
    global pianoY
    global piano
    global keys
    global currentLetter
    wn.tracer(False)
    phil.goto(pianoX,pianoY)
    phil.shape(currentpiano)
    phil.stamp()
    currentNote.goto(noteX, noteY)
    writer.goto(writerX, writerY - 50)
    wn.bgcolor('darkorchid')
    for cookie in range(10):
        writeKeyboardLetter()

def writeKeyboardLetter(): #draws white keys that correspond to piano keys
    wn.tracer(False)
    global currentLetter
    global writerInterval
    currentLetter = keyboardKeys.pop(0)
    writer.write(currentLetter, font=(writerFontKeyboard))
    writer.forward(writerInterval)

def moveNoteC3():
    currentNote.goto(noteX, noteY)
    mixer.music.load('c3.mp3')
    mixer.music.play()

def moveNoteD3():
    currentNote.goto(noteX + noteInterval, noteY)
    mixer.music.load('d3.mp3')
    mixer.music.play()

def moveNoteE3():
    currentNote.goto(noteX + noteInterval * 2, noteY)
    mixer.music.load('e3.mp3')
    mixer.music.play()

def moveNoteF3():
    currentNote.goto(noteX + noteInterval * 3, noteY)
    mixer.music.load('f3.mp3')
    mixer.music.play()

def moveNoteG3():
    currentNote.goto(noteX + noteInterval * 4 - 20, noteY)
    mixer.music.load('g3.mp3')
    mixer.music.play()
    
def moveNoteA3():
    currentNote.goto(noteX + noteInterval * 5 - 20, noteY)
    mixer.music.load('a3.mp3')
    mixer.music.play()

def moveNoteB3():
    currentNote.goto(noteX + noteInterval * 6 - 20, noteY)
    mixer.music.load('b3.mp3')
    mixer.music.play()
    
def moveNoteC4():
    currentNote.goto(noteX + noteInterval * 7 - 20, noteY)
    mixer.music.load('c4.mp3')
    mixer.music.play()

def moveNoteD4():
    currentNote.goto(noteX + noteInterval * 8 - 25, noteY)
    mixer.music.load('d4.mp3')
    mixer.music.play()

def moveNoteE4():
    currentNote.goto(noteX + noteInterval * 9 - 20, noteY)
    mixer.music.load('e4.mp3')
    mixer.music.play()

#Events
drawPiano(piano)
wn.tracer(True)

wn.onkeypress(moveNoteC3, 'a')
wn.onkeypress(moveNoteD3, 's')
wn.onkeypress(moveNoteE3, 'd')
wn.onkeypress(moveNoteF3, 'f')
wn.onkeypress(moveNoteG3, 'g')
wn.onkeypress(moveNoteA3, 'h')
wn.onkeypress(moveNoteB3, 'j')
wn.onkeypress(moveNoteC4, 'k')
wn.onkeypress(moveNoteD4, 'l')
wn.onkeypress(moveNoteE4, 'p')

wn.listen()
wn.mainloop()