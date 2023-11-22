from math import sqrt
from PIL import Image
MAX_ITER = 50
def reccurenceMandelbrot(m, c):
    x = m[0]**2-m[1]**2
    y = 2*m[0]*m[1]+c[0]
    return [x, y]
def appartientAEnsembleMandelbrot(c) :
    m = [0,0]
    d = sqrt(m[0]**2+m[1]**2)
    n=0
    while d < 2 and n < MAX_ITER:
        m = reccurenceMandelbrot(m,c)
        n+= 1
        d = sqrt(m[0]**2+m[1]**2)
        if n >= MAX_ITER:
            return False
    return True
#CORPS DE PROGRAMME
LARG, HAUT = 600, 600
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
