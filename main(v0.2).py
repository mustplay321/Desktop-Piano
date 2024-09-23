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
import turtle as c3trtl
#from playsound import playsound

#Variables
    #Screen/Piano
phil = trtl.Turtle()
wn = trtl.Screen()
piano = 'Piano.gif'
noteDown = "C3Down.gif"
wn.addshape(piano)
wn.addshape(noteDown)
wn.addshape("D3Down.gif")
wn.addshape("E3Down.gif")
wn.addshape("F3Down.gif")
wn.addshape("G3Down.gif")
wn.addshape("A3Down.gif")
wn.addshape("B3Down.gif")
wn.addshape("C4Down.gif")
wn.addshape("D4Down.gif")
wn.addshape("E4Down.gif")
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
note = c3trtl.Turtle()
note.shape(noteDown)

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
    note.hideturtle()
    note.pendown()
    note.goto(pianoX,pianoY)
    for letter in range(10):
        writePianoLetter()
    writer.goto(writerX, writerY - 50)
    for cookie in range(10):
        writeKeyboardLetter()

def writePianoLetter(): #draws letter for each keyboard key
    wn.tracer(False)
    global currentLetter
    global writerInterval
    writer.write(currentLetter, font=(writerFont))
    writer.forward(writerInterval)
    currentLetter = keys.pop(0)

def writeKeyboardLetter(): #draws white keys that correspond to piano keys
    wn.tracer(False)
    global currentLetter
    global writerInterval
    currentLetter = keyboardKeys.pop(0)
    writer.write(currentLetter, font=(writerFontKeyboard))
    writer.forward(writerInterval)

def playNote(active_sound,active_note):
    note.shape(active_note)
    note.showturtle()
    #playsound(active_sound)
    note.hideturtle()

#Events
drawPiano()
'''wn.onkeypress(playNote("C3.wav","C3Down.gif"),'a')
wn.onkeypress(playNote("D3.wav","D3Down.gif"),'s')
wn.onkeypress(playNote("E3.wav","E3Down.gif"),'d')
wn.onkeypress(playNote("F3.wav","F3Down.gif"),'f')
wn.onkeypress(playNote("G3.wav","G3Down.gif"),'g')
wn.onkeypress(playNote("A3.wav","A3Down.gif"),'h')
wn.onkeypress(playNote("B3.wav","B3Down.gif"),'j')
wn.onkeypress(playNote("C4.wav","C4Down.gif"), 'k')
wn.onkeypress(playNote("D4.wav","D4Down.gif"), 'l')
wn.onkeypress(playNote("E4.wav","E4Down.gif"),';')'''

wn.listen()
wn.mainloop()