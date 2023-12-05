import pytesseract
from pytesseract import Output
import cv2

slika = cv2.imread("1234567890.png")

blur = cv2.medianBlur(slika, 5)
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

obrisi = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
if len(obrisi) == 2:
    obrisi = obrisi[0]
else:
    obrisi = obrisi[1]
for obris in obrisi:
    x,y,h,w = cv2.boundingRect(obris)
    cv2.rectangle(slika, (x, y), (x+w, y+h), (0, 255, 0), 2)

custom_config = r"--oem 1 --psm 4"
print(pytesseract.image_to_string(slika, config=custom_config))


cv2.imshow("slika", slika)
cv2.waitKey(0)