from math import sqrt
from PIL import Image
MAX_ITER = 50
def reccurenceMandelbrot(c):
    x = c[0]
    x1 = c[0]
    y = c[1]
    y1 = c[1]
    n = 0
    while n<MAX_ITER and sqrt(x**2 + y**2) < 2:
        n+=1
        x = x**2-y**2+c[0]
        y = 2*x1*y+c[1]
        x1 = x1**2-y1**2+c[0]
        y1 = y
    return [x, y]
def appartientAEnsembleMandelbrot(c) :
    if sqrt(reccurenceMandelbrot(c)[0]**2 + reccurenceMandelbrot(c)[1]**2) < 2:
        return True
    else:
        return False
#CORPS DE PROGRAMME
LARG, HAUT = 6000, 6000
MIN_X, MAX_X = -2, 2
MIN_Y, MAX_Y = -2, 2
coef_x = (MAX_X - MIN_X)/LARG
coef_y = (MAX_Y - MIN_Y)/HAUT
img = Image.new('RGB', [LARG,HAUT], (0,0,0))
data = img.load()
for i in range(img.size[0]):
    x = i*coef_x + MIN_X
    for j in range(img.size[1]):
        y = j*coef_y + MIN_Y
        c = (x,y)
        conclusion = appartientAEnsembleMandelbrot(c)
        if conclusion :
            data[i,j] = (255,255,255)
        else :
            data[i,j] = (0,0,0)
img.save('image.png')
img.show()
