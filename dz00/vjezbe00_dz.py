import cv2

kamera = cv2.VideoCapture(0)
kamera_blue = False
kamera_green = False
kamera_red = False
kamera_gray = False


while True:
    ret, frame = kamera.read()

    cv2.imshow("kamera", frame)
    (kamera_r, kamera_g, kamera_b) = cv2.split(frame)

    if kamera_gray:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("kamera", gray)
    else:
        cv2.imshow("kamera", frame)

    if kamera_blue:
        blue = frame
        blue[:, :, 1] = 0
        blue[:, :, 2] = 0
        cv2.imshow("kamera", blue)
    else:
        cv2.imshow("kamera", frame)

    if kamera_green:
        green = frame
        green[:, :, 0] = 0
        green[:, :, 2] = 0
        cv2.imshow("kamera", green)
    else:
        cv2.imshow("kamera", frame) 

    if kamera_red:
        red = frame
        red[:, :, 0] = 0
        red[:, :, 1] = 0
        cv2.imshow("kamera", red)
    else:
        cv2.imshow("kamera", frame)
    
    if cv2.waitKey(1) == ord("b"):
        kamera_blue = not kamera_blue
    elif cv2.waitKey(1) == ord("g"):
        kamera_green = not kamera_green
    elif cv2.waitKey(1) == ord("r"):
        kamera_red = not kamera_red
    elif cv2.waitKey(1) == ord("s"):
        kamera_gray = not kamera_gray
    elif cv2.waitKey(1) & 0xff == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()