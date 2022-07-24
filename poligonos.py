#CARLOS DANIEL ESTRDA VEGA, CARNÉ 20853
#GRÁFICAS POR COMPUTADORAS
#LABORATORIO 2

from gl import Renderer, color, V2
import random

width = 960
height = 540

rend = Renderer(width, height)

#Dibujar los polígonos 
def drawPoli(poligono, clr = None):
    for i in range(len(poligono)):
        rend.glLine(poligono[i],
                    poligono[ (i + 1) % len(poligono)],
                    clr)

pol1 = [ V2(165, 380), V2(185, 360), V2(180, 330),
         V2(207, 345), V2(233, 330), V2(230, 360),
         V2(250, 380), V2(220, 385), V2(205, 410),V2(193, 383)]

pol2 = [V2(321, 335), V2(288, 286), V2(339, 251), V2(374, 302)]

pol3 = [V2(377, 249), V2(411, 197), V2(436, 249)]

pol4 = [V2(413, 177), V2(448, 159), V2(502, 88), V2(553, 53),
        V2(535, 36),  V2(676, 37),  V2(660, 52), V2(750, 145),
        V2(761, 179), V2(672, 192), V2(659, 214),V2(615, 214),
        V2(632, 230), V2(580, 230), V2(597, 215),V2(552, 214),
        V2(517, 144), V2(466, 180)]

pol5 = [V2(682, 175), V2(708, 120), V2(735, 148), V2(739, 170)]

drawPoli(pol1, color(1,0.5,0.5))
drawPoli(pol2, color(0.5,1,0.5))
drawPoli(pol3, color(0.5,0.5,1))
drawPoli(pol4, color(1,1,1))
drawPoli(pol5, color(1,1,1))


#rellenado del triángulo
rend.glTriangle(V2(377,249),V2(411,197), V2(436,249), color(0.5,0.5,1))

#rellenado del cubo
rend.glTriangle(V2(288,286),V2(339,251), V2(374,302), color(0.5,1,0.5))
rend.glTriangle(V2(374,302),V2(321,335), V2(288,286), color(0.5,1,0.5))

#rellenado de la estrella: 
rend.glTriangle(V2(185,360),V2(180,330), V2(207,345), color(0.5,0.5,1))
rend.glTriangle(V2(207,345),V2(233,330), V2(230,360), color(0.5,0.5,1))
rend.glTriangle(V2(230,360),V2(250,380), V2(220,385), color(0.5,0.5,1))
rend.glTriangle(V2(220,385),V2(205,410), V2(193,383), color(0.5,0.5,1))
rend.glTriangle(V2(193,383),V2(165,380), V2(185,360), color(0.5,0.5,1))
rend.glTriangle(V2(185,360),V2(207,345), V2(230,360), color(0.5,0.5,1))
rend.glTriangle(V2(185,360),V2(230,360), V2(193,383), color(0.5,0.5,1))
rend.glTriangle(V2(193,383),V2(220,383), V2(230,360), color(0.5,0.5,1))
rend.glTriangle(V2(185,360),V2(205,410), V2(220,385), color(0.5,0.5,1))

#rellenado tetera 
rend.glTriangle(V2(413,177), V2(448,159), V2(466,180), color(1,1,1))
rend.glTriangle(V2(466,180), V2(448,159), V2(502,88), color(1,1,1))
rend.glTriangle(V2(466,180), V2(502,88), V2(553,53), color(1,1,1))
rend.glTriangle(V2(553,53), V2(535,36), V2(676,37), color(1,1,1))
rend.glTriangle(V2(553,53), V2(676,37), V2(660,52), color(1,1,1))
rend.glTriangle(V2(466,180), V2(553,53), V2(660,52), color(1,1,1))
rend.glTriangle(V2(660,52), V2(708,120), V2(750,145), color(1,1,1))
rend.glTriangle(V2(708,120), V2(735,148), V2(750,145), color(1,1,1))
rend.glTriangle(V2(708,120), V2(750,145), V2(761,179), color(1,1,1))
rend.glTriangle(V2(708,120), V2(761,179), V2(739,170), color(1,1,1))
rend.glTriangle(V2(761,179), V2(672,192), V2(739,170), color(1,1,1))
rend.glTriangle(V2(672,192), V2(739,170), V2(682,175), color(1,1,1))
rend.glTriangle(V2(672,192), V2(659,214), V2(615,214), color(1,1,1))#
rend.glTriangle(V2(615,214), V2(632,230), V2(580,230), color(1,1,1))
rend.glTriangle(V2(615,214), V2(580,230), V2(597,215), color(1,1,1))
rend.glTriangle(V2(552,214), V2(517,144), V2(672,192), color(1,1,1))
rend.glTriangle(V2(597,215), V2(552,214), V2(672,192), color(1,1,1))
rend.glTriangle(V2(615,214), V2(552,214), V2(672,194), color(1,1,1))
rend.glTriangle(V2(600,214), V2(552,214), V2(672,194), color(1,1,1))
rend.glTriangle(V2(520,145), V2(672, 192), V2(660, 53), color(1,1,1))
rend.glTriangle(V2(673, 192), V2(660, 53), V2(710, 114), color(1,1,1))

# Rellenado tetera (oreja)
rend.glTriangle(V2(683,175), V2(708,121), V2(735,148), color(1,0,1))
rend.glTriangle(V2(682,175), V2(735,148), V2(739,170), color(1,0,1))

#Imprimir
rend.glFinish("output.bmp")