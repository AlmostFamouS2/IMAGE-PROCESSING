import cv2 as cv

o = cv.imread('MATH.PNG')
img = cv.imread('book.jpg')
img = cv.cvtColor(img, cv.COLOR_RGB2GRAY) # Tornando a imagem que era colorida em uma imagem preto e branco.  Porque nao precisamos de cor

img = cv.resize(img, (1200,800))

adaptive = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv.THRESH_BINARY, 101, 5)

adaptive = cv.resize(adaptive, (1200,800))

cv.imshow('title', img)
cv.imshow('asd', o)
cv.imshow('ADAPTIVE', adaptive)

cv.waitKey(0)  # Se vc aperta 0, vc fecha tudo  