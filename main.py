####################################################
# Essa é pra vocês que me cobraram igual um agiota #
####################################################

import pyglet, random

# Cria a janela utilizando pyglet e define uma posição fixa de inicialização na tela
window = pyglet.window.Window(width= 640, height= 640, caption= 'Romance')
window.set_location(350,120)

background = pyglet.shapes.Rectangle(0,0, 640, 640, color=(255,140,180,255))

question = pyglet.text.Label('Quer namorar comigo?',
                          font_name='Arial',
                          font_size=33,
                          x=100, y=520,
                          italic= True,)
message = pyglet.text.Label("Tinha certeza que você ia dizer sim <3",
                            font_name='Arial',
                            font_size=24,
                            x=40, y=40)
#Botão sim
yes = pyglet.graphics.Batch()
yesbutton = [pyglet.shapes.Rectangle(100,380,100,50, color= (255,60,80,255),batch= yes),
            pyglet.shapes.Circle(100,405, 25, color= (255,60,80,255),batch= yes),
            pyglet.shapes.Circle(200,405, 25, color= (255,60,80,255),batch= yes),
            pyglet.text.Label('Sim', font_name='Arial', font_size=20, x=125, y=393,batch= yes)
            ]

#Botão Não
no = pyglet.graphics.Batch()
nobutton = [pyglet.shapes.Rectangle(120,400,100,50, color= (255,60,80,255),batch= no),
            pyglet.shapes.Circle(120,425, 25, color= (255,60,80,255),batch= no),
            pyglet.shapes.Circle(220,425, 25, color= (255,60,80,255),batch= no),
            pyglet.text.Label('Não', font_name='Arial', font_size=20, x=145, y=413,batch= no)
            ]

def moveButton():
    '''
    Move o botão aleatoriamente pela tela
    '''
    x = random.randint(100,540)
    y = random.randint(100,540)
    nobutton[0].x, nobutton[0].y = x, y
    nobutton[1].x, nobutton[1].y = x, y + 25
    nobutton[2].x, nobutton[2].y = x + 100, y + 25
    nobutton[3].x, nobutton[3].y = x + 25 , y + 13

hidden = True
#Desenha as informações na tela
@window.event
def on_draw():
    background.draw()
    question.draw()
    yes.draw()
    no.draw()
    if not hidden:
        message.draw()

#Detecta quando o mouse passa por cima do botão "Não"
@window.event
def on_mouse_motion(x, y, dx, dy):
    if nobutton[0].x - 25 < x < nobutton[0].x + 125 and nobutton[0].y - 15 < y < nobutton[0].y + 65:
        moveButton()
        no.draw()

#Detecta onde o mouse clicou
@window.event
def on_mouse_press(x,y,button,modifiers):
    if 75 < x < 225 and 365 < y < 445:
        global hidden
        hidden = False
        
pyglet.app.run()
