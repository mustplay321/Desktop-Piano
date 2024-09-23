#TODO
'''Play sound when corresponding key on the keyboard is pressed
        -will require audio files
    Make key fill gray when pressed
    Add Black keys
    
    OPTIONAL:
    Allow for holding a key down
'''

#Libraries
import turtle as trtl
import turtle as tortle
import turtle as c3
import turtle as d3
import turtle as e3
import turtle as f3
import turtle as g3
import turtle as a3
import turtle as b3
import turtle as c4
import turtle as d4
import turtle as e4
#from playsound import playsound

#Variables
    #Screen/Piano
phil = trtl.Turtle()
wn = trtl.Screen()
piano = 'Pianonew.GIF'
wn.addshape(piano)
wn.tracer(False)
pianoX = 0
pianoY = 0
phil.hideturtle()
keys = ['C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 0]
keyboardKeys = ['A','S','D','F','G','H','J','K','L',';',0]
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
c3trtl = c3.Turtle()
d3trtl = d4.Turtle()
e3trtl = e3.Turtle()
f3trtl = f3.Turtle()
g3trtl = g3.Turtle()
a3trtl = a3.Turtle()
b3trtl = b3.Turtle()
c4trtl = c4.Turtle()
d4trtl = d4.Turtle()
e4trtl = e4.Turtle()

c3trtl.shape(left)
d3trtl.shape(middle)
e3trtl.shape(right)
f3trtl.shape(left)
g3trtl.shape(middle)
a3trtl.shape(middle)
b3trtl.shape(right)
c4trtl.shape(left)
d4trtl.shape(middle)
e4trtl.shape(right)

#Turtle setup
writer.hideturtle()
writer.shape('classic')
writer.color(writerColor)
writer.penup()
writer.goto(writerX,writerY + 10)


#Functions
def drawPiano(): #draws the piano and letters
    global pianoX
    global pianoY
    global piano
    global keys
    global currentLetter
    wn.tracer(False)
    phil.goto(pianoX,pianoY)
    phil.shape(piano)
    phil.stamp()

    c3trtl.hideturtle()
    c3trtl.pendown()
    c3trtl.goto(pianoX - 229,pianoY)
    d3trtl.hideturtle()
    d3trtl.pendown()
    d3trtl.goto(pianoX - 178,pianoY)
    e3trtl.hideturtle()
    e3trtl.pendown()
    e3trtl.goto(pianoX - 127,pianoY)
    f3trtl.hideturtle()
    f3trtl.pendown()
    f3trtl.goto(pianoX - 76,pianoY)
    g3trtl.hideturtle()
    g3trtl.pendown()
    g3trtl.goto(pianoX - 25,pianoY)
    a3trtl.hideturtle()
    a3trtl.pendown()
    a3trtl.goto(pianoX + 26,pianoY)
    b3trtl.hideturtle()
    b3trtl.pendown()
    b3trtl.goto(pianoX + 77,pianoY)
    c4trtl.hideturtle()
    c4trtl.pendown()
    c4trtl.goto(pianoX + 128,pianoY)
    d4trtl.hideturtle()
    d4trtl.pendown()
    d4trtl.goto(pianoX + 179,pianoY)
    e4trtl.hideturtle()
    e4trtl.pendown()
    e4trtl.goto(pianoX + 230,pianoY)

    writer.goto(writerX, writerY - 50)
    for cookie in range(10):
        writeKeyboardLetter()

def writeKeyboardLetter(): #draws white keys that correspond to piano keys
    wn.tracer(False)
    global currentLetter
    global writerInterval
    currentLetter = keyboardKeys.pop(0)
    writer.write(currentLetter, font=(writerFontKeyboard))
    writer.forward(writerInterval)

def playNote(active_sound,active_note):
    active_note.stamp()
    #playsound(active_sound)
    active_note.clear()

#Events
drawPiano()
wn.tracer(True)

'''wn.onkeypress(playNote("C3.wav",c3trtl),'a')
wn.onkeypress(playNote("D3.wav","d3trtl),'s')
wn.onkeypress(playNote("E3.wav","e3trtl),'d')
wn.onkeypress(playNote("F3.wav",f3trtl),'f')
wn.onkeypress(playNote("G3.wav",g3trtl),'g')
wn.onkeypress(playNote("A3.wav",a3trtl),'h')
wn.onkeypress(playNote("B3.wav",b3trtl),'j')
wn.onkeypress(playNote("C4.wav",c4trtl), 'k')
wn.onkeypress(playNote("D4.wav",d4trtl), 'l')
wn.onkeypress(playNote("E4.wav",e4trtl),';')'''

wn.listen()
wn.mainloop()