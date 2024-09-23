#Libraries
import turtle as trtl
import turtle as tortle

#Variables
    #Screen/Piano
phil = trtl.Turtle()
wn = trtl.Screen()
piano = 'Piano.gif'
wn.addshape(piano)
wn.tracer(False)
pianoX = 0
pianoY = 0
phil.hideturtle()
keys = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C', 'D', 'E', 0]
keyboardKeys = ['A','S','D','F','G','H','J','K','L',';',0]
    #Writer
writer = tortle.Turtle()
writerX = -250
writerY = -110
writerColor = "black"
writerFont = "Arial", 45, "bold"
writerFontKeyboard = "Arial",45
currentLetter = keys.pop(0)
writerInterval = 51

#Turtle setup
writer.hideturtle()
writer.shape('classic')
writer.color(writerColor)
writer.penup()
writer.goto(writerX,writerY)


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

def writeKeyboardLetter(): #draws keys that correspond to piano keys
    wn.tracer(False)
    global currentLetter
    global writerInterval
    currentLetter = keyboardKeys.pop(0)
    writer.write(currentLetter, font=(writerFontKeyboard))
    writer.forward(writerInterval)


#Events
drawPiano()

wn.listen()
wn.mainloop()